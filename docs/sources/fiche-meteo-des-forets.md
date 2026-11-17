# Fiche source - Archives de la Météo des forêts

Explorée par : Aboubacrine Seck, le 17/11/2026

Liens :
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets
- Documentation de Météo-France (page Confluence citée dans la fiche) : https://confluence-meteofrance.atlassian.net/wiki/spaces/OpenDataMeteoFrance/pages/874741792/Donn+es+expertis+es
- API de Météo-France (citée dans le défi) : https://portail-api.meteofrance.fr/web/fr/api/DonneesPubliquesMeteoForets

Fichiers ouverts : `mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`, la présentation PDF de Météo-France et le GeoJSON des départements.

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Météo-France. Le dispositif s'appelle « Météo des forêts » et est diffusé au public depuis 2023 (d'après la présentation PDF). Il s'inscrit dans la stratégie nationale pilotée par la DGPR et la DGSCGC. |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct d'un fichier par année, au format CSV compressé en gzip (`mdf_AAAA.csv.gz`), hébergé sur un stockage de Météo-France. Il existe aussi une API sur le portail Météo-France (non vérifiée : je n'ai pas ouvert cette page, ni testé si un compte ou une clé est nécessaire). Attention, le format change selon l'année : les fichiers 2024 et 2025 utilisent `,` comme séparateur et la colonne `nom_dep` (2024) ou `dep_nom` (2025), le fichier 2026 utilise `;` et `nom_dep`. |
| Grain (une ligne = ?) | Un département, pour une prévision publiée un jour donné. Colonnes : `date` (horodatage de publication, par exemple `2025-06-03T14:50:06Z`), `num_dep`, `niveau_j1`, `niveau_j2`, nom du département. Il y a exactement 96 lignes par jour (96 départements de métropole et Corse). |
| Emprise géographique | France métropolitaine et Corse, 96 départements (la fiche indique « métropole »). Les DOM n'y sont pas. Les 8 départements d'Île-de-France sont tous présents, y compris le 75, le 92, le 93 et le 94. |
| Période réellement couverte par les données | Vérifiée dans les fichiers : 2024 = du 03/06/2024 au 30/09/2024 (120 jours), 2025 = du 03/06/2025 au 30/09/2025 (120 jours), 2026 = du 28/05/2026 au 05/10/2026 (131 jours). Il n'y a pas de jour manquant dans ces plages, mais rien en dehors de la saison : pas de donnée de janvier à mai (sauf fin mai 2026), ni d'octobre à décembre. La fiche data.gouv.fr annonce « à partir du 03/06/2024 ». Rien avant 2024, alors que le dispositif existe depuis 2023 : l'année 2023 n'est pas dans les archives. |
| Date de dernière mise à jour affichée sur la fiche | 05/10/2026 (ajout du fichier 2026). |
| Fréquence de mise à jour | Quotidienne d'après la fiche. En pratique, les fichiers 2024 et 2025 sont des archives fermées, et le fichier 2026 s'arrête au 05/10/2026, date de sa dernière mise à jour. Je n'ai pas vérifié s'il continue d'être alimenté. |
| Volumétrie | Très petite. 2024 : 11 520 lignes (450 Ko décompressé), 2025 : 11 520 lignes, 2026 : 12 576 lignes (480 Ko). Environ 35 000 lignes au total. |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `num_dep` (code du département, texte : `01`… `95`, `2A`, `2B`) et la date. Avec la BDIFF, qui a le département et la date d'alerte, on peut joindre par département + jour. Attention à la jointure : voir « Précautions » plus bas. |
| Données personnelles | Non. Ce sont des niveaux de danger par département et par jour. |
| Licence | « lov2 » sur data.gouv.fr, c'est-à-dire la Licence Ouverte v2.0. |
| Questions de votre analyse auxquelles elle pourrait répondre | Q2 (part des jours avec feu par niveau de l'indice) : oui, c'est la seule source de l'indice, mais elle ne couvre que 3 saisons (voir plus bas). Q3 (indice par secteur) : non, l'indice est à l'échelle du département, on ne peut pas descendre au secteur ou à la commune. Q4 (comparaison à niveau égal avec l'Île-de-France et la France) : oui, les 96 départements sont dedans, avec la réserve que le niveau n'est pas calculé de la même façon partout (voir plus bas). Q1 (concentration des feux par commune) : non, aucun lien avec cette question. |

## Les niveaux

D'après la présentation PDF de Météo-France, l'échelle a 4 niveaux : 1 = faible (vert), 2 = modéré (jaune), 3 = élevé (orange), 4 = très élevé (rouge). Le fichier contient bien les valeurs 1 à 4. Dans la commande, « danger élevé » correspondrait donc au niveau 3, mais la direction ne le précise pas : à vérifier.

## Ce que j'ai remarqué en ouvrant les fichiers

- **Seulement 3 saisons, et 2 seulement en commun avec la BDIFF.** La BDIFF publie les campagnes jusqu'à l'année précédente (donc pas 2026). On ne peut donc croiser que 2024 et 2025. Pour la question 2, c'est très court : j'avais prévu au moins 5 ans.
- **2024 est inutilisable pour le 77.** Cette année-là le 77 est au niveau 1 les 120 jours. Il n'y a aucun jour avec un niveau plus haut, donc on ne peut pas comparer les niveaux entre eux.
- **En 2025, le 77 a très peu de jours au-dessus du niveau 1** : 21 jours au niveau 2, 1 jour au niveau 3, aucun au niveau 4. Le niveau 3 n'a qu'un seul jour d'observation, ce qui est trop peu pour conclure.
- **2026 est très différent :** le 77 a 62 jours au niveau 2, 27 jours au niveau 3 et aucun au niveau 4. Mais la BDIFF 2026 n'est pas encore publiée, donc cette année ne peut pas être croisée avec les feux de forêt.
- **L'indice a fortement monté entre 2024, 2025 et 2026.** Pour le 77, la part des jours au niveau 1 passe de 100 % (2024) à 82 % (2025) puis à 32 % (2026). Soit l'été 2026 était très sec, soit la façon de calculer le niveau a changé (non vérifié). Cela va dans le sens de la commande, qui dit que l'indice annonce souvent un danger élevé.
- **Le 75, le 92, le 93 et le 94 ont les mêmes répartitions de niveaux** dans chaque année (par exemple en 2026 : 64 jours au niveau 1, 50 au niveau 2, 17 au niveau 3). La Météo des forêts les traite donc sans doute comme une seule zone. Je n'ai pas vérifié jour par jour.

## Précautions et points à vérifier

- **Le niveau n'est pas comparable d'un département à l'autre.** La présentation précise que le niveau tient compte, pour chaque département, de la surface de forêt et des zones sensibles aux feux. Un niveau 3 dans le 77 et un niveau 3 dans le Var ne veulent donc pas dire la même chose en termes de risque. Cela limite la question 4.
- **Le jour concerné n'est pas la colonne `date`.** La Météo des forêts est publiée chaque jour à 17 h, pour le lendemain et le surlendemain. L'horodatage du fichier est celui de la publication (environ 14 h 50 UTC, donc vers 16 h 50 en heure française en été). J'en déduis que `niveau_j1` vaut pour le lendemain de `date` et `niveau_j2` pour le surlendemain, mais la fiche ne le dit pas explicitement. Il faut donc le faire confirmer avant de joindre avec la BDIFF, sinon on risque un décalage d'un jour.
- **C'est une prévision, pas un constat.** Les niveaux sont prévus la veille. Pour juger si le seuil était bon, on ne sait pas si la valeur gardée dans l'archive est la prévision ou une version corrigée après coup (non vérifié).
- **Une seule valeur par jour.** Le fichier ne donne que le niveau, pas l'indice numérique ni les mesures météo (vent, humidité). On ne peut donc pas construire un seuil plus fin que les 4 niveaux. L'indice de danger intégré et l'IFM sont d'autres sources du défi.
- **Les formats changent chaque année** (séparateur, nom de colonne). Un chargement automatique devra gérer les trois cas.
- **Fichiers « documentation » du jeu :** le GeoJSON des départements contient 96 polygones avec seulement les propriétés `code` et `nom`. Il n'y a pas de population ni de surface. L'archive ZIP d'échantillons de l'API n'a pas été ouverte (non vérifiée).
