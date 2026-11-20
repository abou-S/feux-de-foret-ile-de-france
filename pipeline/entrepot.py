"""Entrepôt DuckDB : les tables gold dans une base SQL en un seul fichier, sans serveur."""
from pathlib import Path

import duckdb
import pandas as pd


def charger(tables: dict[str, pd.DataFrame], chemin: Path) -> None:
    """Reconstruit l'entrepôt : chaque table gold devient une table SQL du même nom."""
    chemin.unlink(missing_ok=True)
    con = duckdb.connect(str(chemin))
    try:
        for nom, df in tables.items():
            con.register('source', df)
            # Les colonnes `date` sont des jours : DATE plutôt que date et heure.
            dates = [c for c in df.columns if pd.api.types.is_datetime64_any_dtype(df[c])]
            remplace = f" REPLACE ({', '.join(f'CAST({c} AS DATE) AS {c}' for c in dates)})" if dates else ''
            con.execute(f'CREATE TABLE {nom} AS SELECT *{remplace} FROM source')
            con.unregister('source')
    finally:
        con.close()
