# Le modèle cible

Dernière mise à jour : 2026-11-20

Notre modèle de données local : ce qu'on prend dans chaque source, où on le range, et comment on a réglé les conflits entre sources. Le détail technique est dans `pipeline/CONCEPTION.md`, le dictionnaire des tables dans `data/gold/README.md`.

## 1. Le modèle

Sept tables, reliées par le jour, le département, la commune et le point de grille :

```
                                   calendrier
                    ┌──────────────────┼────────────────────────┐
                    │                  │                        │
communes ──── feux_de_foret   suivi_journalier_departement   danger_journalier_point_meteo ──── points_meteo
                    │                  │
                    └─── departements ─┘
```

| Table | Une ligne = | Questions |
|---|---|---|
| `feux_de_foret` | un feu de forêt | G1, G3 |
| `suivi_journalier_departement` | un jour dans un département | G2, G4, G5 |
| `danger_journalier_point_meteo` | un jour en un point de la grille Copernicus | G2, G5 |
| `calendrier`, `departements`, `communes`, `points_meteo` | listes de référence | filtres et noms |

## 2. Ce qu'on prend dans chaque source

On ne garde que les colonnes qui servent au moins une question (minimisation).

| Source | Colonne d'origine | Colonne cible | Table |
|---|---|---|---|
| BDIFF | `Année` + `Numéro` | `id_feu` | `feux_de_foret` |
| BDIFF | `Date de première alerte` | `date` (le jour, sans l'heure) | `feux_de_foret` |
| BDIFF | `Code INSEE`, `Nom de la commune` | `code_insee`, `nom` | `feux_de_foret`, `communes` |
| BDIFF | `Département` | `code_departement` | `feux_de_foret` |
| BDIFF | `Surface parcourue (m2)`, `Précision des surfaces` | `surface_m2`, `precision_surface` | `feux_de_foret` |
| BDIFF | `Nature` | `cause` | `feux_de_foret` |
| BDIFF | nombre de feux par jour et département | `nb_feux`, `jour_avec_feu` | `suivi_journalier_departement` |
| Météo des forêts | `date` + 1 jour | `date` | `suivi_journalier_departement` |
| Météo des forêts | `num_dep` | `code_departement` | `suivi_journalier_departement` |
| Météo des forêts | `niveau_j1` | `niveau_mdf_j1` | `suivi_journalier_departement`, `feux_de_foret` |
| Copernicus (département) | `fwinx`, `ffmcode`, `dufmcode`, `drtcode`, `infsinx`, `fbupinx` | `fwi_moyen`, `ffmc`, `dmc`, `dc`, `isi`, `bui` | `suivi_journalier_departement` |
| Copernicus (points) | maximum de `fwinx` des points du département | `fwi_max` | `suivi_journalier_departement` |
| Copernicus (points) | `latitude`, `longitude`, `commune`, `code_departement` | `id_point` et ses attributs | `points_meteo` |
| Copernicus (points) | `fwinx` | `fwi` | `danger_journalier_point_meteo` |

Laissées de côté : les 15 autres colonnes de la BDIFF (dont décès et bâtiments, voir `docs/qualite/donnees-personnelles.md`), `niveau_j2` de la Météo des forêts (prévision du surlendemain), `fdsrte`, `fdimrk` et `buinfdr` de Copernicus, et tout le fichier des interventions SIS.

## 3. Les conflits entre sources, et comment on les a réglés

| # | Conflit | Sources | Comment on l'a réglé | Où |
|---|---|---|---|---|
| 1 | **Quel jour ?** La Météo des forêts date le niveau du jour de **publication**, en heure UTC ; le niveau `j1` vaut pour le lendemain. La BDIFF date le feu à l'heure française | Météo des forêts, BDIFF | Jour concerné = date de publication en heure de Paris + 1 jour. Le feu est rattaché au niveau de son jour | `pipeline/silver.py`, glossaire « Date » |
| 2 | **Code du département** : `77` en texte dans la BDIFF, nombre sans zéro devant dans la Météo des forêts (`1` pour l'Ain au lieu de `01`), nombre dans Copernicus | les trois | Toujours du texte sur 2 caractères (`01`, `77`) | `code_departement()` dans `pipeline/silver.py` |
| 3 | **Format qui change selon l'année** : séparateur `,` (2024-2025) ou `;` (2026) ; colonne `nom_dep` ou `dep_nom` | Météo des forêts | Le séparateur est détecté, la colonne renommée en `nom_dep` | `pipeline/sources.py` |
| 4 | **En-tête de la BDIFF** précédé de 2 ou 3 lignes d'information selon l'export | BDIFF | On cherche la ligne qui commence par `Année;` | `pipeline/sources.py` |
| 5 | **Même point, coordonnées différentes** : les décimales changent légèrement d'un fichier Copernicus à l'autre | Copernicus | Coordonnées arrondies à 3 décimales | `pipeline/silver.py` |
| 6 | **Paris et petite couronne** : « nombre d'incendies inconnu » dans la BDIFF, une seule ligne BSPP dans le fichier SIS, quatre lignes dans la Météo des forêts | BDIFF, SIS, Météo des forêts | Quatre départements séparés ; leur `nb_feux` est **vide** (inconnu), jamais 0 | décision 007, `departements.feux_connus` |
| 7 | **Feu de forêt ou feu de végétation ?** La BDIFF ne compte que les feux de forêt, le fichier SIS tous les feux de végétation | BDIFF, SIS | Définition de référence : un départ de feu = une fiche BDIFF. Le fichier SIS n'est pas chargé | décision 006, glossaire |
| 8 | **Niveau de danger ou indice ?** La Météo des forêts donne un niveau de 1 à 4, ajusté à la forêt de chaque département ; Copernicus donne le FWI, une valeur continue calculée pareil partout | Météo des forêts, Copernicus | Les deux sont gardés dans des colonnes séparées, jamais convertis l'un dans l'autre | décision 008, glossaire « FWI » |
| 9 | **Indice au département** : la valeur Copernicus du département est une moyenne de points, qui dilue le danger | Copernicus | On garde aussi le maximum (`fwi_max`) et la valeur de chaque point | `suivi_journalier_departement`, `danger_journalier_point_meteo` |
| 10 | **Périodes différentes** : feux 2016-2025, Météo des forêts juin-septembre 2024-2026, Copernicus toute l'année 2024-2026 | les trois | Un calendrier continu de 2016 à 2026. Vide quand une source n'a rien ce jour-là, jamais 0 | `calendrier`, `data/gold/README.md` |

## 4. Ce qui contrôle l'alignement

- Les 9 règles de qualité du pipeline (`docs/qualite/qualite-iso25012.md`), dont « un seul niveau par jour et département » et « un seul enregistrement Copernicus par jour et département ».
- Un test qui vérifie que chaque feu de 2024-2025 est bien rattaché à un jour du suivi journalier.
- Un test qui vérifie que les départements de la BSPP restent « inconnus ».
