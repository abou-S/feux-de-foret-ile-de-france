# Construire le tableau de bord Power BI — guide pas à pas

Pour : l'équipe qui construit le tableau de bord d'aide à la décision du SDIS 77.
Ce guide part des fichiers de `data/gold/` (produits par le pipeline) jusqu'au tableau de bord publié. Le détail de chaque table et de chaque colonne est dans `data/gold/README.md` : gardez-le ouvert à côté.

**Principe :** gold contient des données propres. **Toute l'analyse se fait dans Power BI** : les mesures, les seuils, les taux.

---

## Étape 0 — Préparer le poste

1. **Windows** avec **Power BI Desktop** (gratuit, sur le Microsoft Store).
2. Récupérer le dépôt à jour : `git pull` sur `main`.
3. Vérifier que `data/gold/` contient bien 7 fichiers `.parquet` :
   `calendrier`, `departements`, `communes`, `points_meteo`, `feux_de_foret`, `suivi_journalier_departement`, `danger_journalier_point_meteo`.

Vous n'avez pas besoin de Python : gold est déjà dans le dépôt.

---

## Étape 1 — Charger les 7 tables

### 1.1 Créer un paramètre pour le dossier

Le chemin du dossier change d'un ordinateur à l'autre. On le met dans un paramètre pour ne le changer qu'à un seul endroit.

