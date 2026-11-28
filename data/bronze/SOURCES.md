# Couche bronze : provenance des fichiers

Les fichiers de ce dossier sont les copies brutes des sources. **On ne les modifie jamais** (pas d'ouverture avec « Align » ou « Format » dans VS Code, pas d'enregistrement depuis Excel). Le pipeline les lit, et écrit ses résultats ailleurs (`data/silver/`, `data/gold/`).

Pour vérifier qu'un fichier n'a pas été modifié : `shasum -a 256 <fichier>`, à comparer avec l'empreinte ci-dessous.

| Fichier | Source | Comment il a été obtenu | Date d'extraction | Empreinte SHA-256 |
|---|---|---|---|---|
| `bdiff/incendies_idf_2024_2025.csv` | BDIFF, https://bdiff.agriculture.gouv.fr/incendies | Export CSV manuel du portail. Critères : date de première alerte du 01/01/2024 au 31/12/2025, zone de défense Île-de-France, type de feu F (forêt). Fichier `Incendies.csv` du zip, seulement renommé | 2026-11-19 | `b99caf12729e420fcc23c939f4ac57d3b035f977e2b5850ba01cc899eb43cd6c` |
| `bdiff/Incendies_2016_2025.csv` | BDIFF, https://bdiff.agriculture.gouv.fr/incendies | Export CSV manuel du portail. Critères : date de première alerte du 01/01/2016 au 31/12/2025, zone de défense Île-de-France, type de feu F. 291 feux (251 dans le 77). **3 lignes d'information** avant l'en-tête (dont un avertissement sur l'ancienne version du formulaire). **C'est le fichier BDIFF de référence** : il contient aussi tous les feux de `incendies_idf_2024_2025.csv` (vérifié, identiques) | 2026-11-20 | `8b17fab3b900b3864a4117742a06ea7186b1300dd5be19816086d4763f6f680b` |
| `meteo_des_forets/mdf_2024.csv` | Archives de la Météo des forêts, Météo-France (data.gouv.fr) | Téléchargement de https://meteofrance.s3.sbg.io.cloud.ovh.net/data/BULLETIN/MDF/mdf_2024.csv.gz, décompressé | 2026-11-19 | `53c1b0d89633afd3dbae17004affca64998654d77db7047e0abd607a8f2d6568` |
| `meteo_des_forets/mdf_2025.csv` | Idem | Idem, `mdf_2025.csv.gz` | 2026-11-19 | `383c34692ed322c5ef14ef8b5c02c7b03d07c08a060eeeda2a98f0586313e15a` |
| `meteo_des_forets/mdf_2026.csv` | Idem | Idem, `mdf_2026.csv.gz` | 2026-11-19 | `5542af01679987c277edb49ccaf6651dc0b7dd6e1f76a91c152b1fd0a8dc05b3` |
| `copernicus/copernicus_2022_77.csv` | Copernicus CEMS (EWDS), `cems-fire-historical-v1` | Extraction GRIB ERA5 (2022, 365 jours, emprise IdF) filtrée sur les 6 points de grille du 77, avec `commune_77` associée (9 indices : 7 FWI canadiens + `fdimrk`, `buinfdr`) | 2026-11-27 | `1feb84aa36c261fd15756a74fc304bdc5534e45fa2df332743a02027dc04d4c6` |
| `copernicus/copernicus_2022_idf.csv` | Idem | Idem, 13 points de grille en Île-de-France (départements 77, 78, 91, 94, 95) | 2026-11-27 | `6c84cc6978c5b7a21a29ea23c4689aa8a17824bccb21d419c3ca54ea074ffb9c` |
| `copernicus/copernicus_2022_idf_dept_jour.csv` | Idem | Moyenne simple quotidienne par département calculée depuis `copernicus_2022_idf.csv` (5 départements) | 2026-11-27 | `e8e10b53af99581c434a5b45aa36c03f5e6d93cafa1527fdc2f9a187643be230` |
| `copernicus/copernicus_2023_77.csv` | Idem | Idem, année 2023 (365 jours, 6 points du 77, 9 indices) | 2026-11-27 | `8194307e633daf850935365328c44514672cb6d42dbbc697ed0e1df7aa175caa` |
| `copernicus/copernicus_2023_idf.csv` | Idem | Idem, année 2023 (13 points IdF) | 2026-11-27 | `425d1a3642832c0cd6205e7096acb0d966f8befe46dfbcd5902cd22ddf36a1cd` |
| `copernicus/copernicus_2023_idf_dept_jour.csv` | Idem | Moyenne simple quotidienne par département, 2023 | 2026-11-27 | `6895bb35958128e4969847e7b033c1bd9e3508274e847d9b57d4a174d5073078` |
| `copernicus/copernicus_2024_77.csv` | Copernicus CEMS (EWDS), `cems-fire-historical-v1` | Extraction GRIB ERA5 (2024, 366 jours, emprise IdF) filtrée sur les 6 points de grille du 77, avec `commune_77` associée (9 indices : 7 FWI canadiens + `fdimrk`, `buinfdr`) | 2026-11-19 | `4936b183ffa25a13dc7ac6eab778ed603a2e6b3ab16b5c6779c1fabe3c9af6ee` |
| `copernicus/copernicus_2024_idf.csv` | Idem | Idem, 13 points de grille en Île-de-France (départements 77, 78, 91, 94, 95) | 2026-11-19 | `ec0400f47699f7b8f06040f3cb3bceb7aae60add9718d77c646491c86406bd63` |
| `copernicus/copernicus_2024_idf_dept_jour.csv` | Idem | Moyenne simple quotidienne par département calculée depuis `copernicus_2024_idf.csv` (5 départements) | 2026-11-19 | `257acdaa5146b0f906eec140ec1e70ce9435e7c513a1a8300897bf9a0a850e2a` |
| `copernicus/copernicus_2025_77.csv` | Idem | Idem, année 2025 (365 jours, 6 points du 77, 9 indices) | 2026-11-19 | `f19691e9e39cfb332ef47c935fb05c7b4d7f4577e8ada41b9fb50d4959211e82` |
| `copernicus/copernicus_2025_idf.csv` | Idem | Idem, année 2025 (13 points IdF) | 2026-11-19 | `bbfa1182e8dff57fd5125e381530e97208dba17340fc47657a5c22b5d6894237` |
| `copernicus/copernicus_2025_idf_dept_jour.csv` | Idem | Moyenne simple quotidienne par département, 2025 | 2026-11-19 | `81390ad4b272380a3b1d40139fdb8b4cbcb3d9f2464897b406f0b978cd0c18dc` |
| `copernicus/copernicus_2026_77.csv` | Idem | Idem, année 2026 jusqu'au 2026-08-31 (243 jours, 6 points du 77, 7 indices FWI canadiens uniquement) | 2026-11-19 | `408f49e44406b5739332d4ca7ef24cb9738ea881bb8d18e43561bf5daaf57921` |
| `copernicus/copernicus_2026_idf.csv` | Idem | Idem, année 2026 jusqu'au 2026-08-31 (13 points IdF, 7 indices) | 2026-11-19 | `89e64a2d1792ada199e11054c9df99a633dee5cd42a780b6530288db747ef092` |
| `copernicus/copernicus_2026_idf_dept_jour.csv` | Idem | Moyenne simple quotidienne par département, 2026 jusqu'au 2026-08-31 | 2026-11-19 | `625c86573616d5ab0819ec736e7ef88a5871e79aa52ecf13812357e9968a1cb0` |

