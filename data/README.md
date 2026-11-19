# data/

| Dossier | Contenu | Versionné ? |
|---|---|---|
| `bronze/` | Les sources brutes, jamais modifiées. Provenance et empreintes dans `bronze/SOURCES.md` | Oui, partagé par tout le groupe |
| `silver/` | Les données nettoyées par le pipeline | Non, recalculé par le pipeline |
| `gold/` | Les tables prêtes pour les indicateurs | Non, recalculé par le pipeline |
| `.env` | Les clés d'API (Météo-France…) | **Jamais** |

Tout ce qui est hors de `bronze/` reste sur ton poste : fichiers de travail, téléchargements intermédiaires, exports personnels.
