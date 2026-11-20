# Fiche source - BDIFF (Base de Données sur les Incendies de Forêts en France)

Explorée par : Iris Pouth et Aboubacrine Seck (17/11/2026), fiches fusionnées le 20/11/2026.

Liens :
- Portail : https://bdiff.agriculture.gouv.fr/
- Consultation et export : https://bdiff.agriculture.gouv.fr/incendies
- Définitions : https://bdiff.agriculture.gouv.fr/aide/definitions
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/base-de-donnees-sur-les-incendies-de-forets-en-france-bdiff

Fichier de référence : `data/bronze/bdiff/Incendies_2016_2025.csv` (export du portail, zone de défense Île-de-France, du 01/01/2016 au 31/12/2025, feux de forêt). Provenance et empreinte : `data/bronze/SOURCES.md`.

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Agriculture et de la Souveraineté alimentaire. Application conçue et développée par l'IGN, alimentée par un réseau de contributeurs (SDIS, DDT(M), DRAAF) qui ont un compte. Depuis 2023, la BDIFF a fusionné avec Prométhée (l'ancien outil de l'aire méditerranéenne) |
| Mode d'accès et format | Portail web : on filtre (localisation, dates, heures, surfaces), puis « Télécharger : CSV ». On récupère un zip : un CSV UTF-8 (séparateur `;`), un PDF de définitions, un PDF de mentions légales. **2 ou 3 lignes d'information avant l'en-tête** selon l'export. Pas d'API documentée |
| Grain (une ligne = ?) | Un incendie de forêt (une « fiche incendie »), identifié par son année et son numéro |
| Emprise géographique | France entière, DOM compris. Notre export : Île-de-France. Localisation la plus fine : la commune de départ (code INSEE), sans coordonnées |
| Période réellement couverte | Le portail annonce « depuis 2006 », jusqu'à l'année précédente. Vérifié dans notre fichier : du 22/03/2016 au 05/11/2025. Les définitions des surfaces ont changé en 2023 |
| Date de dernière mise à jour affichée | Fiche data.gouv.fr : 13/12/2025. Le portail n'affiche pas de date de mise à jour des données |
| Fréquence de mise à jour | Annuelle : une campagne devient publique l'année suivante (2026 en 2027). Des campagnes passées peuvent être corrigées après coup |
| Volumétrie | Île-de-France 2016-2025 : 291 feux × 24 colonnes, dont 251 dans le 77. France 2025 seule : 2 541 feux |
| Clés disponibles | `Code INSEE` (commune), `Département`, `Date de première alerte` (jour, pour croiser avec la Météo des forêts et Copernicus), `Année` + `Numéro` (identifiant du feu) |
| Données personnelles | Pas de nom ni d'adresse. Les colonnes décès et bâtiments détruits existent mais sont à 0 ou vides pour tous nos feux d'Île-de-France (voir `docs/qualite/donnees-personnelles.md`) |
| Licence | Licence Ouverte v2.0, d'après la fiche data.gouv.fr. Les mentions légales du portail n'en parlent pas |
| Questions servies | G1 (où partent les feux), G2 et G3 (jour du feu, à croiser avec l'indice), G4 (comparaison des départements), G5 (côté « feux ») |

## Schéma de données (24 colonnes)

| Colonne | Type | Exemple | Remarque |
|---|---|---|---|
| `Année` | entier | 2016 | année de la campagne |
| `Numéro` | entier | 688 | numéro du feu dans l'année |
| `Département` | texte | 77 | |
| `Code INSEE` | texte | 77186 | commune de départ |
| `Nom de la commune` | texte | Fontainebleau | |
| `Date de première alerte` | date et heure | 2016-03-22 14:43:00 | heure où l'alerte arrive au CODIS, sans fuseau (heure française supposée) |
| `Surface parcourue (m2)` | entier | 60 | surface totale brûlée |
| `Surface forêt (m2)` | entier | 60 | |
| `Surface maquis garrigues (m2)` | entier | — | toujours vide en Île-de-France |
| `Autres surfaces naturelles hors forêt (m2)` | entier | 0 | |
| `Surfaces agricoles (m2)`, `Autres surfaces (m2)` | entier | 0 | vides pour 185 feux |
| `Surface autres terres boisées (m2)` et 3 colonnes `Surfaces non boisées…` | entier | 0 | modèle d'après 2023, vides pour 106 feux |
| `Précision des surfaces` | texte | Estimées | `Estimées` (232) ou `Mesurées` (59) |
| `Type de peuplement` | texte | — | toujours vide en Île-de-France |
| `Nature` | texte | Involontaire (particulier) | la cause ; vide pour 166 feux sur 291 |
| `Décès ou bâtiments touchés` | texte | Non | |
| `Nombre de décès`, `Nombre de bâtiments totalement détruits`, `… partiellement détruits` | entier | 0 | 0 ou vide pour tous nos feux |
| `Précision de la donnée` | texte | Données partielles ou non valides | renseignée seulement si la fiche est incomplète (7 feux) |

Colonnes reprises dans l'entrepôt (`feux_de_foret`) : `Année`, `Numéro`, `Département`, `Code INSEE`, `Nom de la commune`, `Date de première alerte`, `Surface parcourue (m2)`, `Précision des surfaces`, `Nature`. Les autres ne servent à aucune question (minimisation).

## Ce qu'on a découvert

- **Feux de forêt seulement** : un feu qui démarre ou se propage en forêt. Les feux de champs ou de haies n'y sont pas (décision 006).
- **Forte concentration** : 45 % des feux du 77 à Fontainebleau sur 2024-2025, 49 % sur 2016-2025.
- **Beaucoup de petits feux** : la moitié fait moins de 5 m² ; un seul feu (Fontainebleau, mai 2025, 3 ha) fait les trois quarts de la surface brûlée de 2024-2025.
- **Années très variables** : de 7 feux (2018) à 67 (2020) en Île-de-France.
- **BSPP** : aucune ligne pour 75, 92, 93, 94 ; le portail affiche « nombre d'incendies inconnu » (décision 007).
