"""Lecture des fichiers de la couche bronze, tels qu'ils sont (formats différents selon la source et l'année)."""
from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
BRONZE = RACINE / 'data' / 'bronze'


def lire_bdiff(chemin: Path) -> pd.DataFrame:
    """Export CSV du portail BDIFF : 2 ou 3 lignes d'information avant l'en-tête, séparateur `;`."""
    lignes = Path(chemin).read_text(encoding='utf-8-sig').splitlines()
    entete = next(n for n, ligne in enumerate(lignes) if ligne.startswith('Année;'))
    return pd.read_csv(chemin, sep=';', skiprows=entete, dtype=str, encoding='utf-8-sig')


def lire_meteo_des_forets(chemin: Path) -> pd.DataFrame:
    """Archive annuelle de la Météo des forêts : séparateur `,` ou `;`, colonne `nom_dep` ou `dep_nom`."""
    premiere = Path(chemin).read_text(encoding='utf-8-sig').splitlines()[0]
    sep = ';' if premiere.count(';') > premiere.count(',') else ','
    df = pd.read_csv(chemin, sep=sep, dtype=str, encoding='utf-8-sig')
    df.columns = [c.strip() for c in df.columns]
    df = df.apply(lambda col: col.str.strip())
    return df.rename(columns={'dep_nom': 'nom_dep'})[['date', 'num_dep', 'niveau_j1', 'niveau_j2', 'nom_dep']]


def lire_copernicus(chemin: Path) -> pd.DataFrame:
    """Fichiers Copernicus (département × jour, ou points de la grille)."""
    return pd.read_csv(chemin, dtype={'code_departement': str})


def fichiers(motif: str, bronze: Path = BRONZE) -> list[Path]:
    """Fichiers bronze correspondant au motif, triés (ex. 'meteo_des_forets/mdf_*.csv')."""
    return sorted(Path(bronze).glob(motif))
