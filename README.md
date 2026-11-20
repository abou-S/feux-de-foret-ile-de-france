# Feux de forêt en Île-de-France : aide à la décision pour le SDIS 77

Projet HETIC, UE01. Client : le Service départemental d'incendie et de secours de Seine-et-Marne (SDIS 77), qui prépare la saison des feux 2027.

## La commande

La direction du SDIS 77 veut savoir deux choses :
1. **où concentrer ses moyens** pendant la saison des feux ;
2. **à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé**.

On l'a découpée en cinq questions analytiques :

| N° | Question |
|---|---|
| G1 | Les départs de feu du 77 sont-ils concentrés sur quelques communes, et sont-elles toujours les mêmes d'une année à l'autre ? |
| G2 | Pour chaque niveau de danger, quelle part des jours a connu un départ de feu, et combien de jours le dispositif serait-il déclenché selon le seuil ? |
| G3 | Quelle part des feux part les jours d'indice bas, et ces feux ont-ils des points communs ? |
| G4 | À niveau égal, le 77 a-t-il plus ou moins de feux que les autres départements d'Île-de-France ? |
| G5 | Quels indices météo (FWI, FFMC, DMC, DC) étaient associés aux départs de feu et aux plus gros feux ? |

Le détail, découpé en questions plus simples, est dans [docs/sources/matrice.md](docs/sources/matrice.md).

## Les sources

| Source | Ce qu'elle donne | Période |
|---|---|---|
| BDIFF (base de données sur les incendies de forêt en France) | un feu de forêt : jour, commune, surface, cause | 2016-2025 |
| Météo des forêts (Météo-France) | un niveau de danger de 1 à 4, par département et par jour | étés 2024-2026 |
| Copernicus (indices de danger feux) | le FWI et ses composantes, par jour, par département et par point de grille | 2024-2026, toute l'année |

Une fiche par source dans [docs/sources/](docs/sources/), et la provenance des fichiers dans [data/bronze/SOURCES.md](data/bronze/SOURCES.md).

## Organisation du dépôt

```
├── data/
│   ├── bronze/        les fichiers bruts, jamais modifiés
│   ├── silver/        une table propre par source (local, recalculé)
│   └── gold/          les 7 tables finales : entrepôt DuckDB, Parquet et CSV pour Power BI
├── pipeline/          le code qui passe de bronze à gold, avec les contrôles de qualité
├── tests/             les tests du pipeline
├── notebooks/         l'étude des données, question par question
├── kpi/               diagnostic, objectifs SMART et fiches indicateurs
└── docs/
    ├── sources/       fiches sources, matrice questions × sources, données manquantes
    ├── qualite/       qualité des données (ISO/IEC 25012) et données personnelles
    ├── glossaire.md
    ├── journal-des-decisions.md
    └── modele-cible.md
```

## Lancer le projet

Il faut Python 3.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python -m pipeline               # reconstruit silver et gold
pytest                           # lance les tests
```

Le pipeline s'arrête si une règle de qualité bloquante échoue. Le résultat de chaque contrôle est dans `data/rapport_qualite.md`.

Pour le tableau de bord, pas besoin de Python : les CSV de `data/gold/csv/` sont déjà dans le dépôt, au format du Power BI français.

## Les documents à lire en premier

| Pour comprendre… | Lire |
|---|---|
| les mots du projet | [docs/glossaire.md](docs/glossaire.md) |
| nos choix et pourquoi | [docs/journal-des-decisions.md](docs/journal-des-decisions.md) |
| le modèle de données | [docs/modele-cible.md](docs/modele-cible.md) et [data/gold/README.md](data/gold/README.md) |
| le fonctionnement du pipeline | [pipeline/README.md](pipeline/README.md) et [pipeline/CONCEPTION.md](pipeline/CONCEPTION.md) |
| ce qui nous manque | [docs/sources/donnees-manquantes.md](docs/sources/donnees-manquantes.md) |
| la qualité des données | [docs/qualite/qualite-iso25012.md](docs/qualite/qualite-iso25012.md) |

## Les limites à garder en tête

- Seulement **deux saisons** (2024 et 2025) pour croiser le niveau de danger et les feux.
- **Feux de forêt seulement** : les autres feux de végétation ne sont pas dans la BDIFF.
- **Paris et la petite couronne** (BSPP) : nombre de feux inconnu. Dans les données, une case vide veut dire « on ne sait pas », jamais 0.

## L'équipe

- Aboubacrine Seck
- Iris Pouth
- Daryl William Fabo
- Harold

## Licence

Code sous licence MIT (voir [LICENSE](LICENSE)). Les données gardent la licence de leur producteur (Licence Ouverte pour la BDIFF et Météo-France, CC BY pour Copernicus).
