# Journal des décisions

Une entrée par décision. Les entrées 001 à 005 sont des propositions issues de la confrontation questions × sources : elles restent à valider en groupe.

## 001 — G1 : approximer le massif par la commune

- **Question :** G1, les feux du 77 sont-ils concentrés sur quelques communes ou massifs ?
- **Manque :** les massifs (la BDIFF s'arrête à la commune, sans coordonnées) et la campagne 2026.
- **Décision :** approximer.
- **Raison :** la commune est un proxy du massif. Iris a déjà vu que Fontainebleau concentre 123 feux sur 251 (49 %) sur 2016-2025. On relie ensuite les communes aux massifs avec BD Forêt, une fois cette source ouverte.
- **Coût :** une commune peut toucher plusieurs massifs, ou l'inverse. La concentration par massif sera approximative, et 2026 manque.
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)

## 002 — G2 : collecter les feux de 2026

- **Question :** G2, part des jours avec feu par niveau de la Météo des forêts.
- **Manque :** plus de 2 saisons exploitables. L'indice n'existe qu'en 2024-2026 et la BDIFF s'arrête à 2025, donc seules 2024 et 2025 se croisent, et le 77 est au niveau 1 toute l'année 2024.
- **Décision :** collecter.
- **Raison :** le SDIS 77 est à l'origine de la commande, il a sûrement ses propres relevés de 2026. En 2026, le 77 a 62 jours au niveau 2 et 27 au niveau 3, c'est la saison la plus utile pour tester un seuil.
- **Coût :** dépend de la réponse du SDIS avant le 11/12. Repli : comparer « niveau 1 » contre « niveau 2 ou plus » sur 2025, sans pouvoir dire à partir de quel niveau précis déclencher (un seul jour de niveau 3 en 2025).
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)

## 003 — G3 : renoncer à l'indice par secteur

- **Question :** G3 (et la question d'Aboubacrine sur un seuil par secteur du 77).
- **Manque :** l'indice n'existe qu'à l'échelle du département (num_dep) et aucune source ne donne le découpage en secteurs.
- **Décision :** renoncer à la partie « par secteur ».
- **Raison :** aucune source ne permet de la mesurer. On garde le reste de G3 : part des feux les jours d'indice bas et leurs points communs (cause, commune, période) sur tout le 77.
- **Coût :** pas de seuil différent par secteur. La direction aura un seuil unique pour le département. Les causes sont inconnues pour 53 % des feux, donc l'analyse porte sur 119 feux sur 251 (fiche Iris).
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)

## 004 — G4 : approximer la comparaison avec les autres départements

- **Question :** G4, le 77 a-t-il plus ou moins de feux que les autres à niveau d'indice égal ?
- **Manque :** la surface boisée par département, le nombre de feux du 75, 92, 93 et 94 (BSPP), et un niveau d'indice comparable d'un département à l'autre.
- **Décision :** approximer.
- **Raison :** on compare le 77 aux départements qui ont des feux (78, 91, 95) et au reste de la France, en rapportant à la surface boisée une fois BD Forêt ou Corine ouvert. Vérifier d'abord cette source.
- **Coût :** le niveau n'a pas le même sens partout (il tient compte de la forêt de chaque département). La petite couronne est absente et avec 2 ou 3 feux par département la comparaison régionale est fragile. La comparaison avec la moyenne nationale sera plus solide que celle avec les voisins.
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)

## 005 — G5 : croiser Copernicus et la BDIFF, après vérification

- **Question :** G5, quelles conditions météorologiques (Fire weather index, Drought code, Duff moisture code, Fine fuel moisture code) sont associées aux départs de feu et aux incendies les plus importants dans le 77 ?
- **Manque :** les indices sont dans Copernicus, mais aucun fichier n'a été ouvert (dates, volume non vérifiés), les mises à jour sont suspendues depuis le 16/11/2026, et les indices sont sur une grille de points alors que la BDIFF localise les feux à la commune, sans coordonnées. La Météo des forêts ne donne que le niveau de synthèse de 1 à 4, pas les indices.
- **Décision :** vérifier d'abord (ouvrir un fichier Copernicus, noter l'avis de suspension), puis approximer : croiser les indices avec les feux de la BDIFF par la date, en ramenant les indices au département du 77.
- **Raison :** les feux existent dans la BDIFF (c'est ce que Daryl proposait de « collecter »), il manque seulement de confirmer que Copernicus est exploitable. On ne décide pas sur des cellules non vérifiées.
- **Coût :** le croisement se fait à la date et au département, pas à l'endroit exact du feu. Si Copernicus est inexploitable dans le temps du projet, on renonce à G5 ou on se limite au niveau de synthèse de la Météo des forêts, qui n'est pas la valeur des indices.
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)

