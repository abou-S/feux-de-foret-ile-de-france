import shutil
from pathlib import Path

from pipeline.__main__ import run

RACINE = Path(__file__).resolve().parents[1]


def copie_projet(tmp_path):
    shutil.copytree(RACINE / 'data' / 'bronze', tmp_path / 'data' / 'bronze')
    return tmp_path


def test_run_produit_gold(tmp_path):
    racine = copie_projet(tmp_path)
    lignes = run(racine)
    for table in ['calendrier', 'departements', 'communes', 'points_meteo', 'feux_de_foret', 'suivi_journalier_departement', 'danger_journalier_point_meteo']:
        assert (racine / 'data' / 'gold' / f'{table}.parquet').exists()
        assert (racine / 'data' / 'gold' / 'csv' / f'{table}.csv').exists()
        assert lignes[table] > 0
    assert (racine / 'data' / 'rapport_qualite.md').exists()
    assert (racine / 'data' / 'journal_chargement.csv').exists()


def test_idempotent(tmp_path):
    racine = copie_projet(tmp_path)
    run(racine)
    premier = {p.name: p.read_bytes() for p in (racine / 'data' / 'gold' / 'csv').glob('*.csv')}
    run(racine)
    second = {p.name: p.read_bytes() for p in (racine / 'data' / 'gold' / 'csv').glob('*.csv')}
    assert premier == second


def test_csv_lisibles_par_power_bi(tmp_path):
    """Les CSV gold commencent par la marque UTF-8 : sans elle, Power BI peut mal afficher les accents."""
    racine = copie_projet(tmp_path)
    run(racine)
    for p in (racine / 'data' / 'gold' / 'csv').glob('*.csv'):
        assert p.read_bytes().startswith(b'\xef\xbb\xbf'), p.name


def test_gold_ne_garde_pas_d_anciennes_tables(tmp_path):
    racine = copie_projet(tmp_path)
    ancien = racine / 'data' / 'gold' / 'csv'
    ancien.mkdir(parents=True)
    (ancien / 'seuils_fwi.csv').write_text('vieux', encoding='utf-8')
    (racine / 'data' / 'gold' / 'seuils_fwi.parquet').write_text('vieux', encoding='utf-8')
    run(racine)
    assert not (ancien / 'seuils_fwi.csv').exists()
    assert not (racine / 'data' / 'gold' / 'seuils_fwi.parquet').exists()
