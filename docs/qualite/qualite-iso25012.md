# La qualité de nos données, avec ISO/IEC 25012

Dernière mise à jour : 2026-11-20

La norme ISO/IEC 25012 ne donne pas de seuils tout faits : elle donne 15 caractéristiques pour décider nous-mêmes ce qu'est une donnée « de bonne qualité » pour notre usage. Notre usage : **aider le SDIS 77 à fixer un seuil de déclenchement et à placer ses moyens**.

## 1. Périmètre

| Jeu de données | Fichier (bronze) | Table de l'entrepôt |
|---|---|---|
| Feux de forêt (BDIFF) | `bdiff/Incendies_2016_2025.csv` | `feux_de_foret`, `suivi_journalier_departement` |
| Météo des forêts | `meteo_des_forets/mdf_2024.csv` à `mdf_2026.csv` | `suivi_journalier_departement` |
| Indices Copernicus | `copernicus/copernicus_AAAA_*.csv` | `suivi_journalier_departement`, `danger_journalier_point_meteo` |

Décision impactée en cas d'erreur : un seuil de déclenchement mal placé (dispositif payé pour rien, ou feux sans dispositif).

## 2. Les parties prenantes

| Rôle | Qui |
|---|---|
| Propriétaire de la donnée (décide des exigences) | le chef de projet, pour le SDIS 77 |
| Responsable qualité (définit et applique les règles) | le responsable qualité et conformité du groupe |
| Producteurs | IGN et ministère de l'Agriculture (BDIFF), Météo-France, Copernicus (ECMWF) |
| Consommateurs | l'équipe Power BI, la direction du SDIS 77 |
| Équipe technique | le responsable pipeline et modèle |

## 3. Les caractéristiques retenues

On ne retient pas les 15 caractéristiques : seulement celles qui comptent pour un entrepôt d'analyse et pour notre décision.

| Caractéristique | Pourquoi elle compte ici |
|---|---|
| **Complétude** | un feu ou un jour manquant fausse directement la part des jours avec feu |
| **Exactitude** | un feu rattaché au mauvais jour ou au mauvais niveau fausse le seuil |
| **Cohérence** | les trois sources doivent parler du même jour et du même département |
| **Actualité** | une décision pour l'été 2027 sur des données de 2024-2025 |
| **Précision** | il faut le jour (pas le mois) et la commune (pas le département) |
| **Traçabilité** | pouvoir prouver d'où vient chaque chiffre du tableau de bord |
| **Compréhensibilité** | l'équipe BI et le SDIS doivent lire les données sans contresens (vide ≠ 0) |

Écartées : confidentialité (aucune donnée personnelle, voir `donnees-personnelles.md`), efficience et récupérabilité (petits volumes, sources publiques retéléchargeables).

## 4. Les exigences, leurs mesures et leur état

Mesures faites sur les fichiers actuels (rapport du pipeline : `data/rapport_qualite.md`).

| Caractéristique | Exigence | Mesure | Seuil | Mesuré | Décision si le seuil n'est pas atteint |
|---|---|---|---|---|---|
| Complétude | chaque feu a une date d'alerte et un département | feux renseignés / feux | 100 % | 100 % (291/291) | bloquer le chargement |
| Complétude | la Météo des forêts a tous les départements, chaque jour de la saison | jours complets / jours de la saison | 100 % | 100 % | alerter |
| Complétude | la cause du feu est connue | feux avec cause / feux | pas de seuil (donnée du producteur) | 43 % (125/291) | publier avec la limite écrite |
| Complétude de la population | les départements de la BSPP ont leurs feux | départements connus / 8 | — | 4/8 | « inconnu » dans l'entrepôt, jamais 0 (décision 007) |
| Exactitude | le niveau est entre 1 et 4 | niveaux valides / niveaux | 100 % | 100 % | bloquer |
| Exactitude | la surface et le FWI ne sont pas négatifs | valeurs ≥ 0 / valeurs | 100 % | 100 % | ligne mise en rejet, alerter |
| Exactitude | les surfaces sont mesurées et non estimées | surfaces mesurées / surfaces | pas de seuil | 20 % (59/291) | limite à afficher : ne pas sur-interpréter les surfaces |
| Cohérence | un feu n'apparaît qu'une fois | identifiants uniques / feux | 100 % | 100 % | bloquer |
| Cohérence | un seul niveau par jour et département | lignes uniques / lignes | 100 % | 100 % | bloquer |
| Cohérence | chaque feu de 2024-2025 est rattaché à un jour de l'entrepôt | feux rattachés / feux | 100 % | 100 % (65/65 dans le 77) | bloquer (test du pipeline) |
| Actualité | des feux de la dernière saison | dernière année de feux | 2026 | 2025 | limite : demander les relevés 2026 au SDIS (décision 002) |
| Actualité | Copernicus mis à jour | date des dernières données | — | 31/08/2026, mises à jour suspendues | limite écrite |
| Précision | le feu est daté au jour, localisé à la commune | feux au jour et à la commune / feux | 100 % | 100 % | — |
| Traçabilité | chaque fichier source a sa provenance et son empreinte | fichiers documentés / fichiers | 100 % | BDIFF et Météo des forêts oui ; Copernicus à compléter (#46) | compléter `data/bronze/SOURCES.md` |
| Compréhensibilité | chaque table et colonne de l'entrepôt est décrite | colonnes décrites / colonnes | 100 % | 100 % (`data/gold/README.md`) | — |

## 5. Comment c'est contrôlé

- **Automatiquement**, à chaque `python -m pipeline` : les règles « bloquer » et « alerter » (`pipeline/qualite.py`), les lignes rejetées dans `data/silver/rejets/`, le rapport `data/rapport_qualite.md`, le journal de chargement avec l'empreinte de chaque fichier.
- **Par des tests** (`pytest`) : feux tous rattachés, « inconnu » jamais transformé en 0, résultats identiques à chaque exécution.
- **À la main** : la crédibilité et la compréhensibilité, en vérifiant dans Power BI les chiffres de contrôle du guide (251 feux, 65 feux…).

## 6. Bilan

Les données **inhérentes** sont propres là où on les contrôle : 100 % sur toutes les règles bloquantes. Les vraies faiblesses sont des **limites du producteur**, qu'on ne peut pas corriger et qu'il faut **afficher** : causes inconnues pour plus de la moitié des feux, surfaces estimées, BSPP absente, une seule dernière saison (2025), et un historique d'indice court.