## 006 — Un départ de feu = un feu de forêt (une fiche BDIFF)

- **Question :** toutes les questions qui comptent des feux (G1 à G5), et en particulier l'indicateur G2 (taux de jours d'alerte sans feu).
- **Manque :** la commande parle à la fois de « feux de forêt » et de « départs de feu » sans les définir. La BDIFF ne garde que les feux de forêt. Les interventions SIS comptent tous les « feux de végétations » (champs, haies, bords de route), mais seulement en total par an. Sans règle, le nombre de feux change selon la source.
- **Décision :** un départ de feu est un feu de forêt, c'est-à-dire une fiche de la BDIFF.
- **Raison :** la commande porte sur la saison des feux de forêt, et le dispositif renforcé (patrouilles, guet) vise les massifs forestiers. La BDIFF est la seule source qui donne chaque feu avec sa date et sa commune.
- **Coût :** les petits feux hors forêt (haies, champs, bords de route) sortent du périmètre. Ce n'est plus un biais de mesure mais une limite écrite : nos chiffres ne parlent que des feux de forêt. Pour élargir plus tard, il faudrait les relevés du SDIS 77 sur ses interventions « feu de végétation ».
- **Date :** 2026-11-19
- **Auteurs :** décision du groupe (Aboubacrine, Iris, Daryl, Harold)

## 007 — G4 : comparer le 77 à l'Île-de-France seulement

- **Question :** G4, à niveau d'indice égal, le 77 a-t-il plus ou moins de feux que les autres départements ?
- **Manque :** pour comparer à toute la France, il faudrait les feux de la BDIFF de tous les départements. L'export du groupe ne couvre que la zone de défense Île-de-France (2024-2025).
- **Décision :** limiter la comparaison à l'Île-de-France.
- **Raison :** choix du groupe de rester sur notre région, celle de la commande.
- **Coût :** la partie « comment nous nous situons par rapport au reste du territoire national » de la commande reste sans réponse : c'est une limite à écrire. La comparaison régionale est fragile : 3 feux dans le 78 et le 91 sur 2024-2025, aucun dans le 95, et un nombre de feux inconnu pour 75, 92, 93 et 94 (BSPP).
- **Date :** 2026-11-19
- **Auteurs :** décision du groupe (Aboubacrine, Iris, Daryl, Harold)

## 008 — G2 : répondre sur la Météo des forêts, recommander un seuil sur le FWI Copernicus

- **Question :** G2, à partir de quel niveau déclencher le dispositif renforcé ?
- **Manque :** la Météo des forêts n'est archivée que depuis 2024 et n'est publiée que de juin à septembre. On ne peut la croiser avec les feux que sur 2024-2025, et le 77 n'y dépasse presque jamais le niveau 1. De plus, Météo-France précise que la Météo des forêts « n'est pas destinée aux services d'incendie et de secours » (« 10 questions pour comprendre la Météo des forêts », 2024).
- **Décision :** on répond à la question posée avec la Météo des forêts (notebook 01). En complément, on recommande un seuil sur le FWI de Copernicus (indice Forêt-Météo, le même que l'IFM utilisé par Météo-France), disponible toute l'année et sur plusieurs années.
  - Seuils candidats fixés d'avance : les bornes des classes EFFIS présentes dans le 77, 11,2 (début de « modéré ») et 21,3 (début d'« élevé »). Des valeurs intermédiaires sont montrées pour information seulement.
  - Valeur du 77 : moyenne des points de la grille, comparée au point le plus proche de Fontainebleau, où les feux sont concentrés.
  - Validation : quand 2016-2023 sera disponible (#46), calage sur 2016-2022 et test sur 2023-2025.
- **Raison :** dix saisons et toute l'année au lieu de deux étés ; un indice continu qui permet de comparer le coût (jours de déclenchement) et les deux erreurs pour chaque seuil ; un indice proche de l'outil opérationnel de Météo-France.
- **Coût :** le FWI Copernicus est une reconstitution après coup sur des points espacés d'environ 30 km, pas la prévision de la veille : un seuil trouvé sur Copernicus ne se transpose pas tel quel dans l'IFM opérationnel. Il faudra le présenter en termes relatifs et le faire traduire par Météo-France.
- **Date :** 2026-11-20
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)
