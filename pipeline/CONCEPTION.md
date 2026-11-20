# Pipeline bronze → silver → gold : conception

Statut : validée le 2026-11-20.

## Pourquoi

Le SDIS 77 veut un tableau de bord Power BI pour décider où mettre ses moyens et à partir de quand déclencher le dispositif renforcé. Le pipeline transforme nos sources brutes en un entrepôt **gold** qui permet de répondre aux cinq questions du groupe (G1 à G5). **Power BI ne lit que gold.**

**Le pipeline prépare, Power BI analyse.** Gold ne contient que des données propres, typées et reliées au bon grain. Les seuils, le menu par budget, les taux et les comparaisons se calculent dans Power BI.

Les notebooks (`notebooks/01`, `03`) ont servi à explorer. Le pipeline reprend ce qu'ils ont établi (formats, jointures, contrôles) sous forme de code propre, relançable.

## Objectifs

- Une seule commande, `python -m pipeline`, reconstruit silver et gold à partir de bronze.
- Gold est un schéma en étoile lisible par Power BI Desktop (Windows), en Parquet et en CSV.
- Chaque étape applique des règles de qualité, garde les lignes rejetées et écrit un rapport.
- Le pipeline peut être relancé autant de fois qu'on veut : même entrée, même sortie (idempotent).

## Hors périmètre

- La comparaison avec le reste de la France (décision 007) : Île-de-France seulement.
- Les massifs forestiers : aucune source ouverte ne les donne pour l'instant (décision 001).
- Les feux de 2026 : la BDIFF ne les publie pas encore. Ils sont « inconnus », pas 0.
- Le tableau de bord lui-même : il est construit dans Power BI, à partir de gold.

## Ce qui serait un échec, même si le code tourne

- Un 0 là où la donnée est inconnue (BSPP, 2026) : le tableau de bord ferait croire à une absence de feux.
- Des feux perdus pendant une jointure sans que personne ne le voie.
- Des colonnes chargées « au cas où » : chaque colonne de gold doit servir à une question.
- Des résultats d'analyse figés dans gold : ils doivent se calculer dans Power BI.

## Approches envisagées

| Approche | Avantages | Inconvénients |
|---|---|---|
| **A. Scripts Python (pandas), sorties Parquet + CSV** (retenue) | outils déjà installés et utilisés dans les notebooks ; Power BI lit Parquet et CSV sans configuration | pas de base de données à interroger en SQL |
| B. Entrepôt DuckDB (un fichier `.duckdb`) | requêtes SQL, proche d'un vrai entrepôt | Power BI demande un pilote ODBC à installer sur le poste Windows |
| C. Garder les notebooks comme pipeline | rien à écrire | pas relançable de façon fiable, mélange exploration et production |

A est retenue : c'est la plus simple pour la personne qui construit le tableau de bord sous Windows.

## Les sources (bronze)

Dans `data/bronze/`, décrites dans `data/bronze/SOURCES.md` :
- BDIFF : `bdiff/Incendies_2016_2025.csv` (Île-de-France, 2016-2025) ;
- Météo des forêts : `meteo_des_forets/mdf_2024.csv`, `mdf_2025.csv`, `mdf_2026.csv` ;
- Copernicus : `copernicus/copernicus_AAAA_idf_dept_jour.csv` (moyenne par département et par jour) et `copernicus_AAAA_idf.csv` (les 13 points de la grille en Île-de-France, avec leur département). Les années 2016-2023 arriveront avec #46 : le pipeline prend toutes les années présentes.

## Silver : une table propre par source

