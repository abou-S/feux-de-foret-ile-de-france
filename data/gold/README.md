# Gold : le dictionnaire des tables

Ces fichiers sont produits par `python -m pipeline` et lus par Power BI. Ils sont **propres et prêts à relier**, mais ne contiennent **aucune analyse** : les seuils, taux et comparaisons se calculent dans Power BI.

- Format : une copie **CSV** de chaque table dans `csv/`, au format français (séparateur `;`, décimales avec une virgule, UTF-8), à utiliser dans Power BI ; et un fichier **Parquet** par table dans ce dossier.
- Zone : **Île-de-France** seulement (décision 007).
- Schéma dessiné et relations à créer : `pipeline/README.md`.

## Vue d'ensemble

```
                                   calendrier
                    ┌──────────────────┼────────────────────────┐
                    │                  │                        │
communes ──── feux_de_foret   suivi_journalier_departement   danger_journalier_point_meteo ──── points_meteo
                    │                  │
                    └─── departements ─┘
```

| Table | Une ligne = | Lignes | Sert à |
|---|---|---|---|
| `feux_de_foret` | un feu de forêt | 291 | G1 (où partent les feux), G3 (feux des jours d'indice bas) |
| `suivi_journalier_departement` | un jour dans un département | 6 163 | G2 (seuil), G4 (comparer les départements), G5 (indices) |
| `danger_journalier_point_meteo` | un jour en un point de la grille Copernicus | 12 662 | G2 et G5 sur un point précis (ex. près de Fontainebleau) |
| `calendrier` | un jour (tous les jours de 2016 à 2026, sans trou) | 4 018 | filtrer par date, année, mois, saison |
| `departements` | un département d'Île-de-France | 8 | filtrer par département, savoir si les feux sont connus |
| `communes` | une commune touchée par au moins un feu | 100 | afficher le nom des communes |
| `points_meteo` | un point de la grille Copernicus | 13 | choisir un point, le placer sur une carte |

**La règle la plus importante :** une case **vide** veut dire **« on ne sait pas »**, jamais « zéro ». Ne remplacez pas les vides par 0 dans Power BI.

---

## `feux_de_foret` : les feux

**Une ligne = un feu de forêt** enregistré dans la BDIFF (un départ de feu = une fiche BDIFF, décision 006). De 2016 à 2025.

| Colonne | Type | Ce que c'est | Vide quand… |
|---|---|---|---|
| `id_feu` | texte | identifiant du feu : année et numéro BDIFF (ex. `2025-694`) | jamais |
| `date` | date | jour de la première alerte | jamais |
| `code_insee` | texte | commune où le feu est parti (relie à `communes`) | jamais |
| `code_departement` | texte | département du feu (`77`, `78`, `91`, `95`) | jamais |
| `surface_m2` | entier | surface brûlée, en m² (10 000 m² = 1 ha) | jamais |
| `precision_surface` | texte | `Estimées` (232 feux) ou `Mesurées` (59) | jamais |
| `cause` | texte | `Involontaire (particulier)`, `Involontaire (travaux)`, `Accidentelle`, `Malveillance` | la cause est inconnue (166 feux sur 291) |
| `niveau_mdf_j1` | entier | niveau de la Météo des forêts ce jour-là : 1 faible, 2 modéré, 3 élevé, 4 très élevé | le jour est hors de la saison de l'indice (publié de juin à septembre, depuis 2024) |
| `fwi_departement` | décimal | indice de danger Copernicus (FWI) du département ce jour-là | pas de donnée Copernicus ce jour-là (avant 2024 pour l'instant) |

Exemple réel : `2025-21228 | 2025-04-09 | 77186 | 77 | 380 | Estimées | Involontaire (particulier) | (vide) | 13,9` → un feu de 380 m² à Fontainebleau le 9 avril 2025, causé par un particulier, sans niveau Météo des forêts (avril, hors saison), avec un FWI de 13,9 dans le 77 ce jour-là.

---

## `suivi_journalier_departement` : chaque jour, dans chaque département

**Une ligne = un jour dans un département d'Île-de-France.** Du 01/01/2024 au 06/10/2026. C'est la table centrale pour le seuil de déclenchement.

| Colonne | Type | Ce que c'est | Vide quand… |
|---|---|---|---|
| `date` | date | le jour | jamais |
| `code_departement` | texte | le département | jamais |
| `niveau_mdf_j1` | entier | niveau de la Météo des forêts **prévu la veille** pour ce jour (1 à 4) | hors saison de l'indice (octobre à mai) |
| `fwi_moyen` | décimal | FWI Copernicus : moyenne des points de la grille du département | pas de point Copernicus dans le département (75, 92, 93) ou pas de donnée ce jour-là |
| `fwi_max` | décimal | FWI Copernicus : le point le plus dangereux du département ce jour-là | idem |
| `ffmc` | décimal | sécheresse des petits combustibles en surface (facilité d'allumage) | idem |
| `dmc` | décimal | sécheresse de la couche organique intermédiaire | idem |
| `dc` | décimal | sécheresse profonde du sol (sécheresse longue) | idem |
| `isi` | décimal | vitesse de propagation attendue (vent) | idem |
| `bui` | décimal | combustible disponible | idem |
| `nb_feux` | entier | nombre de feux partis ce jour-là dans le département | **inconnu** : départements de la BSPP (75, 92, 93, 94) et années sans BDIFF (2026) |
| `jour_avec_feu` | vrai/faux | vrai si au moins un feu ce jour-là | **inconnu**, mêmes cas que `nb_feux` |

Plus le FWI est haut, plus le danger météorologique est fort. Il est continu et sans unité : dans le 77, il va de 0 à environ 40. Classes EFFIS de référence : moins de 11,2 faible ; 11,2 à 21,3 modéré ; 21,3 à 38 élevé ; 38 à 50 très élevé.

---

## `danger_journalier_point_meteo` : chaque jour, en chaque point de la grille

**Une ligne = un jour en un point de la grille Copernicus.** Les points sont espacés d'environ 30 km. Du 01/01/2024 au 31/08/2026.

| Colonne | Type | Ce que c'est | Vide quand… |
|---|---|---|---|
| `date` | date | le jour | jamais |
| `id_point` | texte | le point (relie à `points_meteo`) | jamais |
| `fwi` | décimal | FWI Copernicus à ce point ce jour-là | jamais |

Pourquoi cette table : les feux du 77 sont concentrés autour de Fontainebleau (45 %), et la moyenne du département dilue le danger. Le point **`48.478_2.800` (Féricy)** est le plus proche de Fontainebleau (11 km) : c'est celui de la décision 008.

---

## Les dimensions

### `calendrier`

| Colonne | Type | Ce que c'est |
|---|---|---|
| `date` | date | le jour (clé) |
| `annee` | entier | l'année |
| `mois` | entier | le mois (1 à 12) |
| `saison_indice` | vrai/faux | vrai si la Météo des forêts a été publiée pour ce jour |

Elle contient tous les jours du 01/01/2016 au 31/12/2026, sans trou. Dans Power BI, la marquer comme **table de dates**.

### `departements`

| Colonne | Type | Ce que c'est |
|---|---|---|
| `code_departement` | texte | le code (clé) : `75`, `77`, `78`, `91`, `92`, `93`, `94`, `95` |
| `nom` | texte | le nom |
| `service` | texte | `SDIS` ou `BSPP` (Paris et petite couronne) |
| `feux_connus` | vrai/faux | faux pour la BSPP : la BDIFF ne donne pas leurs feux |

### `communes`

| Colonne | Type | Ce que c'est |
|---|---|---|
| `code_insee` | texte | le code INSEE de la commune (clé) |
| `nom` | texte | le nom |
| `code_departement` | texte | le département (à ne **pas** relier à `departements`) |

Seulement les 100 communes où au moins un feu est parti.

### `points_meteo`

| Colonne | Type | Ce que c'est |
|---|---|---|
| `id_point` | texte | identifiant du point : latitude et longitude arrondies (clé) |
| `latitude`, `longitude` | décimal | position du point (pour une carte) |
| `commune` | texte | commune où tombe le point |
| `code_departement` | texte | département du point (à ne **pas** relier à `departements`) |

Les 13 points en Île-de-France : 6 dans le 77, 2 dans le 78, 2 dans le 91, 1 dans le 94, 2 dans le 95. Aucun dans le 75, le 92 ou le 93 (trop petits pour la grille).

---

## Exemples de mesures dans Power BI

Pour bien démarrer, sans faire l'analyse à votre place :

```
Nombre de feux        = COUNTROWS ( feux_de_foret )
Jours avec feu        = CALCULATE ( COUNTROWS ( suivi_journalier_departement ), suivi_journalier_departement[jour_avec_feu] = TRUE () )
Jours avec niveau ≥ 2 = CALCULATE ( COUNTROWS ( suivi_journalier_departement ), suivi_journalier_departement[niveau_mdf_j1] >= 2 )
```

Pour tester un seuil de FWI, créez un **paramètre de simulation** (Modélisation → Nouveau paramètre) et comparez-le à `fwi_moyen`, `fwi_max` ou au `fwi` d'un point de `danger_journalier_point_meteo`.

## Les limites à afficher sur le tableau de bord

- Seulement **2024 et 2025** pour croiser l'indice et les feux. 2026 n'a pas encore de feux publiés.
- **Feux de forêt seulement** (BDIFF), pas les autres feux de végétation (décision 006).
- **BSPP (75, 92, 93, 94) :** nombre de feux inconnu.
- Le FWI Copernicus est une **reconstitution après coup**, pas la prévision que le SDIS reçoit la veille.
