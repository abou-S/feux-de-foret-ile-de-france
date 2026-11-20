# Matrice questions × sources (v1)

Dernière mise à jour : 2026-11-20

Degrés : **complet** / **partiel** / **absent** / **inconnu**. Chaque degré a sa raison, avec la rubrique de la fiche ou la colonne du fichier.

Base : les analyses d'Aboubacrine, Iris et Daryl, et les fiches d'identité de l'inventaire. Les sources du défi que personne n'a ouvertes ne sont pas dans la matrice (voir plus bas).

## Questions retenues

| N° | Question du groupe | Posée par |
|---|---|---|
| G1 | Les départs de feu en Seine-et-Marne sont-ils concentrés sur quelques communes ou massifs, et ces zones restent-elles les mêmes d'une année à l'autre ? | Aboubacrine Q1, Iris Q1, Daryl Q1 |
| G2 | Pour chaque niveau de la Météo des forêts, quelle part des jours a connu au moins un départ de feu dans le 77, et combien de jours par été le dispositif renforcé serait-il déclenché selon le seuil ? | Aboubacrine Q2, Iris Q2 |
| G3 | Quelle part des feux démarre les jours d'indice bas, et ces feux ont-ils des points communs (cause, lieu, période) ? | Iris Q3, Aboubacrine Q3 (partie « jours d'indice bas ») |
| G4 | À niveau d'indice égal, le 77 a-t-il plus ou moins de feux que les autres départements d'Île-de-France ? (comparaison limitée à la région, décision 007) | Aboubacrine Q4, Iris Q4, Daryl Q4 |
| G5 | Quelles conditions météorologiques, mesurées par les indices de danger (Fire weather index, Drought code, Duff moisture code, Fine fuel moisture code), ont été associées aux départs de feu et aux incendies les plus importants dans le 77 ? | Daryl Q2 |

La numérotation de Daryl n'est pas la même dans sa section 1 et dans sa section 5 : ses questions 3 (seuil et moyens) et 4 (niveau de danger face aux incendies) sont inversées. On suit ici sa section 1.

## Questions atomiques

Chaque question du groupe est découpée en questions qui ne demandent qu'une seule chose, rangées par thème. C'est à ce niveau qu'on relie une question à une donnée précise. Les numéros G1 à G5 restent ceux utilisés dans le diagnostic, les objectifs et les fiches indicateurs.

| N° | Thème | Question atomique | Données nécessaires |
|---|---|---|---|
| G1a | Lieu | Quelle part des départs de feu du 77 part de chaque commune ? | commune de chaque feu |
| G1b | Lieu × temps | Les communes les plus touchées sont-elles les mêmes chaque année ? | commune et année de chaque feu |
| G1c | Lieu | Quelle surface brûle dans chaque commune ? | commune et surface de chaque feu |
| G2a | Danger × feux | Pour chaque niveau de la Météo des forêts, quelle part des jours a eu au moins un départ de feu dans le 77 ? | niveau du jour, feux du jour |
| G2b | Danger | Combien de jours par saison chaque niveau est-il atteint dans le 77 ? | niveau du jour |
| G2c | Danger × feux | Pour chaque valeur du FWI, quelle part des jours a eu au moins un départ de feu dans le 77 ? | FWI du jour, feux du jour (décision 008) |
| G3a | Danger × feux | Quelle part des feux du 77 part un jour de niveau 1, ou hors de la saison de l'indice ? | niveau du jour de chaque feu |
| G3b | Cause | Quelles sont les causes de ces feux ? | cause de chaque feu |
| G3c | Temps | À quels mois partent ces feux ? | date de chaque feu |
| G4a | Comparaison | Pour chaque département d'Île-de-France, quelle part des jours a eu un feu, à chaque niveau ? | niveau et feux du jour, par département |
| G4b | Comparaison | Combien de feux par an dans chaque département d'Île-de-France ? | département et année de chaque feu |
| G5a | Météo | Quelle valeur prend chaque indice (FWI, FFMC, DMC, DC, ISI, BUI) les jours avec feu, et les jours sans feu ? | indices du jour, feux du jour |
| G5b | Météo | Quelle valeur prennent ces indices les jours des plus gros feux ? | indices du jour, surface de chaque feu |

Non retenues telles quelles :
- Daryl Q3 (« quel seuil et quelle répartition des moyens offrent le meilleur compromis ») : c'est la décision de la direction, pas une question analytique. Elle demande aussi un coût que aucune source ne donne. G2 et G4 en sont la partie qu'on peut mesurer.
- Aboubacrine Q3 (« indice par secteur du 77 ») : fondue dans G3, car l'indice n'existe pas sous le département (voir décision 003).

## Matrice

