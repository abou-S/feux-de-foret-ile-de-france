# Fiche source - Interventions réalisées par les services d'incendie et de secours

Explorée par : Aboubacrine Seck, le 17/11/2026.

Liens :
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours
- Fichier ouvert : `interventions2024.csv` (ressource « interventions-SIS-2024 »)

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Intérieur. Données collectées chaque année par la DGSCGC auprès des SDIS, de la BSPP (Paris et petite couronne) et du BMPM (Marseille) |
| Mode d'accès et format | Téléchargement direct sur data.gouv.fr, un CSV par année. Séparateur `;`, encodage ISO-8859-1 (Latin-1), fins de ligne Windows. Les séparateurs de milliers sont devenus des `?` (`1?189` pour 1 189) |
| Grain (une ligne = ?) | Un service d'incendie sur une année : un département, sauf la BSPP (une seule ligne pour 75, 92, 93 et 94) |
| Emprise géographique | France, métropole et DOM. En Île-de-France : 5 lignes (Paris/BSPP, 77, 78, 91, 95). Aucun détail par commune |
| Période réellement couverte | 2008 à 2024 d'après la liste des fichiers ; 2024 vérifiée dans le fichier |
| Date de dernière mise à jour affichée | 02/07/2026 |
| Fréquence de mise à jour | Annuelle, avec environ un an et demi de retard |
| Volumétrie | Fichier 2024 : 99 lignes × 71 colonnes, environ 30 Ko |
| Clés disponibles | `Année`, `Numéro` (code département, ou « BSPP », « BMPM ») : jointure possible seulement au grain département × année |
| Données personnelles | Aucune : comptages agrégés |
| Licence | Licence Ouverte (code « fr-lo ») |
| Questions servies | Aucune complètement. Contexte pour G4 seulement |

## Schéma de données (71 colonnes)

| Colonnes | Type | Exemple (77, 2024) | Remarque |
|---|---|---|---|
| `Année`, `Zone`, `Région`, `Numéro`, `Département`, `Catégorie A` | texte | 2024, Île-de-France, Île-de-France, 77, Seine-et-Marne, A | `Catégorie A` (A, B, C ou vide) n'est pas expliquée |
| 11 colonnes de feux : `Feux d'habitations-bureaux` … `Feux de végétations`, `Autres feux`, `Incendies` | entier | `Feux de végétations` = 225, `Incendies` = 4 735 | **`Feux de végétations`** est la seule colonne utile à notre sujet |
| Secours à personne (20 colonnes), accidents de circulation (6), risques technologiques (6), opérations diverses (17) | entier | — | hors sujet |
| `Total interventions` | entier | 106 665 | |

## Pourquoi elle n'est pas dans l'entrepôt

Elle ne donne ni le jour ni la commune : impossible de la croiser avec l'indice. Et « feux de végétations » n'est pas « feux de forêt » (décision 006). On ne la garde que comme ordre de grandeur : 225 feux de végétation dans le 77 en 2024, contre 10 feux de forêt du 77 dans la BDIFF la même année.
