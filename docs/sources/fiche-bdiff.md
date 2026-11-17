# Fiche source : BDIFF (Base de Données sur les Incendies de Forêts en France)

Lien : https://bdiff.agriculture.gouv.fr/incendies
Explorée par : Iris Pouth Nadia — 17/11/2026
Fichier ouvert : Incendies.csv (extrait de incendies.zip), filtre Seine-et-Marne, 01/01/2016 – 31/12/2025

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Agriculture et de la Souveraineté alimentaire ; application BDIFF conçue et développée par l'IGN, alimentée par un réseau de contributeurs |
| Mode d'accès et format | Consultation web libre avec filtres (dates, département, code INSEE, rectangle sur carte) ; export .zip contenant un CSV (séparateur « ; », encodage UTF-8, 3 lignes de notes avant l'en-tête). Compte IGN requis uniquement pour renseigner des incendies |
| Grain (une ligne = ?) | Un incendie, identifié par l'année et son numéro, avec la date et l'heure de première alerte |
| Emprise géographique | France entière, DOM compris (carte du site). Export testé : Seine-et-Marne (77) |
| Période réellement couverte | Base : depuis 2006, jusqu'à l'année N-1 (page d'accueil BDIFF). Export testé : 2016-2025 (premier feu du 77 : 22/03/2016) |
| Date de dernière mise à jour affichée | Non vérifiée : aucune date de mise à jour affichée sur le site ni dans l'export |
| Fréquence de mise à jour | Saisie en continu par les contributeurs ; diffusion publique jusqu'à l'année N-1 (page d'accueil BDIFF) : l'année en cours n'est pas consultable |
| Volumétrie | 251 lignes × 24 colonnes pour le 77 sur 2016-2025 ; zip de 583 Ko |
| Clés disponibles | Code INSEE de la commune (jointure avec le COG, millésime non vérifié) ; département ; date de première alerte (jointure avec la Météo des forêts) ; Année + Numéro (identifiant du feu) |
| Données personnelles | Aucune : pas de nom, pas d'adresse, pas de coordonnées. Nombres de décès et de bâtiments détruits présents, en valeurs agrégées seulement |
| Licence | Non vérifiée : aucune licence indiquée dans les mentions légales ni dans l'aide du site BDIFF |
| Questions auxquelles elle pourrait répondre | Q1 : feux par commune et par année. Q2 et Q4 : dates au jour près, à croiser avec la Météo des forêts. Q3 en partie : cause (colonne « Nature »), commune, date |

## Colonnes disponibles (24)
Année, Numéro, Département, Code INSEE, Nom de la commune, Date de première alerte,
Surface parcourue (m2), 9 colonnes de surfaces par type de terrain (m2),
Précision des surfaces, Type de peuplement, Nature (cause),
Décès ou bâtiments touchés, Nombre de décès, Nombre de bâtiments totalement / partiellement détruits,
Précision de la donnée

## Qualité constatée (251 feux, Seine-et-Marne, 2016-2025)

| Constat | Chiffre | Impact |
|---|---|---|
| Cause (« Nature ») manquante | 132 / 251 (53 %) | Q3 limitée à 119 feux |
| Causes connues | Involontaire particulier 72, travaux 20, accidentelle 14, malveillance 13 | Utilisable pour Q3 |
| Surfaces estimées / mesurées | 194 estimées (77 %) / 57 mesurées | Surfaces peu fiables |
| Type de peuplement vide | 251 / 251 (100 %) | Colonne inutilisable |
| Surface maquis garrigues vide | 251 / 251 | Normal : pas de maquis en Île-de-France |
| Précision de la donnée vide | 246 / 251 (98 %) | Colonne inutilisable |
| Décès / bâtiments vides | 203 / 251 | Probablement « 0 » non saisi (non vérifié) |
| Colonnes clés complètes | Année, Numéro, Code INSEE, Commune, Date, Surface parcourue : 0 manquant | Jointures possibles |

## Ce que nous avons découvert
- Date de première alerte au jour et à la minute près : croisement jour par jour possible avec la Météo des forêts (Q2, Q4). À convertir avec pd.to_datetime (lue comme texte).
- Forte concentration : Fontainebleau = 123 feux sur 251 (49 %) ; les 3 premières communes = 59 % (Q1).
- Nombre de feux très variable selon les années : 7 (2018) à 62 (2020).
- L'été 2026 ne sera pas consultable avant 2027 (diffusion jusqu'à N-1).
- Pas de coordonnées GPS ni de notion de massif : Q3 (proximité des routes et des habitations) et la partie « massifs » de Q1 demandent une autre source (BD TOPO, BD Forêt).
- Surfaces en m² dans le CSV, en hectares sur le site.
- Licence non trouvée : à demander à l'IGN avant toute diffusion des résultats.
