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
| Paramètres | k, le nombre de communes couvertes (1, 3 ou 5 ; valeur retenue : 3). Fixés d'avance : la règle de choix (les k communes qui ont eu le plus de feux sur la période de sélection), les périodes (sélection sur 2016-2023, mesure sur 2024-2025), la pondération (chaque feu compte pour 1 ; variante : pondération par la Surface parcourue) |
| Périmètre, période, granularité, fréquence | Seine-et-Marne. 2016-2025 (sélection 2016-2023, mesure 2024-2025). Un feu. Une fois par saison, après la diffusion de la BDIFF (N-1) |
| Source et champs | BDIFF, export CSV du portail, critères Département = 77, du 01/01/2016 au 31/12/2025 (profil : `docs/qualite/rapport-bdiff.md`) : `Code INSEE`, `Nom de la commune`, `Surface parcourue (m2)`, `Année`, `Numéro` |
| Lignes utilisables | 251 / 251 (100 %) : Code INSEE, Date de première alerte et Surface parcourue remplis partout, aucun doublon Année + Numéro (règles R1 et R2 réussies). Période de mesure 2024-2025 : 65 feux (10 en 2024, 55 en 2025) |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Taux élevé et commune stable d'une année à l'autre : prépositionner patrouilles et guet sur cette commune. Taux faible ou communes qui changent chaque année : préférer des moyens mobiles à des moyens fixes |
| Propriétaire | Calcul : Iris. Relecture : [responsable qualité et conformité] |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Commune couverte par une patrouille ou un point de guet » | Les k communes qui ont eu le plus de feux par le passé | La liste réelle du SDIS n'est pas connue (à demander) ; le proxy suppose que les feux futurs partent au même endroit | Surestime la part atteignable si les zones changent d'une année à l'autre |
| « Zone surveillée » | La commune entière | La commune de Fontainebleau contient une grande partie de la forêt : couvrir la commune ne dit pas quelle partie du massif est surveillée | Surestime la couverture réelle |
| « Massif » | La commune | La BDIFF n'a ni coordonnées ni notion de massif : un massif à cheval sur plusieurs communes est découpé | Sens inconnu |
| « Importance d'un feu » (variante pondérée) | `Surface parcourue (m2)` | 194 surfaces sur 251 sont estimées, pas mesurées (77 %) | Ordre de grandeur seulement |

### Résultats

Communes choisies sur 2016-2023, taux mesuré sur 2024-2025 (65 feux) :

| k | Communes retenues | Part des feux dans la zone | Part de la surface hors zone (garde-fou) |
|---|---|---|---|
| 1 | Fontainebleau | 44,6 % | 15,0 % |
| **3** | Fontainebleau, Noisy-sur-École, Nemours | **50,8 %** | **12,9 %** |
| 5 | + Arbonne-la-Forêt, Larchant | 53,8 % | 7,9 % |

