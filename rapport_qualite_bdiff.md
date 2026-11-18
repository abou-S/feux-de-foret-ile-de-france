# Rapport de qualité — BDIFF

- **Fichier :** Incendies.csv, export BDIFF, Île-de-France (8 départements demandés), 01/01/2016 – 31/12/2025
- **Volume :** 291 lignes × 24 colonnes (+ 1 colonne « Mois » calculée)
- **Script :** `docs/analyse/qualite_bdiff.py`
- **Profilé par :** Iris Pouth Nadia, 2026-11-18

## 1. Profil

| Constat | Chiffre | Dimension |
|---|---|---|
| Clés complètes : Année, Numéro, Département, Code INSEE, Commune, Date de première alerte, Surface parcourue | 100 % remplies | Complétude des valeurs |
| Feux par département | 77 : 251 · 91 : 35 · 78 : 4 · 95 : 1 · 75, 92, 93, 94 : **aucune ligne** | Complétude des enregistrements |
| Période observée | 22/03/2016 → 05/11/2025 ; les 12 mois sont présents, pic en juillet-août (127 feux, 44 %) ; 2026 absente (diffusion jusqu'à N-1) | Complétude des périodes, actualité |
| Cause (« Nature ») | Manquante pour 166 feux sur 291 (57 %) ; de 0 % (2018) à 100 % (2016) selon l'année | Complétude des valeurs |
| Mécanisme du manque de cause | Manquante pour 44,5 % des petits feux contre 68,2 % des gros feux (coupure à la médiane, 100 m²) | MAR : le manque dépend de la surface et de l'année |
| Précision des surfaces | 232 estimées (80 %), 59 mesurées | Exactitude |
| Surface parcourue | Médiane 100 m², 25 % des feux ≤ 4,5 m², maximum 300 300 m² (30 ha) | Exactitude (bornes plausibles) |
| Colonnes vides | Surface maquis garrigues, Type de peuplement : 0 % rempli | Complétude des valeurs |
| Décès et bâtiments | Remplis à 16,5 %, une seule valeur (0) | Valeur de remplissage |
| Précision de la donnée | Remplie pour 7 lignes (2,4 %) : « Données partielles ou non valides » | Exactitude signalée par le producteur |
| Sous-surfaces (agricoles, non boisées…) | Remplies à 36 % ou 64 % selon la colonne | Complétude des valeurs, peut-être selon la période (à vérifier) |

## 2. Règles de qualité

| Règle | Sélecteur | Prédicat | Seuil | Résultat | Sévérité | Décision |
|---|---|---|---|---|---|---|
| R1 Unicité du feu | Année + Numéro, toutes les lignes | Aucun doublon | 0 doublon | **Réussite** (0/291) | Bloquer | Chargement autorisé |
| R2 Clés valides | Code INSEE, Date de première alerte, Année | Code INSEE sur 5 caractères, date lisible, année de la date = colonne Année | 0 ligne fautive | **Réussite** (0/291) | Bloquer | Jointures avec les communes et la Météo des forêts possibles |
| R3 Couverture département × année | 8 départements IDF × 2016-2025 | Au moins un feu par département et par an | 0 couple absent | **Échec** (62/80 absents) | Alerter | Comparaison entre départements non fiable (G4) |
| R4 Cause renseignée | Nature, toutes les lignes | Valeur non vide | ≥ 80 % renseignée | **Échec** (166/291 manquantes, 43 % renseignées) | Alerter | Analyse des causes limitée et biaisée (G3) |

Le seuil de 80 % pour R4 est une proposition, à valider par le groupe.

## 3. Ce que nos indicateurs peuvent affirmer

- **Où se concentrent les feux dans le 77 (G1)** : la commune, le code INSEE et la date sont complets et sans doublon. Fontainebleau concentre 123 des 251 feux du 77.
- **Quels jours il y a eu des feux (côté feux de G2 et G5)** : la date de première alerte est complète et valide pour 100 % des feux. Elle peut être croisée jour par jour avec l'indice.
- **La saisonnalité des feux** : tous les mois sont présents, avec un pic en juillet-août.

## 4. Ce qu'ils ne peuvent pas affirmer

- **Que le 77 a plus de feux que les autres départements d'Île-de-France (G4).** Paris, les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne n'ont aucune ligne. Les Yvelines (4 feux en 10 ans) et le Val-d'Oise (1 feu) sont presque absents. Dans la donnée, rien ne distingue « aucun feu » de « feu non saisi ». La matrice signale d'ailleurs un « nombre d'incendies inconnu » pour 75, 92, 93 et 94 en 2025.
- **Quelle est la cause principale des feux (G3).** La cause manque pour 57 % des feux, et ce manque n'est pas aléatoire : il touche davantage les gros feux, et varie de 0 % à 100 % selon l'année. Une répartition calculée sur les seules causes connues sous-estimerait les gros feux.
- **Les surfaces brûlées au mètre carré près.** 80 % des surfaces sont estimées : il faut les présenter comme des ordres de grandeur.
- **Quoi que ce soit sur l'été 2026**, qui n'est pas encore diffusé par la BDIFF.
- **Le massif ou la distance aux routes et aux habitations (G1, G3)**, puisque la source ne donne pas de coordonnées.

## 5. À vérifier ensuite

- Paris et la petite couronne : absence réelle de feu de forêt, ou départements non saisis dans la BDIFF ? (Piste : interroger la source « Interventions SIS ».)
- Les 7 lignes marquées « Données partielles ou non valides » : faut-il les garder ?
- Le remplissage des sous-surfaces change-t-il selon l'année (changement de saisie) ?
