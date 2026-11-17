# Analyse de la commande - Aboubacrine Seck

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1. Quelle part des départs de feu et des surfaces brûlées en Seine-et-Marne se concentre dans les communes et massifs les plus touchés ?
2. Pour chaque niveau de la Météo des forêts, quelle est la part des jours où au moins un départ de feu a eu lieu dans le 77 ?
3. Dans chaque secteur du 77, combien de départs de feu ont lieu à chaque niveau de l'indice, et quelle part des feux démarre les jours où l'indice est au plus bas ?
4. À niveau d'indice égal, combien de départs de feu par jour (rapporté à la surface boisée) compte le 77, comparé aux autres départements d'Île-de-France et à la moyenne nationale ?

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| Feu de forêt | Un incendie qui brûle de la forêt (arbres, sous-bois) | Est-ce que les feux de broussailles, de champs ou de chaumes comptent ? À partir de quelle surface on parle de feu de forêt ? |
| Départ de feu | Le moment et l'endroit où un feu commence, même s'il est éteint tout de suite | Est-ce qu'un départ éteint en 5 minutes compte autant qu'un gros feu ? Est-ce la même chose qu'un « feu de forêt » dans les sources ? |
| Météo des forêts | L'indice de Météo-France qui donne le niveau de danger de feu de forêt chaque jour | Combien de niveaux il y a, comment il est calculé, à quelle échelle (département, zone plus petite ?) et depuis quand il existe sous cette forme |
| Danger élevé | Un des niveaux de la Météo des forêts | À quel niveau exact ça correspond ? Les chefs de centre parlent-ils tous du même niveau ? |
| Indice « au plus bas » | Le niveau le plus faible de la Météo des forêts | Est-ce que l'indice est publié tous les jours, ou seulement en été ? Un jour sans indice publié, c'est un niveau bas ou une donnée manquante ? |
| Dispositif renforcé | Les mesures en plus quand le risque est fort : patrouilles, guet, etc. | Qu'est-ce qu'il y a exactement dans le « etc. » ? Combien ça coûte par jour ? Est-ce qu'on peut le déclencher sur une partie du département seulement ? |
| Seuil actuel | Le niveau de l'indice à partir duquel le SDIS déclenche le dispositif aujourd'hui | On ne connaît pas ce seuil, il n'est pas dans la commande |
| Moyens (humains et financiers) | Les pompiers, les véhicules et le budget du SDIS | Est-ce qu'on parle aussi des moyens prêtés par les autres départements ou seulement ceux du 77 ? |
| Département | Le 77 (Seine-et-Marne) et les autres départements d'Île-de-France | Dans la région, Paris et la petite couronne (75, 92, 93, 94) ne sont pas gérés par un SDIS mais par la Brigade des sapeurs-pompiers de Paris. « Département » et « territoire d'un SDIS » ne sont donc pas pareils |
| Été / saison feux | La période où il y a le plus de feux, en gros juin à septembre | Les dates exactes de la saison feux pour le SDIS 77. Le mail parle aussi du printemps, donc la période est peut-être plus large |
| Chef de centre | Le responsable d'une caserne (centre d'incendie et de secours) | Combien de centres il y a dans le 77 et quel secteur chacun couvre, pour pouvoir découper le département |
| Guet | Surveillance de la forêt depuis un point haut pour repérer les fumées | Où sont les points de guet dans le 77 et est-ce qu'ils sont déjà en place |

## 3. Les besoins

La décision à éclairer, en une phrase :

Le SDIS 77 doit décider, avant l'été 2027, où il met ses moyens contre les feux de forêt et à partir de quel niveau de la Météo des forêts il déclenche le dispositif renforcé, sachant qu'il ne peut pas renforcer partout et tout le temps.

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
- Le seuil actuel de déclenchement : on ne sait pas à quel niveau le dispositif est déclenché aujourd'hui, donc on ne peut pas dire de combien il faut le changer.
- Le budget disponible et le coût d'une journée de dispositif renforcé : sans ça on ne peut pas savoir combien de jours de renfort le SDIS peut se payer.
- Ce que la direction appelle « feu de forêt » : seulement la forêt, ou aussi les feux de végétation (champs, broussailles) qui sont nombreux en Seine-et-Marne.
- L'échelle de décision : est-ce que le dispositif peut être déclenché par secteur ou seulement sur tout le département ? Ça change la question 3.
- La période : le mail parle de l'été mais la réponse doit aussi servir pour le printemps. Il faut confirmer les mois à étudier.
- L'hypothèse « autant de feux qu'en 2026, voire plus » : est-ce une prévision officielle ou une impression ? On ne doit pas partir de ça comme d'un fait.
- Pour la comparaison avec la région : la BSPP couvre Paris et la petite couronne, il faudra vérifier qu'on a des données comparables pour ces départements.

## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Liste de tous les départs de feu de végétation avec la date, la commune (ou les coordonnées), la surface brûlée et la cause si elle est connue. En plus, le découpage des secteurs des centres de secours et la carte des massifs forestiers | Un départ de feu | Au moins les 10 dernières années (pour ne pas juger sur une seule saison), en insistant sur 2022 et 2026 | Mise à jour annuelle, avec la saison 2026 complète avant le 11 décembre | Seine-et-Marne, au niveau de la commune ou plus fin |
| 2 | Le niveau de la Météo des forêts pour chaque jour, croisé avec le nombre de départs de feu le même jour | Un jour × un département (ou une zone de l'indice si elle est plus fine) | Les saisons feux depuis que l'indice existe sous sa forme actuelle, au moins 5 ans | Historique figé, mise à jour une fois par an suffit | Seine-et-Marne |
| 3 | Le niveau de l'indice par jour et par zone, et les départs de feu localisés par secteur (centre de secours ou massif) | Un jour × un secteur du 77 | Mêmes années que la question 2 | Mise à jour annuelle | Seine-et-Marne, découpée par secteur |
| 4 | Le niveau de l'indice par jour et le nombre de départs de feu par jour pour chaque département, avec la surface boisée de chaque département pour pouvoir comparer (un département avec plus de forêt aura forcément plus de feux) | Un jour × un département | Mêmes années que la question 2 | Mise à jour annuelle | Les 8 départements d'Île-de-France et toute la France métropolitaine |