Stabilité (nombre d'années, de 2016 à 2025, où la commune est dans le top 3 annuel) : Fontainebleau 10 / 10, Nemours 4 / 10, Noisy-sur-École 3 / 10.

**Verdict :** l'hypothèse « les feux sont concentrés sur quelques communes, toujours les mêmes » est **confirmée pour Fontainebleau seulement**. Elle est stable chaque année et regroupe près de la moitié des feux, même hors échantillon. Nemours et Noisy-sur-École sont instables : sous le garde-fou de stabilité (5 années sur 10), elles ne justifient pas de moyens fixes.

### Changer un paramètre

On fait passer k de 3 à 5 (mesure hors échantillon 2024-2025).

**Ce qui change :**
- **Le numérateur et le taux :** de 50,8 % à 53,8 %, soit + 3 points pour 2 communes de plus.
- **Le garde-fou :** la surface hors zone baisse de 12,9 % à 7,9 %.
- **Le coût :** deux zones de plus à couvrir par des patrouilles ou du guet.
- **La décision :** Fontainebleau apporte 44,6 points à elle seule ; chaque commune ajoutée ensuite n'apporte que 1 à 3 points. Au-delà de k = 1, une commune de plus coûte autant pour un gain faible : c'est un argument pour placer les moyens fixes sur Fontainebleau et redéployer le reste du budget vers le dispositif renforcé (G2).

**Ce qui ne change pas :** la formule, l'unité, le dénominateur (65 feux sur la période de mesure), la source et les champs, le grain, les proxys.

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : il répond directement au premier arbitrage de la commande, « où faut-il concentrer nos moyens » |
| Accepted | À confirmer avec le SDIS, qui doit fournir la liste des communes couvertes aujourd'hui et le plafond k fixé par le budget |
| Credible | Oui : k et les périodes sont fixés avant le calcul, et le résultat hors échantillon (50,8 %) reste proche du résultat sur toute la période (58,6 %) |
| Easy | Oui pour le calcul : une seule source, des champs remplis à 100 %, quelques lignes de code. Non pour le suivi de 2027 : la BDIFF ne publie qu'avec un an de retard |
| Robust | Moyen : il peut être gonflé en choisissant les communes après avoir vu les résultats ; la règle hors échantillon et les deux garde-fous le protègent |

### Détournement, garde-fou, risque résiduel

- **Détournement :** celui qui calcule choisit les k communes sur la même période que celle où il mesure le taux. Ce sont par construction celles qui ont eu le plus de feux : le taux paraît meilleur (58,6 % sur 2016-2025 contre 50,8 % hors échantillon) sans rien prouver pour 2027. Même effet en retenant seulement les saisons record (62 feux en 2020, 55 en 2025).
- **Garde-fou :** une **règle fixée à l'avance** (communes choisies sur 2016-2023, taux mesuré sur 2024-2025), et un contrepoids, la **part de la surface parcourue hors de la zone couverte** (12,9 % pour k = 3). Ce contrepoids mesure l'impact des feux et non leur nombre : si la zone capte beaucoup de petits feux mais que les gros partent ailleurs, il monte alors que l'indicateur reste haut.
- **Risque résiduel :** l'indicateur mesure où sont les moyens, pas ce qu'ils empêchent. Une commune couverte n'a pas moins de feux pour autant. Aucun des deux garde-fous ne voit les feux non saisis dans la BDIFF.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS. Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | La concentration venait de quelques saisons exceptionnelles : en 2027, les feux sont partis ailleurs et les moyens fixes étaient mal placés | Haute | Haute | Stabilité affichée à côté du taux : nombre d'années où chaque commune retenue est dans le top 3. Moins de 5 années sur 10 : pas de moyens fixes sur cette commune (aujourd'hui, seule Fontainebleau passe : 10 / 10) |
| 2 | La zone captait beaucoup de petits feux, mais les gros sont partis dans d'autres communes | Moyenne | Haute | Contrepoids : part de la surface parcourue hors zone. Au-delà de 50 %, on revoit le choix des communes (aujourd'hui : 12,9 %) |
| 3 | « Couvrir Fontainebleau » ne disait pas où placer les moyens dans un massif aussi grand : ils ont été dispersés | Moyenne | Moyenne | Pas de garde-fou pour l'instant : il faudrait une localisation plus fine (coordonnées du SDIS, BD Forêt) |

Situation de référence : [a %] à mesurer (liste des communes couvertes aujourd'hui à demander au SDIS). Valeur du proxy, hors échantillon 2024-2025 : 50,8 % pour k = 3, 44,6 % pour Fontainebleau seule.

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

## Fiche G3 — Feux des jours d'indice bas — Harrold

Indicateur : **nombre de feux partis les jours d'indice bas, pour la cause, la commune ou la période identifiée**.

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | Question G3 : les feux du 77 qui partent les jours de niveau d'indice bas (niveau < [N]) ont-ils une cause, une commune ou une période en commun ? Objectif : d'ici la fin de la saison 2027, faire passer de [a] à [b] le nombre de ces feux pour la cause, la commune ou la période identifiée, sans déclencher le dispositif renforcé complet ces jours-là (`kpi/objectifs.md`) |
| Formule : numérateur | Nombre de fiches BDIFF du 77 dont la Date de première alerte tombe un jour de niveau < [N] (`niveau_j1`, département 77), dans la fenêtre où la Météo des forêts est publiée. Une fois un point commun confirmé (cause, commune ou période), on ne compte que les feux de ce sous-groupe |
| Formule : dénominateur | Pas de dénominateur au sens strict : l'objectif G3 est un effectif, pas une part (`kpi/objectifs.md`). Pour diagnostiquer l'indicateur, on garde en parallèle une part = numérateur (sans le filtre cause/commune/période) / nombre total de fiches BDIFF du 77 tombant dans la même fenêtre |
| Unité | Nombre de feux pour l'indicateur principal (effectif) ; % en indicateur de diagnostic |
| Paramètres | [N], le même seuil que G2 (`kpi/objectifs.md`), pas encore fixé. Testé ici à N = 2 (bas = niveau 1 seul) et comparé à N = 3 (niveau 1 et 2). Fenêtre de publication de la Météo des forêts (juin-septembre 2024 et 2025) |
| Périmètre, période, granularité, fréquence | Seine-et-Marne (77), pas de secteur (décision 003). 2024 et 2025, seules années où la Météo des forêts et la BDIFF se croisent (décision 002) ; 2024 sans variation de niveau (niveau 1 toute l'année), donc en pratique 2025 seul exploitable. Granularité : un feu, c'est-à-dire une fiche BDIFF (décision 006). Recalcul à chaque campagne BDIFF publiée |
| Source et champs | BDIFF, export CSV du portail, Département = 77, 2007-2025 (`docs/sources/fiche-bdiff.md`) : Date de première alerte, Code INSEE, Nom de la commune, Nature, Surface parcourue (m2). Météo des forêts, archives data.gouv.fr (`mdf_2024.csv`, `mdf_2025.csv`) : date, num_dep, niveau_j1 (`docs/sources/fiche-meteo-des-forets.md`). Jointure : département + jour, même convention que G2 (voir Proxy et biais) |
| Lignes utilisables | 36 / 36 (100 %) fiches BDIFF du 77 tombant dans la fenêtre de l'indice (6 en 2024, 30 en 2025) : Code INSEE et Date de première alerte toujours remplis, aucune marquée « données partielles ou non valides ». Cause (Nature) vide pour 17 des 30 feux de 2025 (57 %), et pour 10 des 20 feux de niveau 1 (50 %) : le sous-groupe « cause connue » parmi les feux de jours bas est petit (10 feux sur 2025) |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Si un point commun net ressort (cause, commune ou période), informe une mesure ciblée hors indice. Contribue aussi à fixer [N] avec G2, puisque cet effectif est exactement le garde-fou que G2 utilise (les feux des jours de niveau < N) |
| Propriétaire | Calcul : Harold. Relecture : [responsable qualité et conformité] |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Jour concerné par `niveau_j1` » | `date` de publication + 1 jour (même convention que G2) | Déduit, pas confirmé par la documentation Météo-France. Si c'est faux, tous les feux sont décalés d'un jour, ce qui change qui est compté « jour bas » | Sens inconnu |
| « Feu » | Une fiche BDIFF, donc un feu de forêt (décision 006) | Les feux de végétation hors forêt (champs, haies, bords de route) n'y sont pas, alors qu'ils peuvent aussi partir les jours d'indice bas | Sous-estime le phénomène |
| « Point commun » | Cause (`Nature`), commune (`Nom de la commune` / `Code INSEE`), période (mois, jour de semaine) des feux de niveau < N | La cause est inconnue pour la moitié des feux de niveau bas (10/20 en 2025) : le point commun « cause » ne peut être jugé que sur un sous-groupe très réduit | Peut manquer un point commun réel si les causes inconnues diffèrent des causes connues |
| « Indice bas » | `niveau_j1` au département (pas de découpage par secteur, décision 003) | Le niveau peut être bas pour tout le département alors qu'un secteur précis est sec | Sens inconnu |

### Changer un paramètre

On fait passer N de 2 (bas = niveau 1 seul) à 3 (bas = niveau 1 et 2). Sur la fenêtre de l'indice 2025 (30 feux) : N = 2 donne 20 feux sur 30, soit **66,7 %** ; N = 3 donne 30 feux sur 30, soit **100 %**.

**Ce qui change :**
- **Le numérateur et la part :** + 10 feux, + 33,3 points, jusqu'à devenir égal au dénominateur.
- **La lisibilité :** avec N = 3, plus aucun feu de la fenêtre n'est hors du groupe « bas » (aucun feu le seul jour de niveau 3 de 2025) : la part ne distingue plus rien, l'indicateur devient trivial.
- **Le lien avec G2 :** G2 utilise exactement ce même effectif comme garde-fou (feux des jours de niveau < N). Si N monte ici, le garde-fou de G2 s'élargit aussi et devient moins sélectif.

**Ce qui ne change pas :** la formule, l'unité, la source et les champs, le grain (un feu), la période, la définition d'un feu (décision 006).

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : répond directement à la remarque de la direction sur des feux combattus les jours où l'indice était au plus bas (`kpi/diagnostic.md`) |
| Accepted | À confirmer par le groupe : l'hypothèse G3 n'est pas encore tranchée, et [N] dépend du résultat de G2 |
| Credible | Fragile pour l'instant : un seul jour de niveau 3 observé en 2025 et aucune autre année croisable, donc toute lecture au-delà de « niveau 1 contre niveau 2 » reste limitée |
| Easy | Oui pour l'effectif global, une seule jointure département + jour ; plus coûteux pour les points communs, la cause étant inconnue pour la moitié des feux de niveau bas |
| Robust | Faible : repose sur une seule saison réellement exploitable (2025, 30 feux) et sur une convention de jointure (`niveau_j1` = J+1) non confirmée par la documentation |

### Détournement, garde-fou, risque résiduel

- **Détournement :** confondre « feux les jours d'indice bas » avec « feux que l'indice n'a pas annoncés » — ce n'est pas la même chose, et ça dépend du N choisi. On pourrait aussi gonfler le « point commun » en choisissant la cause, la commune ou la période après avoir vu les résultats (par exemple ne retenir que Fontainebleau, déjà la commune la plus touchée toutes conditions confondues).
- **Garde-fou :** toujours citer le N utilisé à côté du résultat. Comparer le sous-groupe « jours bas » à l'ensemble des feux de la même fenêtre : sur 2025, Fontainebleau fait 43 % de tous les feux de la fenêtre contre 40 % des feux de niveau 1 seul — pas de différence nette, donc pas un point commun propre aux jours bas, plutôt le reflet de la concentration déjà connue par G1.
- **Risque résiduel :** le très petit nombre de feux à niveau élevé (0 feu le seul jour de niveau 3 en 2025) empêche toute comparaison « bas » vs « haut » robuste. Une conclusion forte sur cette seule saison serait prématurée.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS (une mesure ciblée inutile, ou qui manque la vraie cause). Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | Le point commun trouvé (par exemple Fontainebleau) n'est que le reflet de la concentration générale des feux du 77 (G1), pas quelque chose de propre aux jours d'indice bas : la mesure ciblée ferait double emploi avec ce que G1 propose déjà | Haute | Haute | Comparer systématiquement le sous-groupe « jours bas » à l'ensemble de la fenêtre (déjà fait ci-dessus pour la commune) ; ne retenir un point commun que s'il diverge nettement de la répartition générale |
| 2 | La conclusion repose sur une seule saison exploitable (2025, 30 feux, dont 10 seulement à cause connue) : en 2026 ou 2027, avec plus de jours de niveau 2-3, le même calcul donnerait un point commun différent | Haute | Moyenne | Recalculer chaque année dès la campagne BDIFF suivante publiée ; ne pas figer la mesure ciblée avant d'avoir au moins deux saisons avec un vrai contraste de niveaux |
| 3 | Le décalage d'un jour (`niveau_j1` = J+1, convention déduite et non confirmée) a classé certains feux dans le mauvais niveau, faussant le partage « bas »/« haut » | Moyenne | Moyenne | Pas de garde-fou pour l'instant : à faire confirmer par Météo-France ou par Aboubacrine avant de publier un résultat définitif |

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
