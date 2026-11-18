# Objectifs

À partir du diagnostic (`kpi/diagnostic.md`) : pour chaque question, on part du niveau « Objectif » et on le précise en trois étapes. Les valeurs de départ inconnues sont notées « à mesurer » : on ne les invente pas.

## Trois formulations par question

| Question | Une action (pas un objectif) | Un objectif (pas SMART) | Un objectif SMART |
|---|---|---|---|
| G1 | Prépositionner patrouilles et guet sur les communes les plus touchées | Concentrer les moyens fixes sur les zones qui regroupent la plupart des départs de feu | D'ici la fin de la saison 2027, faire passer de [a %] à [b %] la part des départs de feu du 77 qui partent dans une commune couverte par une patrouille ou un point de guet, sans couvrir plus de [k] communes |
| G2 | Recalibrer le seuil de déclenchement du dispositif renforcé | Réduire les jours d'alerte sans feu, sans laisser passer plus de feux les jours d'indice bas | D'ici la fin de l'été 2027, faire passer de [a %] à [b %] la part des jours de niveau supérieur ou égal à [N] où aucun feu ne part dans le 77, sans augmenter la part des feux qui partent les jours de niveau inférieur à [N] |
| G3 | Mettre en place une surveillance ciblée les jours d'indice bas | Réduire les feux qui partent les jours d'indice bas | D'ici la fin de la saison 2027, faire passer de [a] à [b] le nombre de feux partis les jours de niveau inférieur à [N] dans le 77, pour la cause, les communes ou la période identifiées, sans déclencher le dispositif renforcé complet ces jours-là |
| G4 | Comparer le comportement de l'indice dans le 77 et dans les autres départements | Fixer pour le 77 un seuil adapté à la façon dont l'indice s'y comporte | Avant le début de la saison 2027, retenir pour le 77 un seuil dont la part des jours d'alerte avec feu est au moins égale à [x %], la valeur des autres départements d'Île-de-France au même niveau, mesurée sur 2024 et 2025 |
| G5 | Tester les indices détaillés de Copernicus (FWI, DC, DMC, FFMC) | Trouver un indice qui sépare mieux les jours avec feu des jours sans feu | Avant le 11 décembre 2026, trouver parmi FWI, DC, DMC et FFMC un indice dont la part des jours d'alerte avec feu dépasse de [x points] celle du niveau de la Météo des forêts, sur 2024 et 2025 dans le 77, avec le même nombre de jours d'alerte |

## Critère par critère

| Question | Spécifique | Mesurable | Atteignable | Réaliste | Temporel |
|---|---|---|---|---|---|
| G1 | Les départs de feu de forêt du 77, selon la commune où ils partent | Part de [a %] à [b %], calculée avec la commune de chaque feu (Code INSEE de la BDIFF) | [b %] fixé avec le SDIS une fois [a %] connu | Le plafond de [k] communes, lié au budget, empêche de tout couvrir | Fin de la saison 2027 |
| G2 | Les jours de niveau ≥ [N] dans le 77 où aucun feu ne part | Part de [a %] à [b %], en croisant le niveau et les feux jour par jour | [b %] fixé avec le SDIS une fois [a %] connu | La condition sur les feux des jours de niveau < [N] empêche de monter le seuil au maximum | Fin de l'été 2027 |
| G3 | Les feux des jours de niveau < [N] qui ont la cause, la commune ou la période identifiées | Nombre de [a] à [b] | [b] fixé une fois [a] connu, et seulement si l'hypothèse G3 est confirmée | Pas de dispositif complet ces jours-là : la mesure doit rester légère | Fin de la saison 2027 |
| G4 | La part des jours d'alerte avec feu dans le 77, comparée aux autres départements d'Île-de-France | Comparaison à [x %], au même niveau | Dépend du verdict de l'hypothèse G4 | Limité aux départements qui ont des feux (78, 91, 95) : pas de données de feux pour 75, 92, 93, 94 | Avant la saison 2027 |
| G5 | Les quatre indices de Copernicus, comparés au niveau de 1 à 4, dans le 77 | Écart de [x points], au même nombre de jours d'alerte | Seulement si Copernicus est exploitable dans le temps du projet | Le même nombre de jours d'alerte garde la contrainte de budget | Rendu du 11 décembre 2026 |

## Situation de référence

| Question | Valeur de départ | Pourquoi |
|---|---|---|
| G1 | [a %] : à mesurer | La liste des communes couvertes aujourd'hui par les patrouilles et le guet n'est pas connue, il faut la demander au SDIS |
| G2 | [a %] et [N] : à mesurer | Le seuil actuel n'est pas dans la commande. On ne peut croiser l'indice et les feux que sur 2024 et 2025 |
| G3 | [a] : à mesurer | Dépend de [N] et de ce que l'hypothèse G3 fera ressortir |
| G4 | [x %] : à mesurer | À calculer sur 2024 et 2025 pour les autres départements d'Île-de-France |
| G5 | [x points] : à mesurer | Aucun fichier Copernicus n'a encore été ouvert |

## Test de cohérence : peut-on atteindre l'objectif sans faire avancer la stratégie ?

| Question | Comment l'objectif pourrait être atteint sans servir la stratégie |
|---|---|
| G1 | Couvrir une commune ne veut pas dire mieux lutter : la part peut monter sans que les feux soient moins nombreux ni plus vite éteints. L'indicateur mesure où sont les moyens, pas ce qu'ils empêchent |
| G2 | Si le dispositif empêche un feu un jour d'alerte, ce jour compte comme une alerte sans feu. Un dispositif efficace donne donc l'air d'un mauvais seuil. Un été humide peut aussi changer la part sans aucune décision |
| G3 | Les feux peuvent baisser parce que l'été est humide, pas grâce à la surveillance. Et la cause est inconnue pour une grande partie des feux, donc le groupe ciblé peut être très petit |
| G4 | On peut atteindre la valeur des voisins en copiant leur seuil, alors que le niveau n'a pas le même sens d'un département à l'autre (il tient compte de la forêt de chacun) |
| G5 | Un indice peut sembler meilleur sur deux saisons par hasard. Et l'action proposée sort de la commande, qui ne parle que de la Météo des forêts |

## Limites

- **Les objectifs de 2027 ne pourront pas être vérifiés avec la BDIFF**, qui publie avec un an de retard (2027 en 2028). Il faudra les relevés du SDIS 77.
- **Les feux d'avril et mai échappent à G2, G3, G4 et G5.** La Météo des forêts n'est publiée qu'à partir de juin.
- **G3, G4 et G5 dépendent du verdict de leur hypothèse.** Si l'hypothèse est infirmée, l'objectif tombe.
