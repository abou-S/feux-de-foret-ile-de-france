import pandas as pd
import pytest

from pipeline.qualite import ErreurQualite, barriere, rapport_markdown, regles_silver, separer_rejets


def feux(**changements):
    df = pd.DataFrame({'id_feu': ['2025-1', '2025-2'], 'code_departement': ['77', '77'],
                       'date_alerte': pd.to_datetime(['2025-04-01', '2025-05-01']), 'surface_m2': [10.0, 20.0]})
    for col, val in changements.items():
        df[col] = val
    return df


def mdf(niveaux=(1, 2)):
    return pd.DataFrame({'date_concernee': pd.to_datetime(['2025-06-04', '2025-06-04']),
                         'code_departement': ['77', '78'], 'niveau_j1': pd.array(niveaux, dtype='Int64')})


def cop_points():
    return pd.DataFrame({'date': pd.to_datetime(['2025-06-04']), 'latitude': [48.478], 'longitude': [2.8], 'fwi': [5.0]})


def test_tout_va_bien():
    resultats = regles_silver(feux(), mdf(), cop_points())
    assert len(resultats) == 9
    barriere(resultats)  # ne lève rien


def test_doublon_feu_bloque():
    with pytest.raises(ErreurQualite):
        barriere(regles_silver(feux(id_feu=['2025-1', '2025-1']), mdf(), cop_points()))


def test_departement_hors_idf_alerte():
    resultats = regles_silver(feux(code_departement=['77', '13']), mdf(), cop_points())
    alerte = [r for r in resultats if not r.reussi]
    assert len(alerte) == 1 and alerte[0].decision == 'alerter' and alerte[0].lignes_en_echec == 1
    barriere(resultats)  # une alerte ne bloque pas


def test_niveau_hors_1_4_bloque():
    with pytest.raises(ErreurQualite):
        barriere(regles_silver(feux(), mdf(niveaux=(1, 5)), cop_points()))


def test_separer_rejets():
    df = feux(surface_m2=[-1.0, 20.0])
    gardees, rejetees = separer_rejets(df, df['surface_m2'] < 0)
    assert len(gardees) == 1 and len(rejetees) == 1
    assert rejetees.iloc[0]['surface_m2'] == -1.0


def test_rapport_markdown():
    texte = rapport_markdown(regles_silver(feux(), mdf(), cop_points()))
    assert '| Règle | Table | Décision | Lignes en échec | Résultat |' in texte


def test_point_en_double_bloque():
    points = pd.concat([cop_points(), cop_points()])
    with pytest.raises(ErreurQualite):
        barriere(regles_silver(feux(), mdf(), points))