| Table | Grain | Traitements |
|---|---|---|
| `feux` | un feu | en-tête cherché automatiquement (2 ou 3 lignes d'information), noms de colonnes en minuscules, dates typées, surfaces en nombres, `id_feu` = Année + Numéro |
| `meteo_des_forets` | un jour × un département | séparateur et nom de colonne selon l'année, date de publication en UTC, `date_concernee` = date de publication en heure française + 1 jour, code département sur 2 caractères |
| `copernicus_departement` | un jour × un département | indices renommés (`fwi`, `ffmc`, `dmc`, `dc`, `isi`, `bui`) |
| `copernicus_points` | un jour × un point de la grille | coordonnées arrondies à 3 décimales (elles changent légèrement d'un fichier à l'autre) |

**Règles de qualité** (sélecteur, prédicat, seuil, décision), écrites comme des tests :

| Règle | Décision en cas d'échec |
|---|---|
| `feux` : `id_feu` unique | bloquer |
| `feux` : date d'alerte et département renseignés | bloquer |
| `feux` : département dans l'Île-de-France | alerter |
| `feux` : surface ≥ 0 | alerter, ligne en rejet |
| `meteo_des_forets` : un seul niveau par (jour, département) | bloquer |
| `meteo_des_forets` : niveau entre 1 et 4 | bloquer |
| `meteo_des_forets` : 96 départements chaque jour, aucun jour manquant dans la saison | alerter |
| `copernicus` : un seul enregistrement par (jour, département) ou (jour, point) | bloquer |
| `copernicus` : FWI ≥ 0 | alerter, ligne en rejet |

Une règle « bloquer » en échec arrête le pipeline avant gold. Les lignes rejetées vont dans `data/silver/rejets/`.

## Gold : le schéma en étoile

```
              calendrier
                 │
communes ─ feux_de_foret          suivi_journalier_departement ─ departements
                 │                       │
                 └───────── calendrier ────┘
                                         │
                       points_meteo ─ danger_journalier_point_meteo
```

**calendrier** : `date`, `annee`, `mois`, `saison_indice` (vrai si la Météo des forêts est publiée ce jour-là).

**departements** : `code_departement`, `nom`, `service` (SDIS ou BSPP), `feux_connus` (faux pour 75, 92, 93, 94).

**communes** : `code_insee`, `nom`, `code_departement`. Pas de massif (hors périmètre).

**feux_de_foret** (G1, G3) : `id_feu`, `date`, `code_insee`, `code_departement`, `surface_m2`, `precision_surface`, `cause`, `niveau_mdf_j1` du jour (vide hors saison), `fwi_departement` du jour.

**suivi_journalier_departement** (G2, G4, G5) : `date`, `code_departement`, `niveau_mdf_j1` (vide hors saison), `fwi_moyen`, `fwi_max` (maximum des points du département), `ffmc`, `dmc`, `dc`, `isi`, `bui`, `nb_feux`, `jour_avec_feu` (vide quand `nb_feux` est inconnu).
- `nb_feux` est **vide** (inconnu) pour la BSPP et pour les années sans BDIFF (2026), **0** sinon quand aucun feu.

**points_meteo** : `id_point`, `latitude`, `longitude`, `commune`, `code_departement` (les 13 points Copernicus en Île-de-France).

**danger_journalier_point_meteo** (G2, G5) : `date`, `id_point`, `fwi`. Permet d'étudier dans Power BI un point précis, par exemple le plus proche de Fontainebleau (décision 008), au lieu de la moyenne du département.

**Dans Power BI, pas dans gold :** le menu par budget (seuil, feux couverts, jours payés pour rien), les taux et les comparaisons.

**Sorties :** `data/gold/*.parquet` et `data/gold/csv/*.csv`.

## Traçabilité

- `data/rapport_qualite.md` : chaque règle, son résultat, sa décision, le nombre de lignes concernées.
- `data/journal_chargement.csv` : une ligne par exécution et par source (date, fichier, empreinte SHA-256, lignes lues, lignes rejetées, lignes en gold).

## Organisation du code

```
pipeline/
├── __main__.py      lance tout : silver, puis contrôles, puis gold
├── sources.py       lecture des fichiers bronze (formats différents selon l'année)
├── silver.py        nettoyage et harmonisation
├── qualite.py       les règles, la barrière de qualité, le rapport
└── gold.py          dimensions et faits
tests/               tests des transformations clés
```

Dépendance à ajouter : `pyarrow` (écriture Parquet), dans `requirements.txt`.

## Ce qui reste au choix de celui qui construit

- Le détail des noms de colonnes, tant qu'ils restent en minuscules et sans accents (plus simple dans Power BI).
- Le format exact du rapport de qualité.
- Les tests unitaires à écrire en plus de ceux des règles listées ci-dessus.

## Décidé

- **Gold est versionné** (`data/gold/` dans git) : la personne qui construit le tableau de bord sous Windows n'a qu'à faire `git pull` et ouvrir les fichiers dans Power BI. Silver reste local (recalculé par le pipeline). Le `.gitignore` et `data/README.md` sont à mettre à jour en conséquence.