1. **Accueil → Transformer les données** (Power Query s'ouvre).
2. **Gérer les paramètres → Nouveau paramètre**.
3. Nom : `DossierGold`. Type : **Texte**. Valeur : le chemin complet du dossier, par exemple `C:\Users\vous\feux-de-foret-ile-de-france\data\gold\`. Le `\` final compte.

### 1.2 Charger chaque table

Pour chacune des 7 tables : **Nouvelle source → Requête vide**, puis dans la barre de formule :

```
= Parquet.Document(File.Contents(DossierGold & "feux_de_foret.parquet"))
```

Renommez la requête exactement comme le fichier (`feux_de_foret`, etc.), puis recommencez pour les 6 autres.

Le connecteur **Obtenir les données → Parquet** fonctionne aussi, mais il faut alors coller le chemin de chaque fichier, sans le paramètre.

### 1.3 Vérifier les types dans Power Query

Avant de fermer Power Query, vérifiez l'icône de type en tête des colonnes :

| Colonnes | Type attendu |
|---|---|
| `date` (dans toutes les tables) | **Date** (pas Date/Heure) |
| `code_departement`, `code_insee`, `id_point`, `id_feu` | **Texte** (sinon les codes perdent leur forme) |
| `nb_feux`, `niveau_mdf_j1`, `surface_m2`, `annee`, `mois` | **Nombre entier** |
| `fwi`, `fwi_moyen`, `fwi_max`, `ffmc`, `dmc`, `dc`, `isi`, `bui`, `fwi_departement` | **Nombre décimal** |
| `jour_avec_feu`, `feux_connus`, `saison_indice` | **Vrai/Faux** |

⚠️ **Ne remplacez jamais les valeurs vides (`null`) par 0.** Une case vide veut dire « on ne sait pas » (départements de la BSPP, année 2026, jours hors saison).

**Fermer et appliquer.**

---

## Étape 2 — Construire le modèle (les relations)

1. **Fichier → Options → Chargement des données :** décochez « Détecter automatiquement les nouvelles relations » (sinon Power BI en invente de mauvaises).
2. Vue **Modèle** : supprimez toute relation créée automatiquement.
3. Créez ces **7 relations**, toutes en **1 à plusieurs**, **filtrage unique** (de la liste vers le suivi) :

| Depuis (côté 1) | Vers (côté plusieurs) | Colonne |
|---|---|---|
| `calendrier` | `feux_de_foret` | `date` |
| `calendrier` | `suivi_journalier_departement` | `date` |
| `calendrier` | `danger_journalier_point_meteo` | `date` |
| `departements` | `feux_de_foret` | `code_departement` |
| `departements` | `suivi_journalier_departement` | `code_departement` |
| `communes` | `feux_de_foret` | `code_insee` |
| `points_meteo` | `danger_journalier_point_meteo` | `id_point` |

4. **Ne reliez pas** `communes[code_departement]` ni `points_meteo[code_departement]` à `departements` : ça créerait deux chemins de filtre.
5. **Ne reliez jamais les trois tables de suivi entre elles.**
6. Sélectionnez `calendrier` → **Outils de table → Marquer comme table de dates** → colonne `date`.

Le résultat doit ressembler au schéma de `pipeline/README.md`.

### Rendre le modèle lisible

- **Masquez dans la vue rapport** les colonnes de liaison des tables de suivi (`date`, `code_departement`, `code_insee`, `id_point`) : on filtre avec les colonnes des listes (`calendrier`, `departements`…).
- Rangez les tables en deux **dossiers d'affichage** : « Suivi » (`feux_de_foret`, `suivi_journalier_departement`, `danger_journalier_point_meteo`) et « Listes » (les 4 autres).
- Créez une colonne lisible pour le niveau de danger, dans `suivi_journalier_departement` (et pareil dans `feux_de_foret`) :

```
Niveau Météo des forêts =
SWITCH ( suivi_journalier_departement[niveau_mdf_j1],
    1, "1 - Faible", 2, "2 - Modéré", 3, "3 - Élevé", 4, "4 - Très élevé",
    "Hors saison" )
```

---

## Étape 3 — Créer les mesures

Créez une table vide `_Mesures` (**Accueil → Entrer des données**, puis **OK**) pour y ranger toutes les mesures.

### Mesures de base

```
Nombre de feux = COUNTROWS ( feux_de_foret )

Surface brûlée (ha) = DIVIDE ( SUM ( feux_de_foret[surface_m2] ), 10000 )

Part des feux = DIVIDE ( [Nombre de feux], CALCULATE ( [Nombre de feux], ALL ( communes ) ) )

Jours = COUNTROWS ( suivi_journalier_departement )

Jours connus =
CALCULATE ( [Jours], NOT ISBLANK ( suivi_journalier_departement[nb_feux] ) )

Jours avec feu =
CALCULATE ( [Jours], suivi_journalier_departement[jour_avec_feu] = TRUE () )

Part des jours avec feu = DIVIDE ( [Jours avec feu], [Jours connus] )
```

`Jours connus` ne compte que les jours où le nombre de feux est connu : la BSPP et 2026 sont exclus automatiquement.

### Mesures du seuil de FWI (G2)

1. **Modélisation → Nouveau paramètre → Plage numérique** : nom `Seuil FWI`, de 0 à 40, pas de 0,5, valeur par défaut 21,3 (début de la classe EFFIS « élevé »). Cochez « Ajouter un segment à cette page ». Power BI crée la mesure `[Valeur Seuil FWI]`.
2. Ajoutez ces mesures (avec `fwi_max`, le point le plus dangereux du département ; remplacez par `fwi_moyen` pour comparer) :

```
Jours d'alerte =
VAR s = [Valeur Seuil FWI]
RETURN CALCULATE ( [Jours connus], suivi_journalier_departement[fwi_max] >= s )

Jours d'alerte sans feu =
VAR s = [Valeur Seuil FWI]
RETURN CALCULATE ( [Jours connus],
    suivi_journalier_departement[fwi_max] >= s,
    suivi_journalier_departement[jour_avec_feu] = FALSE () )

Alertes sans feu (%) = DIVIDE ( [Jours d'alerte sans feu], [Jours d'alerte] )

Feux couverts =
VAR s = [Valeur Seuil FWI]
RETURN CALCULATE ( SUM ( suivi_journalier_departement[nb_feux] ), suivi_journalier_departement[fwi_max] >= s )

Feux couverts (%) =
DIVIDE ( [Feux couverts],
    CALCULATE ( SUM ( suivi_journalier_departement[nb_feux] ), NOT ISBLANK ( suivi_journalier_departement[fwi_max] ) ) )

Années croisables =
COUNTROWS ( SUMMARIZE (
    FILTER ( suivi_journalier_departement,
        NOT ISBLANK ( suivi_journalier_departement[nb_feux] ) && NOT ISBLANK ( suivi_journalier_departement[fwi_max] ) ),
    calendrier[annee] ) )

Jours d'alerte par an = DIVIDE ( [Jours d'alerte], [Années croisables] )
```

Avec le segment `Seuil FWI`, l'utilisateur fait glisser le seuil et voit en direct le **coût** (jours d'alerte par an), les **feux couverts** et les **alertes sans feu** : c'est le « menu par budget ».

### Pour aller plus loin : le point près de Fontainebleau

Pour utiliser le point Féricy (`48.478_2.800`, le plus proche de Fontainebleau, décision 008) au lieu du département :

```
Feux couverts (point Fontainebleau) =
VAR s = [Valeur Seuil FWI]
RETURN SUMX (
    FILTER ( danger_journalier_point_meteo,
        danger_journalier_point_meteo[id_point] = "48.478_2.800" && danger_journalier_point_meteo[fwi] >= s ),
    VAR d = danger_journalier_point_meteo[date]
    RETURN CALCULATE ( SUM ( suivi_journalier_departement[nb_feux] ),
        calendrier[date] = d, departements[code_departement] = "77" ) )