| Question | BDIFF | Interventions SIS | Météo des forêts | Copernicus (EMS) |
|---|---|---|---|---|
| G1 | **partiel** : commune de chaque feu (Code INSEE, Nom de la commune), surface (Surface parcourue (m2)), date. 2016-2025 vérifié pour le 77 (fiche Iris). Pas de massif ni de coordonnées. 2026 absente | **absent** : une ligne par département et par an (Département, Numéro) | **absent** : que le niveau de danger (niveau_j1, niveau_j2) | **absent** : grille latitude × longitude d'indices de danger, pas de feux (rubrique Grain) |
| G2 | **partiel** : jour du feu (Date de première alerte) et Département. Seulement des feux de forêt, 2026 absente | **absent** : aucune date au jour | **partiel** : un niveau par jour et département (date, num_dep, niveau_j1), le 77 y est. Seulement 2024-2026, et le 77 est au niveau 1 les 120 jours de 2024 | **partiel** : FWI par jour, par département et par point (`fwinx`), toute l'année, vérifié dans les fichiers 2024-2026. Ce n'est pas le niveau de la Météo des forêts mais son indice de base. 2016-2023 à déposer (#46) |
| G3 | **partiel** : cause (Nature), Code INSEE, date. Cause manquante pour 132 feux sur 251 (fiche Iris). Pas de coordonnées donc pas de proximité routes ou habitations | **absent** : pas de feu individuel | **partiel** : indice au département seulement (num_dep) | **partiel** : FWI du jour de chaque feu, y compris d'avril à mai (`fwinx`, toute l'année). Pas plus fin que les 13 points de la grille |
| G4 | **partiel** : l'export Île-de-France 2024-2025 suffit pour la comparaison régionale (décision 007), mais « nombre d'incendies inconnu » pour 75, 92, 93, 94 (BSPP), 3 feux dans le 78 et le 91, aucun dans le 95. Pas de surface boisée | **partiel** : « Feux de végétations » par département et par an, mais aucune date, et une seule ligne pour la BSPP | **partiel** : 96 départements par jour (num_dep, niveau_j1). Le niveau dépend de la forêt de chaque département (présentation PDF), donc pas comparable tel quel | **partiel** : FWI calculé avec la même formule partout, donc comparable entre 77, 78, 91, 94 et 95. Aucun point dans le 75, le 92 et le 93 |
| G5 | **partiel** : c'est le côté « feux » de la question : jour (Date de première alerte), commune (Code INSEE) et surface (Surface parcourue (m2)) de chaque feu, ce qui permet de trouver les plus gros. Aucune condition météo : il faut croiser avec les indices | **absent** : une ligne par département et par an, ni feu individuel ni date | **partiel** : un niveau de synthèse de 1 à 4 par jour et par département (niveau_j1), calculé d'après l'indice de danger intégré (présentation PDF). Ce n'est pas la valeur des indices eux-mêmes, et les composantes (Drought code, Duff moisture code, Fine fuel moisture code) n'y sont pas. 2024-2026 seulement | **partiel** : Fire weather index, Drought code, Duff moisture code et Fine fuel moisture code, quotidiens depuis 1940 (fiche de Daryl, rubriques Grain et Période). Aucun feu. Grille latitude × longitude, pas de département ni de commune. Vérifié dans les fichiers 2024-2026 (`fwinx`, `ffmcode`, `dufmcode`, `drtcode`). 2016-2023 manquent (#46), mises à jour suspendues depuis le 16/11/2026 |

Pour G5, ni la BDIFF ni Copernicus ne suffisent seules : il faut les croiser par la date. Le croisement par le lieu demande de rattacher les cellules de la grille au département du 77, ou de placer les communes de la BDIFF sur la grille.

Aucune question n'a de source « complet ».

## Lecture dans les deux sens

**Questions sans source complète.** Toutes. Les manques qui reviennent :
- les massifs (G1) : aucune source ne localise les feux plus finement que la commune ;
- un historique de l'indice de plus de 3 saisons (G2, G4) ;
- les feux de 2026, la saison la plus utile, pas encore diffusée par la BDIFF (G1, G2, G4) ;
- la surface boisée par département (G4) ;
- le lien entre les indices de Copernicus (grille de points) et les feux de la BDIFF (communes, sans coordonnées) : résolu au niveau du département (moyenne et maximum des points), pas plus fin (G5) ;
- Copernicus avant 2024, pour tester le seuil sur dix ans (G2, #46).

**Sources sans question, ou à interroger.**
- Interventions SIS : ne répond complètement à aucune question. Elle ne sert que de contexte pour G4. Une question qu'on n'a pas posée : quelle part de l'activité du SDIS 77 représentent les feux de végétation, pour juger si un dispositif renforcé pèse lourd dans le budget ?
- Copernicus : fichiers déposés et vérifiés (2024-2026). Seule source des indices détaillés (G5) et seul indice disponible toute l'année et sur plusieurs années (G2, décision 008).
- Sources du défi non ouvertes, qui pourraient combler des manques : BD Forêt et Admin Express (massifs, communes, G1 ; Admin Express servirait aussi à relier la grille de Copernicus aux communes, G5), Corine Land Cover ou BD Forêt (surface boisée, G4).

## Divergences entre fiches (tranchées)

| Sujet | Décision |
|---|---|
| Deux fiches BDIFF (Iris et Aboubacrine) au même chemin | Fusionnées en une seule fiche, `docs/sources/fiche-bdiff.md` |
| Période vérifiée | 2016-2025 en Île-de-France, avec l'export de référence `Incendies_2016_2025.csv` |
| Licence | Licence Ouverte v2.0, d'après la fiche data.gouv.fr (les mentions légales du portail n'en parlent pas) |
| Lignes avant l'en-tête du CSV | 2 ou 3 selon l'export : le pipeline cherche la ligne qui commence par `Année;` |
