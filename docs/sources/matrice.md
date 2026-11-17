# Matrice questions × sources (v0)

Dernière mise à jour : 2026-11-17

Degrés : **complet** / **partiel** / **absent** / **inconnu**. Chaque degré a sa raison, avec la rubrique de la fiche ou la colonne du fichier.

Base : les analyses d'Aboubacrine, Iris et Daryl, et les fiches d'identité de l'inventaire. Les sources du défi que personne n'a ouvertes ne sont pas dans la matrice (voir plus bas).

## Questions retenues

| N° | Question du groupe | Posée par |
|---|---|---|
| G1 | Les départs de feu en Seine-et-Marne sont-ils concentrés sur quelques communes ou massifs, et ces zones restent-elles les mêmes d'une année à l'autre ? | Aboubacrine Q1, Iris Q1, Daryl Q1 |
| G2 | Pour chaque niveau de la Météo des forêts, quelle part des jours a connu au moins un départ de feu dans le 77, et combien de jours par été le dispositif renforcé serait-il déclenché selon le seuil ? | Aboubacrine Q2, Iris Q2 |
| G3 | Quelle part des feux démarre les jours d'indice bas, et ces feux ont-ils des points communs (cause, lieu, période) ? | Iris Q3, Aboubacrine Q3 (partie « jours d'indice bas ») |
| G4 | À niveau d'indice égal, le 77 a-t-il plus ou moins de feux que les autres départements d'Île-de-France et que le reste de la France ? | Aboubacrine Q4, Iris Q4, Daryl Q4 |
| G5 | Quelles conditions météo (pluie, vent, température, sécheresse) sont associées aux départs de feu et aux plus gros incendies ? | Daryl Q2 |

Non retenues telles quelles :
- Daryl Q3 (« quel seuil et quelle répartition des moyens offrent le meilleur compromis ») : c'est la décision de la direction, pas une question analytique. Elle demande aussi un coût que aucune source ne donne. G2 et G4 en sont la partie qu'on peut mesurer.
- Aboubacrine Q3 (« indice par secteur du 77 ») : fondue dans G3, car l'indice n'existe pas sous le département (voir décision 003).

## Matrice

| Question | BDIFF | Interventions SIS | Météo des forêts | Copernicus (EMS) |
|---|---|---|---|---|
| G1 | **partiel** : commune de chaque feu (Code INSEE, Nom de la commune), surface (Surface parcourue (m2)), date. 2016-2025 vérifié pour le 77 (fiche Iris). Pas de massif ni de coordonnées. 2026 absente | **absent** : une ligne par département et par an (Département, Numéro) | **absent** : que le niveau de danger (niveau_j1, niveau_j2) | **absent** : grille latitude × longitude d'indices de danger, pas de feux (rubrique Grain) |
| G2 | **partiel** : jour du feu (Date de première alerte) et Département. Seulement des feux de forêt, 2026 absente | **absent** : aucune date au jour | **partiel** : un niveau par jour et département (date, num_dep, niveau_j1), le 77 y est. Seulement 2024-2026, et le 77 est au niveau 1 les 120 jours de 2024 | **inconnu** : indice quotidien annoncé depuis 1940 (rubrique Période), mais aucun fichier ouvert et mises à jour suspendues depuis le 16/11/2026 |
| G3 | **partiel** : cause (Nature), Code INSEE, date. Cause manquante pour 132 feux sur 251 (fiche Iris). Pas de coordonnées donc pas de proximité routes ou habitations | **absent** : pas de feu individuel | **partiel** : indice au département seulement (num_dep) | **inconnu** : non ouvert |
| G4 | **partiel** : France entière (Département), mais « nombre d'incendies inconnu » pour 75, 92, 93, 94 en 2025 et 2 à 3 feux dans le 78 et le 91. Pas de surface boisée | **partiel** : « Feux de végétations » par département et par an, mais aucune date, et une seule ligne pour la BSPP | **partiel** : 96 départements par jour (num_dep, niveau_j1). Le niveau dépend de la forêt de chaque département (présentation PDF), donc pas comparable tel quel | **inconnu** : couverture mondiale annoncée (rubrique Emprise), non ouvert |
| G5 | **absent** : aucune variable météo | **absent** : aucune variable météo | **partiel** : seulement le niveau de synthèse de 1 à 4, pas la pluie, le vent ni la température | **inconnu** : indices de danger quotidiens annoncés, non ouvert |

Aucune question n'a de source « complet ».

## Lecture dans les deux sens

**Questions sans source complète.** Toutes. Les manques qui reviennent :
- les massifs (G1) : aucune source ne localise les feux plus finement que la commune ;
- un historique de l'indice de plus de 3 saisons (G2, G4) ;
- les feux de 2026, la saison la plus utile, pas encore diffusée par la BDIFF (G1, G2, G4) ;
- la surface boisée par département (G4) ;
- les variables météo détaillées (G5).

**Sources sans question, ou à interroger.**
- Interventions SIS : ne répond complètement à aucune question. Elle ne sert que de contexte pour G4. Une question qu'on n'a pas posée : quelle part de l'activité du SDIS 77 représentent les feux de végétation, pour juger si un dispositif renforcé pèse lourd dans le budget ?
- Copernicus : « inconnu » partout. À vérifier avant de la garder, surtout s'il peut fournir un historique d'indice plus long que 2024.
- Sources du défi non ouvertes, qui pourraient combler des manques : BD Forêt et Admin Express (massifs, communes, G1), Corine Land Cover ou BD Forêt (surface boisée, G4), AROME et ARPEGE (variables météo, G5).

## Divergences entre fiches à trancher

| Sujet | Fiche d'Aboubacrine | Fiche d'Iris | À faire |
|---|---|---|---|
| Fichier | `docs/sources/fiche-bdiff.md` | `docs/sources/fiche-bdiff.md` (même chemin) | Deux fiches pour la même source, et un conflit de fusion assuré. Il faut en garder une seule |
| Période vérifiée | export France entière, 2025 seulement | export du 77, 2016-2025 | Pas contradictoires. Garder 2016-2025 pour le 77 |
| Licence | Licence Ouverte v2.0, d'après la fiche data.gouv.fr | non vérifiée | La fiche data.gouv.fr l'indique, mais pas les mentions légales du portail. À citer avec sa source |
| Lignes avant l'en-tête du CSV | 2 | 3 | Probablement liées aux critères du filtre. À vérifier, et lire les colonnes par leur nom |
