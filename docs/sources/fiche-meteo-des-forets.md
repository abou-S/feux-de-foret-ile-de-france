# Fiche source - Archives de la Météo des forêts

Explorée par : Aboubacrine Seck, le 17/11/2026, complétée le 20/11/2026.

Liens :
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets
- Documentation Météo-France : https://confluence-meteofrance.atlassian.net/wiki/spaces/OpenDataMeteoFrance/pages/874741792/Donn+es+expertis+es
- API : https://portail-api.meteofrance.fr/web/fr/api/DonneesPubliquesMeteoForets

Fichiers : `data/bronze/meteo_des_forets/mdf_2024.csv`, `mdf_2025.csv`, `mdf_2026.csv` (provenance : `data/bronze/SOURCES.md`).

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Dispositif grand public lancé en 2023. Le niveau est établi à partir de l'IFM (indice Forêt-Météo), de la sécheresse de la végétation (relevés ONF), de la forêt du département, des zones sensibles aux feux et de l'avis d'un prévisionniste |
| Mode d'accès et format | Archives : un CSV par année (compressé en gzip), sans clé. API (clé Météo-France, en-tête `apikey`) : uniquement la diffusion en cours, de juin à septembre ; aucune date dans les paramètres, donc pas d'historique |
| Grain (une ligne = ?) | Un département, pour une prévision publiée un jour donné |
| Emprise géographique | France métropolitaine et Corse, 96 départements. Les 8 départements d'Île-de-France y sont |
| Période réellement couverte | Vérifié : 2024 du 03/06 au 30/09, 2025 du 03/06 au 30/09, 2026 du 28/05 au 05/10. Rien avant 2024 (la saison 2023 n'est pas archivée), rien d'octobre à mai |
| Date de dernière mise à jour affichée | 05/10/2026 |
| Fréquence de mise à jour | Quotidienne pendant la saison (publication à 17 h pour le lendemain et le surlendemain) |
| Volumétrie | 11 520 lignes en 2024 et en 2025, 12 576 en 2026 : environ 35 000 lignes en tout |
| Clés disponibles | `num_dep` (département) et `date` (publication) : jour concerné = date de publication + 1 jour pour `niveau_j1` |
| Données personnelles | Aucune |
| Licence | Licence Ouverte v2.0 |
| Questions servies | G2 (le niveau du seuil), G3 (jours de niveau bas), G4 (comparaison des départements, avec réserve) |

## Schéma de données (5 colonnes)

| Colonne | Type | Exemple | Remarque |
|---|---|---|---|
| `date` | date et heure (UTC) | 2025-06-03T14:50:06Z | heure de **publication**, pas le jour concerné |
| `num_dep` | texte | 1 | **sans zéro devant** (`1` et non `01`) |
| `niveau_j1` | entier (1 à 4) | 1 | niveau prévu pour le **lendemain** : 1 faible, 2 modéré, 3 élevé, 4 très élevé |
| `niveau_j2` | entier (1 à 4) | 1 | niveau prévu pour le surlendemain ; pas repris dans l'entrepôt |
| `nom_dep` (2024, 2026) ou `dep_nom` (2025) | texte | Ain | **le nom de la colonne change selon l'année** |

Le séparateur change aussi : `,` en 2024 et 2025, `;` en 2026. Le pipeline gère ces trois formats.

## Ce qu'on a découvert

- **Seulement 2024 à 2026** : on ne peut croiser l'indice et les feux que sur 2024 et 2025, et le 77 est au niveau 1 les 120 jours de 2024.
- **Le niveau n'est pas comparable d'un département à l'autre** : il tient compte de la forêt de chacun.
- **« N'est pas destinée aux SDIS »** (Météo-France, « 10 questions pour comprendre la Météo des forêts », 2024) : les SDIS reçoivent des indicateurs opérationnels séparés.
- **75, 92, 93, 94** ont les mêmes niveaux chaque jour : sans doute traités comme une seule zone.
