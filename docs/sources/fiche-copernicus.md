# Fiche source - Copernicus : indices de danger feux historiques

Explorée par : Daryl William Fabo (17/11/2026). Complétée le 20/11/2026 avec les fichiers déposés dans `data/bronze/copernicus/`.

Lien : https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1 (« Fire danger indices historical data from the Copernicus Emergency Management Service »)

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Copernicus Emergency Management Service (Union européenne), produit par l'ECMWF |
| Mode d'accès et format | API avec compte (Early Warning Data Store). Format d'origine NetCDF ou GRIB (multidimensionnel). Daryl l'a converti en CSV pour l'Île-de-France |
| Grain (une ligne = ?) | Fichier natif : un jour × un point de grille (environ 30 km d'écart). Fichiers déposés : un jour × un point (`_idf`, `_77`) et un jour × un département (`_idf_dept_jour`, moyenne des points du département) |
| Emprise géographique | Monde. Fichiers déposés : Île-de-France, 13 points (6 dans le 77). Aucun point dans le 75, le 92 et le 93 (trop petits) |
| Période réellement couverte | Annoncée : depuis 1940. Fichiers déposés : du 01/01/2024 au 31/08/2026, **toute l'année** (pas seulement l'été). 2016-2023 à déposer (#46) |
| Date de dernière mise à jour affichée | 16/11/2026 ; un avis annonce une suspension des mises à jour à partir de cette date |
| Fréquence de mise à jour | Quotidienne (suspendue depuis le 16/11/2026) |
| Volumétrie | Fichier complet téléchargé : plus de 1 Go. Fichiers Île-de-France : 4 745 lignes (points) et 1 825 lignes (départements) par an |
| Clés disponibles | `time` (jour), `latitude` + `longitude` (point), `code_departement` (ajouté par Daryl) |
| Données personnelles | Aucune : données météorologiques |
| Licence | Creative Commons Attribution (CC BY) |
| Questions servies | G2 (seuil sur le FWI, décision 008), G3 (danger les jours des feux), G4 (FWI comparable d'un département à l'autre), G5 (les indices détaillés) |

## Schéma de données

**`copernicus_AAAA_idf_dept_jour.csv`** (un jour × un département) :

| Colonne | Type | Exemple | Ce que c'est |
|---|---|---|---|
| `time` | date | 2025-01-01 | le jour |
| `code_departement` | entier | 77 | |
| `fwinx` | décimal | 1,05 | **FWI**, indice Forêt-Météo : l'indice de synthèse |
| `ffmcode` | décimal | 76,07 | FFMC : sécheresse des petits combustibles en surface |
| `dufmcode` | décimal | 0,92 | DMC : sécheresse de la couche organique intermédiaire |
| `drtcode` | décimal | 42,17 | DC : sécheresse profonde |
| `infsinx` | décimal | 3,32 | ISI : vitesse de propagation |
| `fbupinx` | décimal | 1,63 | BUI : combustible disponible |
| `fdsrte` | décimal | 0,03 | DSR : sévérité journalière |
| `fdimrk`, `buinfdr` | décimal | 1,06 ; 0 | indices d'autres systèmes (à vérifier) ; absents du fichier 2026 |

Valeur du département = **moyenne simple** des points de la grille du département (vérifié : 21,73 pour le 77 le 15/07/2025 = moyenne de ses 6 points).

**`copernicus_AAAA_idf.csv`** (un jour × un point) : mêmes indices, plus `latitude`, `longitude`, `code_departement`, `commune` (commune où tombe le point), et des colonnes techniques du format d'origine (`values`, `step`, `surface`, `valid_time`) non reprises.

Les coordonnées n'ont pas exactement les mêmes décimales d'un fichier à l'autre : le pipeline les arrondit à 3 décimales pour reconnaître le même point.

## Ce qu'on a découvert

- Le FWI est le **même indice** que l'IFM de Météo-France, celui qui sert de base à la Météo des forêts : il est continu, existe toute l'année et se compare d'un département à l'autre.
- C'est une **reconstitution après coup**, pas la prévision que le SDIS reçoit la veille.
- La moyenne du 77 **dilue** le danger : le point de Féricy, à 11 km de Fontainebleau, fait mieux pour repérer les jours de feu (notebook 03).
