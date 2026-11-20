"""Règles de qualité (sélecteur, prédicat, décision), barrière de qualité et rapport."""
from dataclasses import dataclass

import pandas as pd

DEP_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']


class ErreurQualite(Exception):
    """Une règle « bloquer » a échoué : le chargement s'arrête avant gold."""


@dataclass
class Resultat:
    table: str
    regle: str
    decision: str  # 'bloquer' ou 'alerter'
    lignes_en_echec: int

    @property
    def reussi(self) -> bool:
        return self.lignes_en_echec == 0


def _jours_manquants(dates: pd.Series) -> int:
    """Jours absents entre le premier et le dernier jour de chaque année (saison continue attendue)."""
    manquants = 0
    for _, d in pd.Series(dates.unique()).groupby(pd.Series(dates.unique()).dt.year):
        manquants += len(pd.date_range(d.min(), d.max())) - d.nunique()
    return manquants


def regles_silver(feux: pd.DataFrame, mdf: pd.DataFrame, cop_dep: pd.DataFrame, cop_points: pd.DataFrame) -> list[Resultat]:
    """Les 9 règles de pipeline/CONCEPTION.md, dans l'ordre du tableau."""
    deps_par_jour = mdf.groupby('date_concernee')['code_departement'].nunique()
    return [
        Resultat('feux', 'id_feu unique', 'bloquer', int(feux['id_feu'].duplicated().sum())),
        Resultat('feux', 'date d\'alerte et département renseignés', 'bloquer',
                 int((feux['date_alerte'].isna() | feux['code_departement'].isna()).sum())),
        Resultat('feux', 'département en Île-de-France', 'alerter', int((~feux['code_departement'].isin(DEP_IDF)).sum())),
        Resultat('feux', 'surface ≥ 0 (sinon rejet)', 'alerter', int((feux['surface_m2'] < 0).sum())),
        Resultat('meteo_des_forets', 'un seul niveau par (jour, département)', 'bloquer',
                 int(mdf.duplicated(['date_concernee', 'code_departement']).sum())),
        Resultat('meteo_des_forets', 'niveau entre 1 et 4', 'bloquer', int((~mdf['niveau_j1'].isin([1, 2, 3, 4])).sum())),
        Resultat('meteo_des_forets', 'même nombre de départements chaque jour, aucun jour manquant dans la saison', 'alerter',
                 int((deps_par_jour < deps_par_jour.max()).sum()) + _jours_manquants(mdf['date_concernee'])),
        Resultat('copernicus', 'un seul enregistrement par (jour, département) et par (jour, point)', 'bloquer',
                 int(cop_dep.duplicated(['date', 'code_departement']).sum()
                     + cop_points.duplicated(['date', 'latitude', 'longitude']).sum())),
        Resultat('copernicus', 'FWI ≥ 0 (sinon rejet)', 'alerter',
                 int((cop_dep['fwi'] < 0).sum() + (cop_points['fwi'] < 0).sum())),
    ]


def separer_rejets(df: pd.DataFrame, masque_rejet: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Les lignes non conformes vont dans une file de rejet, pas à la poubelle."""
    return df[~masque_rejet].reset_index(drop=True), df[masque_rejet].reset_index(drop=True)


def barriere(resultats: list[Resultat]) -> None:
    bloquants = [r for r in resultats if r.decision == 'bloquer' and not r.reussi]
    if bloquants:
        raise ErreurQualite('Règles bloquantes en échec : ' + ' ; '.join(f'{r.table} — {r.regle} ({r.lignes_en_echec})'
                                                                          for r in bloquants))


def rapport_markdown(resultats: list[Resultat]) -> str:
    lignes = ['# Rapport de qualité', '', '| Règle | Table | Décision | Lignes en échec | Résultat |', '|---|---|---|---|---|']
    for r in resultats:
        etat = 'réussite' if r.reussi else ('échec : chargement arrêté' if r.decision == 'bloquer' else 'échec : alerte')
        lignes.append(f'| {r.regle} | {r.table} | {r.decision} | {r.lignes_en_echec} | {etat} |')
    return '\n'.join(lignes) + '\n'
