"""Lance le pipeline : bronze → silver → contrôles de qualité → gold.  Usage : python -m pipeline"""
import hashlib
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

from pipeline import gold, qualite, silver
from pipeline.sources import RACINE, fichiers, lire_bdiff, lire_copernicus, lire_meteo_des_forets


def _sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def _ecrire(df: pd.DataFrame, dossier: Path, nom: str, csv: bool = True) -> None:
    dossier.mkdir(parents=True, exist_ok=True)
    df.to_parquet(dossier / f'{nom}.parquet', index=False)
    if csv:
        (dossier / 'csv').mkdir(exist_ok=True)
        df.to_csv(dossier / 'csv' / f'{nom}.csv', index=False, encoding='utf-8-sig')  # marque UTF-8 pour Power BI


def run(racine: Path = RACINE) -> dict[str, int]:
    bronze, data = racine / 'data' / 'bronze', racine / 'data'
    journal = []

    def lire_tout(motif, lecteur):
        morceaux = []
        for chemin in fichiers(motif, bronze):
            df = lecteur(chemin)
            journal.append({'fichier': str(chemin.relative_to(bronze)), 'sha256': _sha256(chemin), 'lignes_lues': len(df)})
            morceaux.append(df)
        return pd.concat(morceaux, ignore_index=True)

    # Silver. Plusieurs exports BDIFF peuvent se recouvrir : on retire les lignes strictement identiques.
    # Un même feu avec des valeurs différentes resterait en double et bloquerait la barrière (règle id_feu unique).
    feux = silver.silver_feux(lire_tout('bdiff/*.csv', lire_bdiff).drop_duplicates())
    mdf = silver.silver_meteo_des_forets(lire_tout('meteo_des_forets/mdf_*.csv', lire_meteo_des_forets))
    cop_dep = silver.silver_copernicus_departement(lire_tout('copernicus/copernicus_*_idf_dept_jour.csv', lire_copernicus))
    cop_points = silver.silver_copernicus_points(lire_tout('copernicus/copernicus_*_idf.csv', lire_copernicus))

    resultats = qualite.regles_silver(feux, mdf, cop_dep, cop_points)
    (data / 'rapport_qualite.md').write_text(qualite.rapport_markdown(resultats), encoding='utf-8')
    qualite.barriere(resultats)

    feux, rejets_feux = qualite.separer_rejets(feux, feux['surface_m2'] < 0)
    cop_dep, rejets_dep = qualite.separer_rejets(cop_dep, cop_dep['fwi'] < 0)
    cop_points, rejets_points = qualite.separer_rejets(cop_points, cop_points['fwi'] < 0)
    rejets = data / 'silver' / 'rejets'
    rejets.mkdir(parents=True, exist_ok=True)
    for nom, df in [('feux', rejets_feux), ('copernicus_departement', rejets_dep), ('copernicus_points', rejets_points)]:
        df.to_csv(rejets / f'{nom}.csv', index=False, encoding='utf-8')
    for nom, df in [('feux', feux), ('meteo_des_forets', mdf), ('copernicus_departement', cop_dep), ('copernicus_points', cop_points)]:
        _ecrire(df, data / 'silver', nom, csv=False)

    # Gold
    fj = gold.suivi_journalier_departement(mdf, cop_dep, cop_points, feux)
    feux_idf = feux[feux['code_departement'].isin(gold.DEP_IDF)]
    ff = gold.feux_de_foret(feux_idf, mdf, cop_dep)
    tables = {
        'calendrier': gold.calendrier(fj, ff, mdf),
        'departements': gold.departements(mdf),
        'communes': gold.communes(feux_idf),
        'feux_de_foret': ff,
        'suivi_journalier_departement': fj,
        'points_meteo': gold.points_meteo(cop_points),
        'danger_journalier_point_meteo': gold.danger_journalier_point_meteo(cop_points),
    }
    # Gold est reconstruit en entier : on retire les tables d'une exécution précédente qui n'existent plus.
    for ancien in list((data / 'gold').glob('*.parquet')) + list((data / 'gold' / 'csv').glob('*.csv')):
        ancien.unlink()
    for nom, df in tables.items():
        _ecrire(df, data / 'gold', nom)

    horodatage = datetime.now().isoformat(timespec='seconds')
    nb_rejets = len(rejets_feux) + len(rejets_dep) + len(rejets_points)
    lignes_journal = pd.DataFrame([{'horodatage': horodatage, **j} for j in journal])
    lignes_journal['lignes_rejetees_total'] = nb_rejets
    chemin_journal = data / 'journal_chargement.csv'
    lignes_journal.to_csv(chemin_journal, mode='a', header=not chemin_journal.exists(), index=False, encoding='utf-8')
    return {nom: len(df) for nom, df in tables.items()}


if __name__ == '__main__':
    try:
        for table, n in run().items():
            print(f'{table:32} {n:>6} lignes')
        print('Rapport de qualité : data/rapport_qualite.md')
    except qualite.ErreurQualite as e:
        print(f'Chargement arrêté : {e}', file=sys.stderr)
        sys.exit(1)