```

---

## Étape 4 — Construire les pages

Une page par question, plus une page d'accueil et une page sur les limites. Mettez sur chaque page un **segment `departements[nom]`** et un **segment `calendrier[annee]`**.

| Page | Question | Visuels proposés |
|---|---|---|
| **1. Vue d'ensemble** | — | Cartes : `Nombre de feux`, `Surface brûlée (ha)`, `Part des jours avec feu`. Histogramme : `Nombre de feux` par `calendrier[annee]` |
| **2. Où partent les feux ?** | G1 | Barres : `Nombre de feux` et `Part des feux` par `communes[nom]` (10 premières). Carte : `communes[nom]` (catégorie de données « Lieu »), taille = `Nombre de feux`. Petits multiples par année pour voir si ce sont toujours les mêmes communes |
| **3. À partir de quand déclencher ?** | G2 | Matrice : `Niveau Météo des forêts` en lignes, `Jours`, `Jours avec feu`, `Part des jours avec feu` en valeurs. Segment `Seuil FWI` + cartes `Jours d'alerte par an`, `Feux couverts (%)`, `Alertes sans feu (%)` |
| **4. Les feux des jours d'indice bas** | G3 | Filtre : `feux_de_foret` avec niveau 1 ou FWI sous le seuil. Barres : `Nombre de feux` par `cause`, par `calendrier[mois]`, par commune |
| **5. Le 77 face à l'Île-de-France** | G4 | Matrice : `departements[nom]` × `Niveau Météo des forêts`, valeur `Part des jours avec feu`. Bien laisser vides la BSPP |
| **6. Les indices de danger** | G5 | Barres groupées : moyenne de `ffmc`, `dmc`, `dc`, `isi`, `bui`, `fwi_max` les jours avec feu et sans feu (segment `jour_avec_feu`) |
| **7. Sources et limites** | — | Zone de texte : les limites ci-dessous et les sources (BDIFF, Météo des forêts, Copernicus) |

### Les limites à écrire sur la page 7

- Seulement **2024 et 2025** pour croiser l'indice et les feux ; 2026 n'a pas encore de feux publiés.
- **Feux de forêt seulement** (BDIFF), pas les autres feux de végétation (décision 006).
- **BSPP (75, 92, 93, 94) :** nombre de feux inconnu.
- La Météo des forêts n'est publiée que **de juin à septembre** ; le FWI Copernicus existe toute l'année.
- Le FWI Copernicus est une **reconstitution après coup**, pas la prévision que le SDIS reçoit la veille : un seuil trouvé ici est à faire traduire par Météo-France.

---

## Étape 5 — Vérifier les chiffres

Avant de présenter, comparez avec les études du groupe (notebooks) :

| Contrôle (filtre : Seine-et-Marne) | Valeur attendue |
|---|---|
| `Nombre de feux`, 2016 à 2025 | 251 |
| `Nombre de feux`, 2024 et 2025 | 65 |
| `Jours avec feu`, Niveau 2, 2024-2025 | 6 (sur 21 jours de niveau 2) |
| Part des feux de Fontainebleau, 2024-2025 | environ 45 % |

Si un chiffre diffère, vérifiez d'abord les relations (étape 2) et les filtres de la page.

---

## Étape 6 — Enregistrer, mettre à jour, partager

- **Enregistrer** le fichier dans le dépôt : `dashboard/tableau_de_bord_sdis77.pbix`, sur une branche, puis une pull request.
- **Mettre à jour les données :** quand le pipeline a été relancé et gold poussé, faire `git pull`, puis **Accueil → Actualiser** dans Power BI.
- **Partager :** publier sur le service Power BI (**Accueil → Publier**) si l'école le permet, sinon présenter depuis Power BI Desktop.
