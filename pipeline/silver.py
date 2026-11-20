"""Couche silver : une table propre par source (noms, types et formats harmonisés)."""
import pandas as pd


def code_departement(s: pd.Series) -> pd.Series:
    """Code département sur 2 caractères : '1' devient '01', '2A' ne change pas."""
    return s.astype(str).str.strip().str.zfill(2)


def silver_feux(brut: pd.DataFrame) -> pd.DataFrame:
    """Un feu par ligne (BDIFF). Un feu = une fiche BDIFF (décision 006)."""
    alerte = pd.to_datetime(brut['Date de première alerte'])
    return pd.DataFrame({
        'id_feu': brut['Année'].str.strip() + '-' + brut['Numéro'].str.strip(),
        'annee': brut['Année'].astype(int),
        'numero': brut['Numéro'].str.strip(),
        'code_departement': code_departement(brut['Département']),
        'code_insee': brut['Code INSEE'].str.strip(),
        'commune': brut['Nom de la commune'],
        'date_alerte': alerte,
        'date': alerte.dt.normalize(),
        'surface_m2': pd.to_numeric(brut['Surface parcourue (m2)']),
        'precision_surface': brut['Précision des surfaces'],
        'cause': brut['Nature'],
    })


def silver_meteo_des_forets(brut: pd.DataFrame) -> pd.DataFrame:
    """Un niveau par jour concerné et par département. niveau_j1 vaut pour le lendemain de la publication."""
    publication = pd.to_datetime(brut['date'], utc=True)
    concernee = publication.dt.tz_convert('Europe/Paris').dt.normalize().dt.tz_localize(None) + pd.Timedelta(days=1)
    return pd.DataFrame({
        'date_publication': publication,
        'date_concernee': concernee,
        'code_departement': code_departement(brut['num_dep']),
        'nom_departement': brut['nom_dep'],
        'niveau_j1': pd.to_numeric(brut['niveau_j1']).astype('Int64'),
        'niveau_j2': pd.to_numeric(brut['niveau_j2']).astype('Int64'),
    })


INDICES = {'fwinx': 'fwi', 'ffmcode': 'ffmc', 'dufmcode': 'dmc', 'drtcode': 'dc', 'infsinx': 'isi', 'fbupinx': 'bui'}


def silver_copernicus_departement(brut: pd.DataFrame) -> pd.DataFrame:
    """Indices Copernicus par jour et par département (moyenne des points, calculée par Daryl)."""
    s = brut.rename(columns={'time': 'date', **INDICES})
    s['date'] = pd.to_datetime(s['date'])
    s['code_departement'] = code_departement(s['code_departement'])
    return s[['date', 'code_departement', *INDICES.values()]].reset_index(drop=True)


def silver_copernicus_points(brut: pd.DataFrame) -> pd.DataFrame:
    """FWI par jour et par point de la grille. Coordonnées arrondies : leurs décimales changent d'un fichier à l'autre."""
    s = brut.rename(columns={'time': 'date', 'fwinx': 'fwi'})
    s['date'] = pd.to_datetime(s['date'])
    s['code_departement'] = code_departement(s['code_departement'])
    s['latitude'] = s['latitude'].round(3)
    s['longitude'] = s['longitude'].round(3)
    return s[['date', 'code_departement', 'commune', 'latitude', 'longitude', 'fwi']].reset_index(drop=True)
