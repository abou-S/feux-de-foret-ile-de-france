# data/

| Dossier | Contenu | Versionné ? |
|---|---|---|
| `bronze/` | Les sources brutes, jamais modifiées. Provenance et empreintes dans `bronze/SOURCES.md` | Oui, partagé par tout le groupe |
| `silver/` | Les données nettoyées par le pipeline | Non, recalculé par le pipeline |
| `gold/` | Le schéma en étoile lu par Power BI (Parquet, et CSV dans `gold/csv/`), produit par `python -m pipeline` | Oui, pour que Power BI n'ait besoin que d'un `git pull` |
| `rapport_qualite.md` | Le résultat des règles de qualité du dernier chargement | Oui |
| `journal_chargement.csv` | Une ligne par fichier lu et par exécution (empreinte, lignes lues) | Non |
| `.env` | Les clés d'API (Météo-France…) | **Jamais** |

Tout ce qui est hors de `bronze/` reste sur ton poste : fichiers de travail, téléchargements intermédiaires, exports personnels.
