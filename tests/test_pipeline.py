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


def test_csv_au_format_francais(tmp_path):
    """Séparateur « ; » et décimales avec une virgule : lisibles par un Power BI en français sans réglage."""
    racine = copie_projet(tmp_path)
    run(racine)
    lignes = (racine / 'data' / 'gold' / 'csv' / 'points_meteo.csv').read_text(encoding='utf-8-sig').splitlines()
    assert lignes[0] == 'id_point;latitude;longitude;commune;code_departement'
    assert lignes[1].split(';')[1] == '48,197'          # latitude avec une virgule
    assert lignes[1].split(';')[0] == '48.197_2.800'    # l'identifiant (texte) ne change pas


def test_entrepot_duckdb(tmp_path):
    """L'entrepôt DuckDB contient les 7 tables gold, avec le même nombre de lignes."""
    import duckdb
    racine = copie_projet(tmp_path)
    lignes = run(racine)
    con = duckdb.connect(str(racine / 'data' / 'gold' / 'entrepot.duckdb'), read_only=True)
    tables = {t for (t,) in con.execute('SHOW TABLES').fetchall()}
    assert tables == set(lignes)
    for table, n in lignes.items():
        assert con.execute(f'SELECT count(*) FROM {table}').fetchone()[0] == n
    # Un jour, pas une date et heure
    types_date = con.execute("SELECT DISTINCT data_type FROM information_schema.columns WHERE column_name = 'date'").fetchall()
    assert types_date == [('DATE',)]
    # Les vides restent vides (inconnu), jamais 0
    assert con.execute("SELECT count(*) FROM suivi_journalier_departement WHERE code_departement = '75' AND nb_feux IS NOT NULL").fetchone()[0] == 0
    con.close()


def test_entrepot_reconstruit(tmp_path):
    """Relancer le pipeline remplace l'entrepôt au lieu d'ajouter des lignes."""
    import duckdb
    racine = copie_projet(tmp_path)
    run(racine)
    lignes = run(racine)
    con = duckdb.connect(str(racine / 'data' / 'gold' / 'entrepot.duckdb'), read_only=True)
    assert con.execute('SELECT count(*) FROM feux_de_foret').fetchone()[0] == lignes['feux_de_foret']
    con.close()
