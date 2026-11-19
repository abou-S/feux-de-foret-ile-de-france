# Fiches indicateurs

Une fiche par objectif (voir `kpi/objectifs.md`). Chacun remplit **sa** fiche sur sa propre branche, sans toucher aux autres sections. La section « Jeu d'indicateurs v0 » est remplie en groupe, à la mise en commun.

---
## Fiche G1 — Concentration géographique des feux — Iris

Indicateur : **part des départs de feu partis dans la zone couverte**.

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | Question G1 : les départs de feu en Seine-et-Marne sont-ils concentrés sur quelques communes ou massifs, et ces zones restent-elles les mêmes d'une année à l'autre ? Objectif : d'ici la fin de la saison 2027, faire passer de [a %] à [b %] la part des départs de feu du 77 qui partent dans une commune couverte par une patrouille ou un point de guet, sans couvrir plus de [k] communes |
| Formule : numérateur | Nombre de départs de feu du 77 dont le Code INSEE appartient à la zone couverte (les k communes retenues), sur la période de mesure |
| Formule : dénominateur | Nombre total de départs de feu du 77 sur la même période |
| Unité | % des départs de feu |
| Paramètres | k, le nombre de communes couvertes (1, 3, 5 ou 10 ; valeur retenue : 3). Fixés d'avance : la règle de choix (les k communes qui ont eu le plus de feux sur la période de sélection), les périodes (sélection sur 2016-2023, mesure sur 2024-2025), la pondération (chaque feu compte pour 1 ; variante : pondération par la Surface parcourue) |
| Périmètre, période, granularité, fréquence | Seine-et-Marne. 2016-2025 (sélection 2016-2023, mesure 2024-2025). Un feu. Une fois par saison, après la diffusion de la BDIFF (N-1) |
| Source et champs | BDIFF, export CSV du portail, critères Département = 77, du 01/01/2016 au 31/12/2025 (profil : `docs/qualite/rapport-bdiff.md`) : `Code INSEE`, `Nom de la commune`, `Surface parcourue (m2)`, `Année`, `Numéro` |
| Lignes utilisables | 251 / 251 (100 %) : Code INSEE, Date de première alerte et Surface parcourue remplis partout, aucun doublon Année + Numéro (règles R1 et R2 réussies). Période de mesure 2024-2025 : 65 feux (10 en 2024, 55 en 2025) |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Taux élevé et stable d'une année à l'autre : prépositionner patrouilles et guet sur ces k communes. Taux faible ou communes qui changent chaque année : préférer des moyens mobiles à des moyens fixes |
| Propriétaire | Calcul : Iris. Relecture : [responsable qualité et conformité] |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Commune couverte par une patrouille ou un point de guet » | Les k communes qui ont eu le plus de feux par le passé | La liste réelle du SDIS n'est pas connue (à demander) ; le proxy suppose que les feux futurs partent au même endroit | Surestime la part atteignable si les zones changent d'une année à l'autre |
| « Zone surveillée » | La commune entière | La commune de Fontainebleau contient une grande partie de la forêt : couvrir la commune ne dit pas quelle partie du massif est surveillée | Surestime la couverture réelle |
| « Massif » | La commune | La BDIFF n'a ni coordonnées ni notion de massif : un massif à cheval sur plusieurs communes est découpé | Sens inconnu |
| « Importance d'un feu » (variante pondérée) | `Surface parcourue (m2)` | 194 surfaces sur 251 sont estimées, pas mesurées (77 %) | Ordre de grandeur seulement |

### Changer un paramètre

On fait passer k de 3 à 5. Sur 2016-2025, avec sélection et mesure sur la même période : k = 3 (Fontainebleau, Nemours, Noisy-sur-École) donne 147 feux sur 251, soit **58,6 %** ; k = 5 (+ Arbonne-la-Forêt, Le Vaudoué) donne 162 feux sur 251, soit **64,5 %**.