## Ce qu'il faut savoir avant de les lire

- **BDIFF :** séparateur `;`, encodage UTF-8, **2 ou 3 lignes d'information avant l'en-tête** selon l'export : chercher la ligne qui commence par `Année;`. Utiliser `Incendies_2016_2025.csv` ; `incendies_idf_2024_2025.csv` est gardé pour l'historique. Les départements 75, 92, 93 et 94 (BSPP) n'ont aucune ligne : leur nombre de feux est inconnu, ce n'est pas 0 (voir décision 007).
- **Météo des forêts :** le format change selon l'année.
  - 2024 : séparateur `,`, colonne `nom_dep`.
  - 2025 : séparateur `,`, colonne `dep_nom`.
  - 2026 : séparateur `;`, colonne `nom_dep`.
  - Dans les trois, `num_dep` n'a pas de zéro devant (`1` et non `01`), et `date` est l'heure de publication en UTC.
- **Copernicus CEMS (FWI) :** séparateur `,`, encodage UTF-8, pas de lignes d'information avant l'en-tête. Données quotidiennes à `12:00 UTC` (`valid_time`), issues du jeu `cems-fire-historical-v1` sur le portail EWDS (https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1), utilisées pour recommander un seuil sur le FWI (voir décision 008).
  - **Paramètres de requête EWDS :**
    - `dataset` : `cems-fire-historical-v1`
    - `product_type` : `reanalysis` (`dataset_type`: `consolidated_dataset`, `system_version`: `4_1`)
    - `variable` : les 7 indices du système canadien FWI présents sur toute la série (`2022-2026`) : `fire_weather_index` (`fwinx`), `build_up_index` (`fbupinx`), `drought_code` (`drtcode`), `duff_moisture_code` (`dufmcode`), `fine_fuel_moisture_code` (`ffmcode`), `fire_daily_severity_rating` (`fdsrte`), `initial_fire_spread_index` (`infsinx`). Les fichiers `2022`, `2023`, `2024` et `2025` contiennent aussi `fdimrk` (McArthur) et `buinfdr` (NFDRS), absents en `2026`.
    - `year` : `2022` à `2026` (`2026` s'arrête au `2026-08-31`), tous les mois (`01` à `12`) et tous les jours (`01` à `31`).
    - Sous-ensemble spatial appliqué après lecture GRIB : `48.1 <= latitude <= 49.1` et `1.6 <= longitude <= 3.6`, puis filtrage géométrique sur les contours administratifs d'Île-de-France.
  - **Grille spatiale et agrégation départementale :**
    - Les GRIB source utilisent la **grille gaussienne réduite ERA5 (N320)** (dimension `values`, pas en latitude ~0,281° / ~28–30 km, pas en longitude 0,40° à 48,76°N et 0,417° à 49,04°N).
    - **13 points de grille** tombent en Île-de-France : **6 dans le 77** (Étrépilly, Neufmoutiers-en-Brie, Choisy-en-Brie, Féricy, Paroy, Chaintreaux), 2 dans le 78 (Saint-Martin-la-Garenne, Trappes), 2 dans le 91 (Richarville, Videlles), 1 dans le 94 (Thiais) et 2 dans le 95 (Cergy, Louvres).
    - **75, 92 et 93 ont 0 point de grille :** la Petite Couronne (~48,80°–48,96°N) tombe entièrement dans l'intervalle entre deux rangées de latitudes N320 (`48.7588°N` et `49.0398°N`). Aucun centre de maille ne s'y trouve ; ces trois départements sont donc absents des fichiers `*_idf.csv` et `*_idf_dept_jour.csv`.
    - Les fichiers `copernicus_<annee>_idf_dept_jour.csv` contiennent la **moyenne simple** (arithmétique, non pondérée, float64 sans arrondi) par `(time, code_departement)` des points de grille situés dans chaque département.
- **Licences :** Licence Ouverte v2.0 pour BDIFF et Météo des forêts (fiches data.gouv.fr). Licence Copernicus CEMS / EWDS pour les indices FWI (usage libre avec mention de la source : *Generated using Copernicus Emergency Management Service information*). Aucune donnée personnelle.

## Mettre à jour un fichier

On ajoute un nouveau fichier daté plutôt que d'écraser l'ancien, et on ajoute une ligne à ce tableau.
