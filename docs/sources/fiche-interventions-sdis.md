# Fiche source - Interventions réalisées par les services d'incendie et de secours

Explorée par : Aboubacrine Seck, le 17/11/2026

Liens :
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours
- Fichier ouvert : `interventions2024.csv` (ressource « interventions-SIS-2024 »)

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Intérieur. Les données sont collectées tous les ans par la DGSCGC (Direction générale de la sécurité civile et de la gestion des crises) auprès des services d'incendie et de secours : les SDIS, la BSPP (Paris et petite couronne) et le BMPM (Marseille). |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct sur data.gouv.fr, un fichier CSV par année. Séparateur `;`, encodage ISO-8859-1 (Latin-1), fins de ligne Windows. Attention, les séparateurs de milliers sont devenus des `?` dans le fichier (par exemple `1?189` pour 1 189), il faudra les nettoyer avant de faire des calculs. |
| Grain (une ligne = ?) | Un service d'incendie et de secours sur une année. En pratique c'est un département, sauf la BSPP qui a une seule ligne pour Paris et la petite couronne. Les colonnes sont des nombres d'interventions par type (71 colonnes, dont « Feux de végétations », « Incendies », « Total interventions »). |
| Emprise géographique | France : métropole et DOM (jusqu'à Mayotte 976). En Île-de-France il n'y a que 5 lignes : Paris (BSPP, qui couvre 75, 92, 93 et 94), 77, 78, 91 et 95. Il n'y a pas de détail par commune. |
| Période réellement couverte par les données | D'après la liste des ressources : 2008 à 2024, un fichier par an. Dans le fichier ouvert, j'ai vérifié seulement l'année 2024. Les autres années ne sont pas vérifiées. Les fichiers 2010, 2011 et 2013 font environ 9 Ko au lieu de 30 Ko, donc leur structure est sûrement différente (non vérifiée). Le lien du fichier 2012 pointe vers un ancien stockage et sa taille n'est pas renseignée, je ne l'ai pas testé. La fiche ne remplit pas le champ « couverture temporelle ». |
| Date de dernière mise à jour affichée sur la fiche | 02/07/2026 (ajout du fichier 2024). |
| Fréquence de mise à jour | Annuelle d'après la fiche. En pratique le fichier d'une année arrive environ un an et demi plus tard (le fichier 2024 a été mis en ligne en juillet 2026). |
| Volumétrie | Fichier 2024 : 99 lignes et 71 colonnes, environ 30 Ko. Les autres années font environ 30 Ko chacune, sauf 2010, 2011 et 2013 (environ 9 Ko). C'est très léger. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Année, et la colonne « Numéro » qui contient le code du département (77, 78…), sauf pour la BSPP et le BMPM où elle contient « BSPP » / « BMPM ». Il y a aussi Zone, Région et Département (nom). On peut joindre au niveau département et année seulement. |
| Données personnelles | Non. Ce sont des comptages agrégés par département et par an. |
| Licence | « fr-lo » sur data.gouv.fr, c'est-à-dire la Licence Ouverte (Etalab). |
| Questions de votre analyse auxquelles elle pourrait répondre | Q4 en partie : on peut comparer le nombre de « Feux de végétations » par an du 77 avec les autres départements d'Île-de-France et la France. Par contre il n'y a pas de jour, donc impossible de comparer « à niveau d'indice égal ». Q1, Q2 et Q3 : non. Il n'y a ni commune, ni date au jour, donc on ne peut pas croiser avec la Météo des forêts. Cette source peut quand même servir de contexte, par exemple pour savoir quelle part de l'activité du SDIS 77 représentent les feux de végétation. |

## Ce que j'ai remarqué en ouvrant le fichier

- « Feux de végétations », ce n'est pas « feux de forêt ». En 2024, la Seine-et-Marne compte 225 feux de végétation dans ce fichier. Ce chiffre comprend sûrement des feux de champs, de broussailles, de bords de route… Il ne se compare pas directement aux feux de forêt de la BDIFF. À mettre dans le glossaire.
- Chiffres 2024 en Île-de-France (feux de végétation) : 77 = 225, Paris/BSPP = 223, 91 = 186, 78 = 165, 95 = 26. Le 77 est le plus haut de la région, mais il faudrait rapporter ces chiffres à la surface de végétation pour comparer.
- Pour le 77 en 2024, il y a 106 665 interventions au total, dont 4 735 incendies. Les feux de végétation sont une toute petite part de l'activité.
- Une colonne « Catégorie A » vaut A, B, C ou vide. Elle n'est pas expliquée dans la fiche (sûrement la catégorie du SDIS selon sa taille, non vérifié).
- Comme la BSPP regroupe 4 départements sur une seule ligne, il est impossible d'avoir un chiffre pour le 92, le 93 ou le 94 séparément.
