# Guide pour Claude : construire le tableau de bord Power BI du SDIS 77

Ce document est un **brief pour un agent Claude qui a accès à Power BI**. Harold le lui donne tel quel, en lui demandant de le suivre. Il dit quoi construire, avec quelles données, quelles mesures et quel style, et comment vérifier que c'est juste.

Dernière mise à jour : 2026-11-21

---

## 0. Ta mission

Tu construis un **tableau de bord d'aide à la décision** pour la direction du SDIS 77 (Service départemental d'incendie et de secours de Seine-et-Marne), qui prépare la saison des feux de forêt 2027.

La direction a posé deux questions. Le tableau de bord doit y répondre en premier :
1. **Où concentrer nos moyens ?**
2. **À partir de quel niveau de danger déclencher le dispositif renforcé ?**

Nous avons découpé ces deux questions en cinq questions analytiques, G1 à G5 (section 4), chacune avec son indicateur.

**Le lecteur** est un directeur de SDIS, pas un analyste. Il a quelques minutes. Chaque page doit donner **une réponse lisible en 5 secondes**, puis le détail pour qui veut vérifier.

**Ton style** : professionnel et épuré. Peu de visuels par page, tous utiles. Pas de décoration.

### Ce que tu fais, dans l'ordre

1. Lire ce guide en entier, puis `data/gold/README.md` (dictionnaire des tables).
2. Charger les 7 CSV et poser les types (section 2).
3. Créer les relations (section 3).
4. Créer les mesures et les paramètres (section 4).
5. **Vérifier chaque chiffre de contrôle (section 6) avant de construire les pages.** Si un chiffre ne correspond pas, corrige le modèle ou la mesure, jamais le chiffre attendu.
6. Construire les pages (section 5) avec le thème (section 7).
7. Faire le rapport final à Harold (section 8).

Si ton accès à Power BI ne permet que le modèle (tables, relations, mesures) et pas les visuels, fais les étapes 1 à 5, puis donne à Harold les instructions pas à pas pour chaque visuel, page par page.

---

## 1. Les règles à ne jamais enfreindre

1. **Une case vide veut dire « on ne sait pas », jamais 0.** Ne remplace jamais un vide par 0, ni dans Power Query, ni dans une mesure (`+ 0`, `COALESCE(..., 0)`), ni dans un visuel. Les vides concernent Paris et la petite couronne (75, 92, 93, 94 : feux inconnus), l'année 2026 (feux pas encore publiés) et les jours hors saison de la Météo des forêts.
2. **Ne modifie pas les fichiers de `data/gold/`.** Ils sont produits par le pipeline du projet. Tout calcul se fait dans Power BI.
3. **N'invente aucun chiffre ni aucune conclusion.** Toute valeur affichée vient d'une mesure. Les textes de conclusion sont ceux de la section 5, rien de plus.
4. **Affiche toujours le volume à côté d'un taux.** « 27 % » sans « 6 jours sur 22 » est trompeur : nos taux reposent sur peu de jours.
5. **Tout en français** : titres, étiquettes, format des nombres (`44,6 %`, `1 234`).
6. **Cite les limites** sur la page qui les concerne, en une ligne, et en entier sur la dernière page.

---

## 2. Les données

### Où

