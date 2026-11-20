import pandas as pd

from pipeline.silver import (code_departement, silver_copernicus_departement, silver_copernicus_points,
                             silver_feux, silver_meteo_des_forets)


def test_code_departement():
    assert code_departement(pd.Series(['1', '77', ' 2A'])).tolist() == ['01', '77', '2A']


def test_date_concernee():
    brut = pd.DataFrame({'date': ['2025-06-03T14:50:06Z', '2024-06-03T16:00:00Z'], 'num_dep': ['77', '1'],
                         'niveau_j1': ['2', '1'], 'niveau_j2': ['1', '1'], 'nom_dep': ['Seine-et-Marne', 'Ain']})
    s = silver_meteo_des_forets(brut)
    assert s['date_concernee'].tolist() == [pd.Timestamp('2025-06-04'), pd.Timestamp('2024-06-04')]
    assert s['code_departement'].tolist() == ['77', '01']
    assert s['niveau_j1'].tolist() == [2, 1]


def test_silver_feux_id():
    brut = pd.DataFrame({'Année': ['2025'], 'Numéro': ['694'], 'Département': ['77'], 'Code INSEE': ['77186'],
                         'Nom de la commune': ['Fontainebleau'], 'Date de première alerte': ['2025-04-01 13:33:40'],
                         'Surface parcourue (m2)': ['200'], 'Précision des surfaces': ['Estimées'], 'Nature': [None]})
    s = silver_feux(brut)
    assert s.loc[0, 'id_feu'] == '2025-694'
    assert s.loc[0, 'surface_m2'] == 200.0
    assert s.loc[0, 'date'] == pd.Timestamp('2025-04-01')
    assert s.loc[0, 'annee'] == 2025


def test_copernicus_departement_renomme():
    brut = pd.DataFrame({'time': ['2025-07-15'], 'code_departement': ['77'], 'fwinx': [21.7], 'ffmcode': [90.0],
                         'dufmcode': [30.0], 'drtcode': [400.0], 'infsinx': [5.0], 'fbupinx': [60.0]})
    s = silver_copernicus_departement(brut)
    assert list(s.columns) == ['date', 'code_departement', 'fwi', 'ffmc', 'dmc', 'dc', 'isi', 'bui']
    assert s.loc[0, 'date'] == pd.Timestamp('2025-07-15')


def test_points_arrondis():
    brut = pd.DataFrame({'time': ['2024-07-01', '2025-07-01'], 'code_departement': ['77', '77'],
                         'commune': ['Féricy', 'Féricy'], 'latitude': [48.477732039271515, 48.47773203927152],
                         'longitude': [2.8, 2.8], 'fwinx': [10.0, 12.0]})
    s = silver_copernicus_points(brut)
    assert s['latitude'].unique().tolist() == [48.478]
    assert list(s.columns) == ['date', 'code_departement', 'commune', 'latitude', 'longitude', 'fwi']