**Ce qui change :**
- **Le numérateur et le taux :** + 15 feux, + 6 points.
- **Le coût :** deux zones de plus à couvrir par des patrouilles ou du guet.
- **La décision :** le gain par commune ajoutée diminue. Fontainebleau apporte 49 points à elle seule, les deux communes suivantes moins de 10 à elles deux, puis chaque commune ajoutée 2 à 3 points. Au-delà de k = 3, chaque commune coûte autant pour un gain faible : c'est un argument pour rester à 3 et redéployer le reste du budget vers le dispositif renforcé (G2).

**Ce qui ne change pas :** la formule, l'unité, le dénominateur (251 feux), la source et les champs, le grain, les proxys.

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : il répond directement au premier arbitrage de la commande, « où faut-il concentrer nos moyens » |
| Accepted | À confirmer avec le SDIS, qui doit fournir la liste des communes couvertes aujourd'hui et le plafond k fixé par le budget |
| Credible | Oui si k et les périodes de sélection et de mesure sont écrits dans la fiche avant le calcul : un taux élevé veut dire que peu de communes concentrent les départs de feu |
| Easy | Oui pour le calcul : une seule source, des champs remplis à 100 %, quelques lignes de code. Non pour le suivi de 2027 : la BDIFF ne publie qu'avec un an de retard |
| Robust | Moyen : il peut être gonflé en choisissant les communes après avoir vu les résultats. Voir garde-fous ci-dessous |

### Détournement, garde-fou, risque résiduel

- **Détournement :** celui qui calcule choisit les k communes sur la même période que celle où il mesure le taux. Ce sont par construction celles qui ont eu le plus de feux : le taux paraît excellent sans rien prouver pour 2027. Même effet en retenant seulement les saisons record (62 feux en 2020, 55 en 2025).
- **Garde-fou :** une **règle fixée à l'avance** (communes choisies sur 2016-2023, taux mesuré sur 2024-2025), et un contrepoids, la **part de la surface parcourue hors de la zone couverte**. Ce contrepoids mesure l'impact des feux et non leur nombre : si la zone capte beaucoup de petits feux mais que les gros partent ailleurs, il monte alors que l'indicateur reste haut.
- **Risque résiduel :** l'indicateur mesure où sont les moyens, pas ce qu'ils empêchent. Une commune couverte n'a pas moins de feux pour autant. Aucun des deux garde-fous ne voit les feux non saisis dans la BDIFF.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS. Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | La concentration venait de quelques saisons exceptionnelles (2020, 2025) : en 2027, les feux sont partis ailleurs et les moyens fixes étaient mal placés | Haute | Haute | Stabilité affichée à côté du taux : nombre d'années où chaque commune retenue est dans le top k. Moins de [5] années sur 10 : pas de moyens fixes sur cette commune |
| 2 | La zone captait beaucoup de petits feux, mais les gros sont partis dans d'autres communes | Moyenne | Haute | Contrepoids : part de la surface parcourue hors zone. Au-delà de [50 %], on revoit le choix des communes |
| 3 | « Couvrir Fontainebleau » ne disait pas où placer les moyens dans un massif aussi grand : ils ont été dispersés | Moyenne | Moyenne | Pas de garde-fou pour l'instant : il faudrait une localisation plus fine (coordonnées du SDIS, BD Forêt) |

Situation de référence : [a %] à mesurer (liste des communes couvertes à demander au SDIS). Taux hors échantillon 2024-2025 pour k = 3, part de la surface hors zone et stabilité : [à mesurer], avec le script de calcul.

---

## Fiche G2 — Seuil de déclenchement — Aboubacrine

