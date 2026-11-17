# Inventaire des sources

| Source | Explorée par | Pertinente pour nos questions ? | Ce que nous avons découvert |
|---|---|---|---|
| BDIFF (Base de Données sur les Incendies de Forêts en France) | Iris | Oui : Q1, Q2, Q4 ; Q3 partiellement | 251 feux dans le 77 (2016-2025), date au jour près, code INSEE ; 49 % des feux à Fontainebleau ; cause manquante pour 53 % des feux ; pas de coordonnées GPS ; licence non trouvée |

## Quelles questions de nos analyses n'ont encore aucune source ?

- Q3, partie « proximité des habitations ou des routes » : la BDIFF ne localise les feux qu'à la commune, sans coordonnées. Il faudrait une source avec la position des feux, plus une source sur les routes et le bâti (BD TOPO IGN).
- Q1, partie « massifs » : la BDIFF ne définit pas les massifs forestiers (piste : BD Forêt IGN).
- Q2 et Q4 : il manque l'historique quotidien de l'indice Météo des forêts, à croiser avec les dates de la BDIFF.

## Quelle source nous a surpris, et pourquoi ?

- BDIFF : la moitié des feux de Seine-et-Marne (123 sur 251) est concentrée sur une seule commune, Fontainebleau. Et la cause du feu est inconnue pour plus de la moitié des incendies (132 sur 251), alors que c'est un champ central pour comprendre les départs de feu.

## Quelle source semble utile mais inexploitable dans le temps du projet ?

- Aucune parmi celles que j'ai explorées : la BDIFF est légère (251 lignes pour le 77) et s'exporte librement. Seule limite : l'année en cours n'est pas diffusée (données jusqu'à N-1).
