# Les données manquantes

Dernière mise à jour : 2026-11-20

Ce qu'il nous faudrait pour répondre complètement aux questions (`docs/sources/matrice.md`), et qu'on ne peut pas utiliser. Pour chaque manque : pourquoi, et ce qu'on en a conclu (décision du journal quand il y en a une).

## Données qui manquent

| Donnée | Questions | Pourquoi on ne l'a pas | Ce qu'on en conclut |
|---|---|---|---|
| Les massifs forestiers où partent les feux | G1 | La BDIFF localise les feux à la commune, sans coordonnées. BD Forêt n'a pas été ouverte | On mesure la concentration par commune (décision 001). La concentration par massif est sans doute plus forte encore |
| Les feux de 2026 | toutes | La BDIFF ne publie une année que l'année suivante | Demande au SDIS 77 de ses propres relevés (décision 002). Sans eux, on ne croise que 2024 et 2025 |
| Le niveau de la Météo des forêts avant 2024 | G2, G4 | Le dispositif n'est archivé que depuis 2024 (2023 manque) | Le seuil sur la Météo des forêts repose sur 2 saisons. On ajoute le FWI de Copernicus, disponible sur plusieurs années (décision 008) |
| Le FWI Copernicus de 2016 à 2023 | G2 | Pas encore téléchargé (fichier complet de plus de 1 Go) | Tâche #46 : extrait Île-de-France, pour tester le seuil sur dix ans |
| Les feux de Paris et de la petite couronne (75, 92, 93, 94) | G4 | La BSPP n'alimente pas la BDIFF (« nombre d'incendies inconnu ») | Ces départements restent « inconnus », jamais 0 (décision 007) |
| Les feux du reste de la France | G4 | Notre export ne couvre que l'Île-de-France | Choix du groupe de rester sur la région (décision 007) ; la partie « territoire national » de la commande reste sans réponse |
| La surface boisée par département | G4 | BD Forêt ou Corine Land Cover n'ont pas été ouverts | La comparaison entre départements n'est pas rapportée à leur forêt (décision 004) |
| Les feux de végétation hors forêt (champs, haies) | toutes | La BDIFF ne garde que les feux de forêt ; les statistiques SIS n'ont ni jour ni commune | Hors périmètre : un départ de feu = un feu de forêt (décision 006) |
| Le découpage du 77 en secteurs de centres de secours | G3 | Aucune source ouverte | Pas de seuil par secteur (décision 003) |
| La cause de plus de la moitié des feux | G3 | Le champ `Nature` est vide pour 166 feux sur 291 | L'analyse des causes porte sur 125 feux ; c'est une limite à afficher |
| La position exacte des feux (routes, habitations) | G3 | Pas de coordonnées dans la BDIFF | Question écartée |
| Le seuil actuel et le budget du SDIS | G2 | Absents de la commande | Questions à poser au SDIS. En attendant, le tableau de bord propose un « menu par budget » |
| Les indicateurs opérationnels que Météo-France envoie aux SDIS | G2 | Non publics ; la Météo des forêts « n'est pas destinée aux SDIS » | À demander au SDIS : si c'est cet indice qu'utilisent ses chefs de centre, le seuil doit porter dessus |

## Source écartée

**Interventions des services d'incendie (ministère de l'Intérieur)** : une ligne par département et par an, sans jour ni commune, et des « feux de végétations » qui ne sont pas des feux de forêt. Elle ne peut se croiser avec aucun indice : elle ne sert qu'à donner un ordre de grandeur (225 feux de végétation dans le 77 en 2024, contre 10 feux de forêt dans la BDIFF). Elle n'est pas chargée dans l'entrepôt (minimisation).

## Ce qu'on en retient

- **Aucune question n'a de source complète.** Les réponses seront des tendances, avec leurs limites écrites, pas des certitudes.
- **Le manque le plus lourd est la durée** : deux saisons pour croiser l'indice et les feux. Le FWI de Copernicus sur dix ans et les relevés 2026 du SDIS sont les deux façons de le combler.
- **Deux réponses ne peuvent venir que du SDIS** : son seuil actuel et son budget en jours de dispositif renforcé.
- Le modèle de l'entrepôt (pipeline bronze, silver, gold) est construit pour accueillir ces données dès qu'elles arrivent : il suffit de les déposer dans `data/bronze/` et de relancer `python -m pipeline`.
