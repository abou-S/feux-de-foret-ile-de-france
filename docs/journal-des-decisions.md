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

## 005 — G5 : vérifier Copernicus avant de décider

- **Question :** G5, quelles conditions météo sont associées aux feux ?
- **Manque :** la Météo des forêts ne donne que le niveau de 1 à 4. Les variables détaillées seraient dans Copernicus, mais aucun fichier n'a été ouvert (cellules « inconnu »).
- **Décision :** vérifier d'abord (ouvrir un fichier Copernicus, noter l'avis de suspension des mises à jour du 16/11/2026), puis choisir entre approximer et renoncer.
- **Raison :** on ne décide pas sur des cellules « inconnu ».
- **Coût :** G5 reste en attente. Si Copernicus est inexploitable dans le temps du projet, on renonce à G5 ou on se limite au niveau de synthèse.
- **Date :** 2026-11-17
- **Auteurs :** Aboubacrine Seck (proposition, à valider par le groupe)