Indicateur : **taux de jours d'alerte sans feu**.

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | Question G2 : pour chaque niveau de la Météo des forêts, quelle part des jours a eu au moins un départ de feu dans le 77 ? Objectif : d'ici la fin de l'été 2027, faire passer de [a %] à [b %] la part des jours de niveau ≥ N où aucun feu ne part, sans augmenter la part des feux qui partent les jours de niveau < N |
| Formule : numérateur | Nombre de jours où le niveau prévu pour le 77 est ≥ N et où aucun départ de feu n'a eu lieu dans le 77 |
| Formule : dénominateur | Nombre de jours où le niveau prévu pour le 77 est ≥ N, sur la période couverte par l'indice |
| Unité | % de jours |
| Paramètres | N, le seuil (2, 3 ou 4). Fixés d'avance : l'échéance (`niveau_j1`, la prévision faite la veille pour le lendemain, puisque c'est la veille que le SDIS décide) et la définition d'un feu (une fiche BDIFF) |
| Périmètre, période, granularité, fréquence | Seine-et-Marne. Saisons de l'indice (juin à septembre) où l'indice et les feux existent tous les deux : 2024 et 2025. Un jour pour le 77. Calcul mensuel pendant la saison, bilan en fin de saison |
| Source et champs | Météo des forêts, archives data.gouv.fr (`mdf_2024.csv`, `mdf_2025.csv`) : `date`, `num_dep`, `niveau_j1`. BDIFF, export CSV du portail : `Date de première alerte`, `Département`. Jointure : département + jour |
| Lignes utilisables | Météo des forêts 77 : 120 / 120 en 2024, 120 / 120 en 2025. BDIFF 77 2025 : 55 / 55 (aucune fiche marquée « données partielles »), dont 30 pendant la saison de l'indice. BDIFF 2024 : pas encore ouverte de mon côté, à reprendre de l'export d'Iris (2016-2025) |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Taux élevé : beaucoup de jours déclenchés pour rien, on relève N, à condition que le garde-fou (feux les jours < N) n'augmente pas. Taux faible : N peut rester, ou baisser si le budget le permet |
| Propriétaire | Calcul : Aboubacrine. Relecture : responsable qualité et conformité |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Aucun feu ne part » | Aucune fiche BDIFF ce jour-là dans le 77 | La BDIFF ne garde que les feux de forêt. Un petit feu de champ ou un départ éteint tout de suite peut ne pas y être | Surestime les jours sans feu, donc le taux |
| « Le jour concerné par le niveau » | `date` de publication + 1 jour pour `niveau_j1` | Déduit, pas écrit dans la documentation de Météo-France. Si c'est faux, tous les feux sont décalés d'un jour | Sens inconnu |
| « Le jour du feu » | `Date de première alerte` | Un feu qui dure plusieurs jours n'est rattaché qu'à son premier jour | Surestime un peu les jours sans feu |

### Changer un paramètre

On fait passer N de 3 (« élevé », le « danger élevé » de la commande) à 2 (« modéré »).

**Ce qui change :**
- **Le dénominateur :** les jours de niveau 2 sont ajoutés. Dans le 77, on passe de 1 jour (2025, et aucun en 2024) à 22 jours (2025, toujours aucun en 2024).
- **La lisibilité :** avec N = 3, un seul jour : le taux vaut 0 % ou 100 %, il ne veut rien dire. Avec N = 2, il devient calculable.
- **Le garde-fou :** avec N = 3, tous les feux des jours de niveau 2 comptent comme « hors alerte ». Avec N = 2, beaucoup moins.
- **La décision :** avec N = 2, un taux élevé pousse à remonter à 3. Avec N = 3, on ne peut rien conclure, faute de jours.
- **Le coût :** N = 2 déclenche le dispositif beaucoup plus souvent.

**Ce qui ne change pas :** la formule, l'unité, la source et les champs, le grain (un jour pour le 77), la période, la définition d'un feu.

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : il mesure directement ce que l'objectif veut faire baisser, les jours où le dispositif est déclenché pour rien |
| Accepted | À confirmer avec le SDIS : la définition d'un feu (une fiche BDIFF = un feu de forêt) et la valeur de N. Les termes « jour avec feu » et « niveau de danger » sont encore « à vérifier » dans le glossaire |
| Credible | Oui si N, l'échéance et la définition d'un feu sont écrits dans la fiche avant le calcul. Deux personnes liront alors la même chose : un taux élevé veut dire beaucoup d'alertes sans feu |
| Easy | Oui pour le calcul : deux CSV publics et une jointure par jour. Non pour le suivi de 2027 : la BDIFF ne publie qu'avec un an de retard, il faudra les relevés du SDIS |
| Robust | Faible tel quel : très peu de jours de niveau élevé dans le 77, et il peut être détourné en changeant N. Voir garde-fous ci-dessous |

### Détournement, garde-fou, risque résiduel

- **Détournement :** celui qui fixe le seuil monte N à 4. Il ne reste que les jours les plus secs, où il y a plus souvent un feu : le taux baisse et l'objectif semble atteint. En réalité, le dispositif n'est presque plus déclenché, et les feux partent sans lui.
- **Garde-fou :** le **taux de feux partis les jours de niveau < N** (nombre de feux un jour de niveau < N / nombre de feux pendant la saison de l'indice). Il compte des feux, pas des jours : il monte justement quand on monte N. C'est la condition de notre objectif. On affiche aussi le **nombre de jours de niveau ≥ N** à côté du taux, avec un **seuil plancher** : sous [k] jours (k à fixer), on ne lit pas le taux.
- **Risque résiduel :** un jour d'alerte sans feu n'est pas forcément une fausse alerte. Les patrouilles et le guet ont pu empêcher un feu. Aucun des deux garde-fous ne le voit : un dispositif efficace donne l'air d'un mauvais seuil.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS. Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | Le seuil a été fixé sur trop peu de jours (2 saisons, 1 seul jour de niveau 3 dans le 77) : le résultat tenait au hasard d'un été | Haute | Haute | Seuil plancher de jours, volume affiché à côté du taux, recalcul à chaque saison |
| 2 | Le dispositif a empêché des feux, ses jours sont passés pour de fausses alertes, et on a relevé N à tort | Moyenne | Haute | Contrôle par échantillon : pour quelques jours d'alerte sans feu, demander au SDIS si une patrouille est intervenue |
| 3 | Le niveau a été rattaché au mauvais jour (décalage d'un jour entre la publication et le feu) | Moyenne | Moyenne | Pas de garde-fou pour l'instant : à confirmer auprès de Météo-France |

---

## Fiche G3 — Feux des jours d'indice bas — Harold

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---
## Fiche G4 — Comparaison avec les autres départements — Iris

Indicateur : **écart de la part des jours d'alerte avec feu, 77 contre autres départements d'Île-de-France**.

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | Question G4 : à niveau d'indice égal, le 77 a-t-il plus ou moins de feux que les autres départements d'Île-de-France et que le reste de la France ? Objectif : avant le début de la saison 2027, retenir pour le 77 un seuil dont la part des jours d'alerte avec feu est au moins égale à [x %], la valeur des autres départements d'Île-de-France au même niveau, mesurée sur 2024 et 2025 |
| Formule : numérateur | Pour un département : nombre de jours où le niveau prévu est ≥ N **et** où au moins un départ de feu est enregistré dans ce département |
| Formule : dénominateur | Pour le même département : nombre de jours où le niveau prévu est ≥ N, sur la période couverte par l'indice |
| Unité | % de jours ; indicateur suivi : écart taux(77) − taux(autres), en points |
| Paramètres | N, le seuil (2, 3 ou 4 ; valeur retenue : 2, faute de jours de niveau 3). Fixés d'avance : le groupe de comparaison (78, 91, 95 regroupés ; 75, 92, 93, 94 exclus, sans aucune ligne dans la BDIFF), l'échéance (`niveau_j1`, prévision de la veille), le jour du feu (`Date de première alerte`), la définition d'un feu (une fiche BDIFF) |
| Périmètre, période, granularité, fréquence | 77, 78, 91, 95. Saisons de l'indice (juin à septembre) 2024 et 2025. Un département pour un jour. Une fois par saison |
| Source et champs | BDIFF, export CSV du portail, Île-de-France, 2016-2025 : `Département`, `Date de première alerte`. Météo des forêts, archives data.gouv.fr (`mdf_2024.csv`, `mdf_2025.csv`) : `date`, `num_dep`, `niveau_j1`. Jointure : département + jour (`docs/analyse/fusion_bdiff.py`, sorties `jours_dep.csv` et `feux_niveau.csv`) |
| Lignes utilisables | Feux 2024-2025 : 77 : 65 · 78 : 3 · 91 : 3 · 95 : 0. Avec un niveau (juin-septembre) : 77 : 36 · 78 : 2 · 91 : 1 · 95 : 0. Les 29 feux du 77 sans niveau sont hors saison (22 en avril-mai 2025). Jours de niveau ≥ 2 dans le 77 : 22 en 2025, 0 en 2024 (fiche G2) ; dans le 78, le 91 et le 95 : [à mesurer dans `jours_dep.csv`] |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Écart positif : l'indice annonce au moins aussi bien les feux dans le 77 qu'ailleurs, le seuil peut être aligné sur celui des voisins. Écart négatif : l'indice déclenche plus pour rien dans le 77, un seuil propre au 77 se justifie. Sous le seuil plancher : pas de comparaison, le seuil du 77 se fixe avec G2 seul |
| Propriétaire | Calcul : Iris. Relecture : [responsable qualité et conformité] |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Jour avec départ de feu » | Au moins une fiche BDIFF ce jour-là dans le département | Les feux non saisis manquent : le 78 et le 95 sont presque vides alors qu'ils sont boisés (rapport de qualité, règle R3) | Sous-estime le taux des autres départements, donc [x %] est trop bas et l'objectif trop facile à atteindre |
| « Départ de feu » | Feu de forêt enregistré dans la BDIFF | Les autres feux de végétation (cultures, friches) n'y sont pas | Sous-estime tous les taux |
| « Niveau comparable entre départements » | Même valeur de `niveau_j1` | Le niveau tient compte de la forêt de chaque département (présentation de Météo-France, citée dans la matrice) : un même niveau ne désigne pas le même danger partout | Sens inconnu |
| « Jours couverts » | Juin à septembre seulement | 29 feux du 77 sur 65 (45 %) en 2024-2025 n'ont aucun niveau | Le taux ne décrit que l'été |

### Résultats

Feux joints à un niveau, 2024-2025 :

| Département | Niveau 1 | Niveau 2 | Niveau 3 ou 4 | Total |
|---|---|---|---|---|
| 77 | 26 | 10 | 0 | 36 |
| 78 | 1 | 1 | 0 | 2 |
| 91 | 0 | 1 | 0 | 1 |
| 95 | 0 | 0 | 0 | 0 |

- **77, N = 2 :** 6 jours avec feu sur 22 jours de niveau ≥ 2 en 2025, soit **27 %** (2024 : aucun jour de niveau ≥ 2).
- **Autres départements, N = 2 :** 2 jours avec feu sur [à mesurer] jours de niveau ≥ 2.

**Verdict :** l'hypothèse G4 **ne peut pas être tranchée**. Les autres départements d'Île-de-France ne comptent que 3 feux avec un niveau en deux saisons, bien sous le seuil plancher : leur taux n'est pas interprétable. **Proposition au groupe :** remplacer le groupe de comparaison par la France entière (export national d'Aboubacrine), ou passer G4 en indicateur de contexte.

**Constat associé :** 72 % des feux d'été du 77 (26 sur 36) sont partis un jour de niveau 1, et aucun un jour de niveau 3 ou 4.

### Changer un paramètre

On fait passer N de 2 à 3.

**Ce qui change :**
- **Le dénominateur :** dans le 77, de 22 jours à 1 seul jour (2025), et toujours aucun en 2024.
- **Le taux :** il devient 0 % (aucun feu ce jour-là), une valeur qui ne veut rien dire avec un seul jour.
- **La comparaison :** aucun feu des autres départements n'est parti un jour de niveau 3 : leur numérateur vaut 0, la comparaison disparaît.
- **La décision :** avec N = 3, G4 ne peut plus rien éclairer ; avec N = 2, il peut au moins décrire le 77.

**Ce qui ne change pas :** la formule, l'unité, les sources et les champs, le grain, le groupe de comparaison, les proxys.

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : il répond à la demande de la direction de savoir « comment l'indice se comporte dans notre département et dans les autres départements de la région » |
| Accepted | À confirmer avec le SDIS : la définition d'un feu (une fiche BDIFF) et le groupe de comparaison. « Jour avec feu » et « niveau de danger » sont encore « à vérifier » dans le glossaire |
| Credible | Non en l'état : avec 3 feux chez les voisins, deux personnes peuvent tirer des conclusions opposées du même chiffre |
| Easy | Oui pour le calcul : deux sources publiques et une jointure par département et par jour, déjà écrite. Non pour 2027 : la BDIFF publie avec un an de retard |
| Robust | Faible : il dépend du choix de N et de la sous-saisie des feux chez les voisins. Voir garde-fous ci-dessous |

### Détournement, garde-fou, risque résiduel

- **Détournement :** celui qui fixe le seuil choisit un N très haut dans le 77. Il ne reste que quelques jours de danger extrême, souvent accompagnés d'un feu : le taux du 77 monte et dépasse celui des voisins, alors que la plupart des feux partent hors alerte (aujourd'hui, 72 % partent au niveau 1).
- **Garde-fou :** la **part des feux du 77 partis un jour de niveau < N** (feux partis hors alerte / feux pendant la saison de l'indice). Il compte des feux, pas des jours : il monte quand on relève N. On affiche aussi le **volume** à côté du taux (nombre de feux et de jours d'alerte par département), avec un **seuil plancher** : sous [10] feux ou [20] jours d'alerte dans un département, son taux n'est pas lu.
- **Risque résiduel :** un département sans feu enregistré n'est pas forcément un département sans feu : la BDIFF peut ne pas avoir été remplie. Aucun garde-fou ne distingue une absence de feu d'une absence de saisie.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS. Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | La valeur des voisins reposait sur une poignée de feux (3 en deux saisons) : [x %] n'était que du hasard, et le seuil du 77 a été calé dessus | Haute | Haute | Seuil plancher de volume : sous [10] feux ou [20] jours d'alerte par département, pas de comparaison ; recours à la France entière |
| 2 | Les feux des voisins étaient sous-saisis dans la BDIFF : [x %] était trop bas, et le seuil du 77 a été jugé bon à tort | Haute | Moyenne | Réconciliation des totaux : feux BDIFF par département et par an comparés aux « feux de végétation » de la source Interventions SIS ; un écart de plus de [50 %] exclut le département |
| 3 | Un même niveau ne désignait pas le même danger dans le 77 et chez les voisins : on a copié un seuil inadapté | Moyenne | Moyenne | Pas de garde-fou pour l'instant : à confirmer dans la documentation de Météo-France |

Situation de référence : [x %] à mesurer, mais non interprétable sur l'Île-de-France en l'état (voir verdict).

---

## Fiche G5 — Indices météo détaillés (Copernicus) — Daryl

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---

## Jeu d'indicateurs v0 (groupe)

| Rôle | Indicateur | Objectif | Raison |
|---|---|---|---|
| KPI principal | | | |
| KPI secondaire | | | |
| Garde-fou | | | |
| Contexte | | | |
| Écarté | | | |