`data/gold/csv/` dans le dépôt, 7 fichiers. Crée un paramètre Power Query `DossierGold` (texte, chemin du dossier `csv` avec le `\` final) et construis chaque source avec `DossierGold & "nom.csv"` : si le dossier change de place, on ne le corrige qu'une fois.

### Format

Séparateur `;`, décimales avec une virgule, encodage **UTF-8 (65001)**, première ligne = en-têtes. Un Power BI en français les lit directement. Vérifie quand même que les accents s'affichent bien (« Fontainebleau », « Val-d'Oise », « Noisy-sur-École »).

### Les tables

| Table | Une ligne = | Lignes | Colonnes |
|---|---|---|---|
| `feux_de_foret` | un feu de forêt (2016-2025) | 291 | `id_feu`, `date`, `code_insee`, `code_departement`, `surface_m2`, `precision_surface`, `cause`, `niveau_mdf_j1`, `fwi_departement` |
| `suivi_journalier_departement` | un jour dans un département (01/01/2024 au 06/10/2026) | 6 163 | `date`, `code_departement`, `niveau_mdf_j1`, `fwi_moyen`, `fwi_max`, `ffmc`, `dmc`, `dc`, `isi`, `bui`, `nb_feux`, `jour_avec_feu` |
| `danger_journalier_point_meteo` | un jour en un point de la grille Copernicus | 12 662 | `date`, `id_point`, `fwi` |
| `calendrier` | un jour, de 2016 à 2026, sans trou | 4 018 | `date`, `annee`, `mois`, `saison_indice` |
| `departements` | un département d'Île-de-France | 8 | `code_departement`, `nom`, `service`, `feux_connus` |
| `communes` | une commune touchée par au moins un feu | 100 | `code_insee`, `nom`, `code_departement` |
| `points_meteo` | un point de la grille Copernicus | 13 | `id_point`, `latitude`, `longitude`, `commune`, `code_departement` |

Ce que veulent dire les colonnes importantes :
- `niveau_mdf_j1` : niveau de la Météo des forêts pour ce jour (1 faible, 2 modéré, 3 élevé, 4 très élevé). Vide hors saison (publié de juin à septembre, depuis 2024).
- `fwi_moyen` / `fwi_max` : indice de danger FWI de Copernicus pour le département, moyenne / maximum de ses points de grille. Il existe toute l'année.
- `nb_feux` : nombre de feux de forêt ce jour-là dans le département. **Vide = inconnu** (BSPP, 2026), 0 = aucun feu.
- `jour_avec_feu` : vrai si `nb_feux` ≥ 1, vide si `nb_feux` est inconnu.

### Les types à poser dans Power Query

| Colonnes | Type |
|---|---|
| `date` (toutes les tables) | Date (pas Date/Heure) |
| `code_departement`, `code_insee`, `id_point`, `id_feu` | **Texte** (ce sont des codes : `77`, `77186`, `2016-688` ne doivent pas devenir des nombres ou des dates) |
| `nb_feux`, `niveau_mdf_j1`, `surface_m2`, `annee`, `mois` | Nombre entier |
| `fwi`, `fwi_moyen`, `fwi_max`, `ffmc`, `dmc`, `dc`, `isi`, `bui`, `fwi_departement`, `latitude`, `longitude` | Nombre décimal |
| `jour_avec_feu`, `feux_connus`, `saison_indice` | Vrai/Faux |

Supprime l'étape « Type modifié » automatique si elle contredit ce tableau.

---

## 3. Le modèle

Désactive la détection automatique des relations, supprime celles qui ont été créées, puis crée ces 7 relations, toutes **1 à plusieurs, filtrage unique** (de la liste vers le suivi) :

| Côté 1 | Côté plusieurs | Colonne |
|---|---|---|
| `calendrier` | `feux_de_foret` | `date` |
| `calendrier` | `suivi_journalier_departement` | `date` |
| `calendrier` | `danger_journalier_point_meteo` | `date` |
| `departements` | `feux_de_foret` | `code_departement` |
| `departements` | `suivi_journalier_departement` | `code_departement` |
| `communes` | `feux_de_foret` | `code_insee` |
| `points_meteo` | `danger_journalier_point_meteo` | `id_point` |

- Ne relie **pas** `communes` ni `points_meteo` à `departements` (deux chemins de filtre).
- Ne relie **jamais** les trois tables de suivi entre elles.
- Marque `calendrier` comme table de dates.
- Masque les clés des tables de suivi dans la vue rapport : on filtre avec les colonnes de `calendrier`, `departements` et `communes`.
- Range les mesures dans une table vide `_Mesures`, en dossiers d'affichage `G1` à `G5` et `Base`.
- Ajoute une colonne lisible pour le niveau, dans `suivi_journalier_departement` et dans `feux_de_foret` : `1 - Faible`, `2 - Modéré`, `3 - Élevé`, `4 - Très élevé`, et `Hors saison` quand le niveau est vide.

---

## 4. Les indicateurs et les mesures

Les définitions viennent de nos fiches indicateurs (`kpi/02_fiches_indicateurs.md`). Écris les mesures DAX toi-même à partir de ces définitions, puis valide-les avec les chiffres de contrôle de la section 6.

### Paramètres (segments)

| Paramètre | Valeurs | Défaut | Sert à |
|---|---|---|---|
| `Seuil Météo des forêts` (N) | 2, 3, 4 | 2 | G2, G3, G4 |
| `Seuil FWI` (S) | 0 à 40, pas de 0,5 | 21,3 | G2 (menu par budget), G5 |
| `Communes couvertes` (k) | 1, 3, 5 | 3 | G1 |
| `Indicateur FWI` | `fwi_max`, `fwi_moyen` | `fwi_max` | G2, G5 |

Pourquoi N = 2 par défaut : dans le 77, il n'y a eu qu'**un seul jour de niveau 3** en 2024-2025. Avec N = 3, les taux ne veulent rien dire.

Pourquoi S = 21,3 par défaut : c'est le début de la classe « élevé » de l'échelle européenne EFFIS (classes : < 11,2 / 11,2 à 21,3 / 21,3 à 38 / 38 à 50 / 50 à 70 / > 70).

### Mesures de base

| Mesure | Définition |
|---|---|
| `Nombre de feux` | nombre de lignes de `feux_de_foret` |
| `Surface brûlée (ha)` | somme de `surface_m2` / 10 000 |
| `Jours connus` | jours de `suivi_journalier_departement` où `nb_feux` n'est pas vide |
| `Jours avec feu` | jours où `jour_avec_feu` est vrai |
| `Part des jours avec feu` | `Jours avec feu` / `Jours connus` |

### G1 : où partent les feux ? (moyens fixes)

**Indicateur : part des départs de feu partis dans les k communes couvertes.** Fiche d'Iris.

- Les k communes sont choisies **à l'avance**, sur 2016-2023 : celles du 77 qui ont eu le plus de feux sur cette période. Le taux est **mesuré sur 2024-2025**, des années qui n'ont pas servi au choix. C'est ce qui rend le chiffre honnête : ne choisis jamais les communes sur la période où tu mesures.
- Pour cela, ajoute à `communes` une colonne calculée `rang_2016_2023` : le rang de la commune parmi celles du 77 selon son nombre de feux avant le 01/01/2024 (ex æquo au même rang). Fontainebleau est 1re, Noisy-sur-École et Nemours sont 2es ex æquo, Arbonne-la-Forêt et Larchant 4es ex æquo.
- `Part des feux dans la zone` = feux du 77 dans les communes de rang ≤ k / tous les feux du 77, sur la période filtrée.
- **Garde-fou** : `Part de la surface hors zone` = surface brûlée hors des communes de rang ≤ k / surface brûlée totale du 77. Si la zone capte beaucoup de petits feux mais que les gros partent ailleurs, il monte.
- **Stabilité** : nombre d'années, de 2016 à 2025, où la commune est dans les 3 communes du 77 qui ont eu le plus de feux cette année-là. Moins de 5 sur 10 : la commune ne justifie pas de moyens fixes.

### G2 : à partir de quel niveau déclencher ? (le seuil)

**Indicateur principal : taux de jours d'alerte sans feu.** Fiche d'Aboubacrine.

- `Jours d'alerte (N)` = jours du 77 où `niveau_mdf_j1` ≥ N.
- `Jours d'alerte sans feu (N)` = parmi eux, ceux où `jour_avec_feu` est faux.
- `Taux de jours d'alerte sans feu` = `Jours d'alerte sans feu (N)` / `Jours d'alerte (N)`. Élevé = beaucoup de jours payés pour rien.
- **Garde-fou** : `Part des feux les jours sous le seuil` = feux du 77 partis un jour où `niveau_mdf_j1` < N / feux du 77 partis pendant la saison de l'indice (`niveau_mdf_j1` non vide). Il monte quand on relève N : on ne lit jamais le taux principal sans lui.
- **Plancher** : si `Jours d'alerte (N)` < 10, affiche « Trop peu de jours pour conclure » à la place du taux.

**Le menu par budget, sur le FWI de Copernicus** (décision 008 : la Météo des forêts n'existe que de juin à septembre depuis 2024, le FWI toute l'année) :
- `Jours d'alerte FWI` = jours où `Indicateur FWI` ≥ S, parmi les jours connus.
- `Jours d'alerte FWI par an` = `Jours d'alerte FWI` / nombre d'années où l'on a à la fois des feux connus et le FWI. C'est le **coût**.
- `Feux couverts (%)` = somme de `nb_feux` les jours où FWI ≥ S / somme de `nb_feux` les jours où le FWI existe. C'est le **bénéfice**.
- `Alertes sans feu (%)` = jours d'alerte FWI sans feu / jours d'alerte FWI.

En faisant glisser S, le directeur voit en direct ce que chaque seuil coûte (jours de dispositif par an) et ce qu'il rapporte (part des feux couverts).

### G3 : les feux des jours d'indice bas

**Indicateur : nombre de feux partis les jours d'indice bas.** Fiche de Harold.

- `Feux des jours bas (N)` = feux du 77 partis pendant la saison de l'indice, un jour où `niveau_mdf_j1` < N.
- `Part des feux des jours bas` = `Feux des jours bas (N)` / feux du 77 partis pendant la saison de l'indice. C'est un indicateur de diagnostic.
- Pour chercher un point commun (cause, commune, mois), **compare toujours** la répartition des feux des jours bas à celle de tous les feux de la même saison. Un point commun n'en est un que s'il est nettement différent. Exemple : Fontainebleau fait 40 % des feux de niveau 1 en 2025, contre 43 % de tous les feux de la saison 2025. Ce n'est pas un point commun des jours bas, c'est la concentration déjà vue en G1.
- Affiche la part de **cause inconnue** à côté de toute répartition par cause.

### G4 : le 77 face à l'Île-de-France

**Indicateur : écart de la part des jours d'alerte avec feu, 77 contre autres départements d'Île-de-France.** Fiche d'Iris.

- Pour chaque département : jours où `niveau_mdf_j1` ≥ N **et** avec au moins un feu / jours où `niveau_mdf_j1` ≥ N.
- Groupe de comparaison : 78, 91 et 95 regroupés. 75, 92, 93 et 94 sont exclus (feux inconnus) : laisse-les vides, ne les montre jamais à 0.
- **Verdict de la fiche : non tranché.** Les autres départements n'ont que 3 feux en saison de l'indice sur deux ans. Affiche le nombre de feux à côté de chaque taux, et le message « Trop peu de feux hors 77 pour comparer ».

### G5 : les indices météo détaillés

**Indicateur : part des jours d'alerte Copernicus avec feu.** Fiche de Daryl.

- Même principe que G2, mais avec le FWI au lieu du niveau de la Météo des forêts : jours du 77 où `fwi_max` ≥ S avec au moins un feu / jours du 77 où `fwi_max` ≥ S.
- Comparaison à **budget égal** : sur la saison de l'indice 2024-2025, la Météo des forêts a mis 22 jours en alerte (N = 2). Le seuil FWI qui donne aussi 22 jours est `fwi_max` ≥ 24,64. On compare alors la part des jours d'alerte avec feu des deux indices.
- Visuel de contexte : valeur moyenne de `ffmc`, `dmc`, `dc`, `isi`, `bui` et `fwi_max` les jours avec feu et les jours sans feu. Attention : `ffmc`, `dmc`, `dc`, `isi` et `bui` sont des **moyennes** du département, seul le FWI a aussi un maximum.

---

## 5. Les pages

Sur chaque page : un titre qui est une **question**, une ligne de **réponse** en dessous, les segments `Année` et `Département` en haut à droite (sauf mention contraire), et une ligne de limites en bas.

Filtres par défaut : **Seine-et-Marne**, années **2024 et 2025** (les seules où l'indice et les feux se croisent), sauf mention contraire.

### Page 1 — Synthèse pour la direction

La page la plus importante. Pas de segment. Deux blocs côte à côte, un par question de la direction :

**Où concentrer nos moyens ?**
- Carte KPI : part des feux à Fontainebleau, 2024-2025 (k = 1).
- Carte KPI : stabilité de Fontainebleau (années dans le top 3, sur 10).
- Texte : « Fontainebleau concentre près de la moitié des feux du 77 en 2024-2025, et figure parmi les 3 communes les plus touchées chaque année depuis 2016. Les autres communes changent d'une année à l'autre : pour elles, des moyens mobiles plutôt que fixes. »

**À partir de quel niveau déclencher ?**
- Petit tableau, une ligne par seuil N (2, 3) : jours d'alerte, jours sans feu, taux de jours d'alerte sans feu, part des feux les jours sous le seuil.
- Texte : « Le 77 n'a connu qu'un seul jour de niveau 3 en deux ans : le niveau de la Météo des forêts ne permet pas de fixer un seuil fiable. Le FWI de Copernicus, disponible toute l'année, permet de choisir un seuil selon le budget (page 3). »

En bas : « Données : BDIFF 2016-2025, Météo des forêts 2024-2026, Copernicus 2024-2026. Limites : page 7. »

### Page 2 — Où partent les feux ? (G1)

Filtres : Seine-et-Marne. Segment `Communes couvertes (k)`.
- Cartes KPI : `Part des feux dans la zone` (2024-2025), `Part de la surface hors zone`.
- Barres horizontales : 10 communes avec le plus de feux, 2016-2025, avec `Nombre de feux`.
- Matrice commune × année (10 premières communes, 2016-2025), valeur `Nombre de feux`, mise en forme conditionnelle en dégradé d'une seule couleur, avec une colonne `Stabilité` : montre d'un coup d'œil que Fontainebleau est là chaque année.
- Réponse : « Fontainebleau : 44,6 % des feux de 2024-2025, dans le top 3 chaque année. Ajouter 2 communes n'apporte que 6 points. »

### Page 3 — À partir de quand déclencher ? (G2)

Deux parties.

En haut, **la Météo des forêts** (segment N) :
- Tableau par niveau (1 à 4) : jours, jours avec feu, part des jours avec feu.
- Cartes KPI : `Jours d'alerte (N)`, `Taux de jours d'alerte sans feu`, `Part des feux les jours sous le seuil`.

En bas, **le menu par budget sur le FWI** (segment S, en curseur) :
- Trois cartes KPI : `Jours d'alerte FWI par an` (coût), `Feux couverts (%)` (bénéfice), `Alertes sans feu (%)`.
- Courbe : en abscisse le seuil S, en ordonnée `Feux couverts (%)` et `Jours d'alerte FWI par an`. C'est le compromis à montrer.
- Réponse : « Avec le niveau de la Météo des forêts, pas assez de jours de danger pour conclure. Avec le FWI, chaque seuil a un coût et un bénéfice : à la direction de choisir selon son budget. »

### Page 4 — Les feux des jours d'indice bas (G3)

Filtres : Seine-et-Marne, saison de l'indice 2024-2025. Segment N.
- Cartes KPI : `Feux des jours bas (N)` et sa part.
- Barres groupées : répartition par cause, **jours bas contre toute la saison**, avec la barre « Cause inconnue ».
- Même chose par mois et pour les 5 premières communes.
- Réponse : « Les feux des jours bas ressemblent aux autres : pas de point commun propre. La moitié n'ont pas de cause connue. »

### Page 5 — Le 77 face à l'Île-de-France (G4)

Pas de filtre département. Segment N.
- Barres : part des jours d'alerte avec feu par département, avec le nombre de jours d'alerte et de feux en étiquette. Départements de la BSPP absents ou marqués « inconnu ».
- Bandeau visible : « Trop peu de feux hors du 77 (3 en deux saisons) pour comparer. »

### Page 6 — Les indices de danger (G5)

Filtres : Seine-et-Marne, 2024-2025.
- Comparaison à budget égal (22 jours) : deux cartes, part des jours d'alerte avec feu pour la Météo des forêts (N = 2) et pour le FWI (`fwi_max` ≥ 24,64).
- Barres groupées : moyenne de chaque indice les jours avec feu et les jours sans feu.
- Courbe dans le temps : `fwi_max` du 77 par jour, avec les jours de feu en points.
- Réponse : « À nombre de jours d'alerte égal, le FWI repère un peu plus de jours de feu que la Météo des forêts (7 contre 6 sur 22). L'écart est faible sur deux saisons. »

### Page 7 — Sources et limites

Texte seulement, en deux colonnes.

Sources : BDIFF (feux de forêt, 2016-2025), Météo des forêts (Météo-France, 2024-2026), Copernicus CEMS (indices de danger, 2024-2026).

Limites :
- Seulement **2024 et 2025** pour croiser l'indice et les feux. 2026 n'a pas encore de feux publiés.
- **Feux de forêt seulement** : les autres feux de végétation ne sont pas dans la BDIFF.
- **Paris et la petite couronne (BSPP)** : nombre de feux inconnu.
- La Météo des forêts n'est publiée que **de juin à septembre**. Le FWI existe toute l'année.
- Le FWI de Copernicus est une **reconstitution après coup**, pas la prévision que le SDIS reçoit la veille. Un seuil trouvé ici est à faire traduire par Météo-France.
- La **cause** est inconnue pour plus de la moitié des feux, et la plupart des **surfaces** sont estimées.

---

## 6. Les chiffres de contrôle

Calculés sur les fichiers gold. Vérifie chaque ligne **avant** de construire les pages. Filtre : Seine-et-Marne, sauf mention contraire.

| # | Contrôle | Filtre | Attendu |
|---|---|---|---|
| 1 | `Nombre de feux` | toutes les régions, 2016-2025 | 291 |
| 2 | `Nombre de feux` | 2016-2025 | 251 |
| 3 | `Nombre de feux` | 2024-2025 | 65 (10 en 2024, 55 en 2025) |
| 4 | Feux par département | 2016-2025 | 77 : 251, 91 : 35, 78 : 4, 95 : 1 |
| 5 | G1 `Part des feux dans la zone` | 2024-2025, k = 1 / 3 / 5 | 44,6 % / 50,8 % / 53,8 % |
| 6 | G1 `Part de la surface hors zone` | 2024-2025, k = 1 / 3 / 5 | 15,0 % / 12,9 % / 7,9 % |
| 7 | G1 stabilité de Fontainebleau | 2016-2025 | 10 sur 10 |
| 8 | Jours de saison de l'indice | 2024-2025 | 240 (218 de niveau 1, 21 de niveau 2, 1 de niveau 3) |
| 9 | G2 `Jours d'alerte (N)` et sans feu | 2024-2025, N = 2 | 22 jours, 16 sans feu, taux 72,7 % |
| 10 | G2 avec N = 3 | 2024-2025 | 1 jour, sans feu : « Trop peu de jours pour conclure » |
| 11 | G2 `Part des feux les jours sous le seuil` | 2024-2025, N = 2 | 26 feux sur 36, soit 72,2 % |
| 12 | Menu FWI, `fwi_max`, S = 21,3 | 2024-2025 | 39 jours d'alerte (19,5 par an), 13 avec feu, feux couverts 18 sur 65 (27,7 %), alertes sans feu 66,7 % |
| 13 | Menu FWI, `fwi_max`, S = 11,2 | 2024-2025 | 127 jours d'alerte, 31 avec feu, feux couverts 40 sur 65 (61,5 %) |
| 14 | Menu FWI, `fwi_moyen`, S = 21,3 | 2024-2025 | 22 jours d'alerte, 6 avec feu, feux couverts 10 |
| 15 | G3 `Feux des jours bas` | 2025, N = 2 | 20 feux sur 30 (66,7 %), dont 10 sans cause connue |
| 16 | G3 part de Fontainebleau | 2025, saison de l'indice | 40,0 % des feux de niveau 1, 43,3 % de tous les feux |
| 17 | G4 jours d'alerte avec feu | 2024-2025, N = 2 | 77 : 6 sur 22 ; 78 : 1 sur 18 ; 91 : 1 sur 28 ; 95 : 0 sur 17 |
| 18 | G5 à budget égal | saison de l'indice 2024-2025, `fwi_max` ≥ 24,64 | 22 jours, 7 avec feu (31,8 %), contre 6 sur 22 (27,3 %) pour la Météo des forêts |
| 19 | `nb_feux` de Paris (75) | toutes années | vide, jamais 0 |

Si un contrôle échoue, cherche dans cet ordre : les relations (section 3), les types (surtout `code_departement` en texte), les filtres de la page, puis la mesure.

---

## 7. Le style

### Principes

- **Une page = une question = une réponse.** La réponse est écrite sous le titre, pas à deviner.
- **Au plus 4 à 5 visuels par page.** Si un visuel ne sert pas la réponse, retire-le.
- **Les chiffres clés en haut** (cartes KPI), le détail en dessous.
- **Pas** de 3D, de camembert de plus de 3 parts, de jauge, d'ombre, de dégradé de fond, ni de logo inventé. N'utilise pas le logo du SDIS 77 : nous n'avons pas l'autorisation.
- **Axes à zéro** pour les barres. Étiquettes de données plutôt qu'axes chargés.
- **Couleur avec du sens** : du gris pour le contexte, une seule couleur d'accent pour ce qu'on veut faire voir. Les couleurs du niveau de danger ne servent qu'au niveau de danger.

### Mise en page

Format 16:9 (1280 × 720). Marge de 24 px. Bandeau de titre en haut (titre de 20 pt, réponse de 12 pt en gris foncé), segments alignés à droite dans le bandeau, cartes KPI sur une ligne, visuels dans une grille à 2 colonnes, ligne de limites en bas (9 pt, gris).

Une barre de navigation à gauche ou en haut, avec les 7 pages, identique sur toutes les pages.

### Thème

Importe ce thème (**Affichage → Thèmes → Parcourir les thèmes**, enregistré en `dashboard/theme-sdis77.json`) :

```json
{
  "name": "SDIS 77 sobre",
  "dataColors": ["#B3261E", "#5F6B7A", "#9AA5B1", "#D9822B", "#2E7D5B", "#3D5A80"],
  "background": "#FFFFFF",
  "foreground": "#1F2933",
  "tableAccent": "#B3261E",
  "good": "#2E7D5B",
  "neutral": "#D9822B",
  "bad": "#B3261E",
  "textClasses": {
    "title": { "fontFace": "Segoe UI Semibold", "fontSize": 14, "color": "#1F2933" },
    "header": { "fontFace": "Segoe UI Semibold", "fontSize": 12, "color": "#1F2933" },
    "label": { "fontFace": "Segoe UI", "fontSize": 10, "color": "#5F6B7A" },
    "callout": { "fontFace": "Segoe UI Semibold", "fontSize": 28, "color": "#1F2933" }
  }
}
```

- Accent : rouge `#B3261E` (feu, danger), à utiliser avec parcimonie.
- Niveaux de danger : 1 `#2E7D5B` (vert), 2 `#E0B000` (jaune), 3 `#D9822B` (orange), 4 `#B3261E` (rouge), hors saison `#C9CED6` (gris).
- Fond de page blanc, cartes sur fond `#F5F7FA`, sans bordure ou avec une bordure fine `#E4E7EB`.

---

## 8. Livrables et rapport final

### Où enregistrer

- Le rapport : `dashboard/tableau_de_bord_sdis77.pbip` (format **Projet Power BI**, des fichiers texte que git peut suivre). Si ce format n'est pas disponible, `dashboard/tableau_de_bord_sdis77.pbix`.
- Le thème : `dashboard/theme-sdis77.json`.
- Ne fais **aucune action git** (commit, push, pull request) : Harold s'en charge.

### Ton rapport à Harold

À la fin, donne à Harold :
1. le tableau de la section 6 avec, pour chaque ligne, la valeur obtenue et ✅ ou ❌ ;
2. la liste des mesures créées, avec leur dossier ;
3. ce que tu n'as pas pu faire, et pourquoi (par exemple : visuels non accessibles avec tes outils) ;
4. tout écart entre ce guide et les données. Signale-le, ne le corrige pas en silence.

### Si quelque chose n'est pas clair

Les documents du projet font foi, dans cet ordre :
1. `data/gold/README.md` : ce que contient chaque colonne ;
2. `kpi/02_fiches_indicateurs.md` (et les fiches G4 et G5 sur les branches `20-fiche-g4-iris` et `20-fiche-g5-daryl` si elles ne sont pas encore sur main) : la définition des indicateurs ;
3. `docs/journal-des-decisions.md` : les choix du groupe ;
4. `docs/glossaire.md` : le sens des mots.

Si la réponse n'y est pas, pose la question à Harold plutôt que de deviner.
