# Fiches indicateurs

Une fiche par objectif (voir `kpi/objectifs.md`). Chacun remplit **sa** fiche sur sa propre branche, sans toucher aux autres sections. La section « Jeu d'indicateurs v0 » est remplie en groupe, à la mise en commun.

---

## Fiche G1 — Concentration géographique des feux — Aboubacrine

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---

## Fiche G2 — Seuil de déclenchement — Aboubacrine

Indicateur : **taux de jours d'alerte sans feu**.

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | Question G2 : pour chaque niveau de la Météo des forêts, quelle part des jours a eu au moins un départ de feu dans le 77 ? Objectif : d'ici la fin de l'été 2027, faire passer de [a %] à [b %] la part des jours de niveau ≥ N où aucun feu ne part, sans augmenter la part des feux qui partent les jours de niveau < N |
| Formule : numérateur | Nombre de jours où le niveau prévu pour le 77 est ≥ N et où aucun départ de feu n'a eu lieu dans le 77 |
| Formule : dénominateur | Nombre de jours où le niveau prévu pour le 77 est ≥ N, sur la période couverte par l'indice |
| Unité | % de jours |
| Paramètres | N, le seuil (2, 3 ou 4). Fixés d'avance : l'échéance (`niveau_j1`, la prévision faite la veille pour le lendemain, puisque c'est la veille que le SDIS décide) et la définition d'un feu (une fiche BDIFF) |
| Périmètre, période, granularité, fréquence | Seine-et-Marne. Saisons de l'indice (juin à septembre) où l'indice et les feux existent tous les deux : 2024 et 2025. Un jour pour le 77. Calcul mensuel pendant la saison, bilan en fin de saison |
| Source et champs | Météo des forêts, archives data.gouv.fr (`mdf_2024.csv`, `mdf_2025.csv`) : `date`, `num_dep`, `niveau_j1`. BDIFF, export CSV du portail : `Date de première alerte`, `Département`. Jointure : département + jour |
| Lignes utilisables | Météo des forêts 77 : 120 / 120 en 2024, 120 / 120 en 2025. BDIFF 77 2025 : 55 / 55 (aucune fiche marquée « données partielles »), dont 30 pendant la saison de l'indice. BDIFF 2024 : pas encore ouverte de mon côté, à reprendre de l'export d'Iris (2016-2025) |
| Proxy et biais | Voir ci-dessous |
| Décision éclairée | Taux élevé : beaucoup de jours déclenchés pour rien, on relève N, à condition que le garde-fou (feux les jours < N) n'augmente pas. Taux faible : N peut rester, ou baisser si le budget le permet |
| Propriétaire | Calcul : Aboubacrine. Relecture : responsable qualité et conformité |

**Proxy et biais**

| Terme sans champ | Proxy utilisé | Biais | Sens |
|---|---|---|---|
| « Aucun feu ne part » | Aucune fiche BDIFF ce jour-là dans le 77 | La BDIFF ne garde que les feux de forêt. Un petit feu de champ ou un départ éteint tout de suite peut ne pas y être | Surestime les jours sans feu, donc le taux |
| « Le jour concerné par le niveau » | `date` de publication + 1 jour pour `niveau_j1` | Déduit, pas écrit dans la documentation de Météo-France. Si c'est faux, tous les feux sont décalés d'un jour | Sens inconnu |
| « Le jour du feu » | `Date de première alerte` | Un feu qui dure plusieurs jours n'est rattaché qu'à son premier jour | Surestime un peu les jours sans feu |

### Changer un paramètre

On fait passer N de 3 (« élevé », le « danger élevé » de la commande) à 2 (« modéré »).

**Ce qui change :**
- **Le dénominateur :** les jours de niveau 2 sont ajoutés. Dans le 77, on passe de 1 jour (2025, et aucun en 2024) à 22 jours (2025, toujours aucun en 2024).
- **La lisibilité :** avec N = 3, un seul jour : le taux vaut 0 % ou 100 %, il ne veut rien dire. Avec N = 2, il devient calculable.
- **Le garde-fou :** avec N = 3, tous les feux des jours de niveau 2 comptent comme « hors alerte ». Avec N = 2, beaucoup moins.
- **La décision :** avec N = 2, un taux élevé pousse à remonter à 3. Avec N = 3, on ne peut rien conclure, faute de jours.
- **Le coût :** N = 2 déclenche le dispositif beaucoup plus souvent.

**Ce qui ne change pas :** la formule, l'unité, la source et les champs, le grain (un jour pour le 77), la période, la définition d'un feu.

### RACER

| Critère | Jugement |
|---|---|
| Relevant | Oui : il mesure directement ce que l'objectif veut faire baisser, les jours où le dispositif est déclenché pour rien |
| Accepted | À confirmer avec le SDIS : la définition d'un feu (une fiche BDIFF = un feu de forêt) et la valeur de N. Les termes « jour avec feu » et « niveau de danger » sont encore « à vérifier » dans le glossaire |
| Credible | Oui si N, l'échéance et la définition d'un feu sont écrits dans la fiche avant le calcul. Deux personnes liront alors la même chose : un taux élevé veut dire beaucoup d'alertes sans feu |
| Easy | Oui pour le calcul : deux CSV publics et une jointure par jour. Non pour le suivi de 2027 : la BDIFF ne publie qu'avec un an de retard, il faudra les relevés du SDIS |
| Robust | Faible tel quel : très peu de jours de niveau élevé dans le 77, et il peut être détourné en changeant N. Voir garde-fous ci-dessous |

### Détournement, garde-fou, risque résiduel

- **Détournement :** celui qui fixe le seuil monte N à 4. Il ne reste que les jours les plus secs, où il y a plus souvent un feu : le taux baisse et l'objectif semble atteint. En réalité, le dispositif n'est presque plus déclenché, et les feux partent sans lui.
- **Garde-fou :** le **taux de feux partis les jours de niveau < N** (nombre de feux un jour de niveau < N / nombre de feux pendant la saison de l'indice). Il compte des feux, pas des jours : il monte justement quand on monte N. C'est la condition de notre objectif. On affiche aussi le **nombre de jours de niveau ≥ N** à côté du taux, avec un **seuil plancher** : sous [k] jours (k à fixer), on ne lit pas le taux.
- **Risque résiduel :** un jour d'alerte sans feu n'est pas forcément une fausse alerte. Les patrouilles et le guet ont pu empêcher un feu. Aucun des deux garde-fous ne le voit : un dispositif efficace donne l'air d'un mauvais seuil.

### Pre-mortem

Dans un an, l'indicateur a fait prendre une mauvaise décision au SDIS. Les raisons plausibles, de la plus probable et grave à la moins probable :

| Rang | Raison | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | Le seuil a été fixé sur trop peu de jours (2 saisons, 1 seul jour de niveau 3 dans le 77) : le résultat tenait au hasard d'un été | Haute | Haute | Seuil plancher de jours, volume affiché à côté du taux, recalcul à chaque saison |
| 2 | Le dispositif a empêché des feux, ses jours sont passés pour de fausses alertes, et on a relevé N à tort | Moyenne | Haute | Contrôle par échantillon : pour quelques jours d'alerte sans feu, demander au SDIS si une patrouille est intervenue |
| 3 | Le niveau a été rattaché au mauvais jour (décalage d'un jour entre la publication et le feu) | Moyenne | Moyenne | Pas de garde-fou pour l'instant : à confirmer auprès de Météo-France |

---

## Fiche G3 — Feux des jours d'indice bas — Harold

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---

## Fiche G4 — Comparaison avec les autres départements — Iris

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---

## Fiche G5 — Indices météo détaillés (Copernicus) — Daryl

### Fiche d'indicateur

| Rubrique | Valeur |
|---|---|
| Question et objectif | |
| Formule : numérateur | |
| Formule : dénominateur | |
| Unité | |
| Paramètres | |
| Périmètre, période, granularité, fréquence | |
| Source et champs | |
| Lignes utilisables | |
| Proxy et biais | |
| Décision éclairée | |
| Propriétaire | |

### Changer un paramètre

### RACER

| Critère | Jugement |
|---|---|
| Relevant | |
| Accepted | |
| Credible | |
| Easy | |
| Robust | |

### Détournement, garde-fou, risque résiduel

### Pre-mortem

---

## Jeu d'indicateurs v0 (groupe)

| Rôle | Indicateur | Objectif | Raison |
|---|---|---|---|
| KPI principal | | | |
| KPI secondaire | | | |
| Garde-fou | | | |
| Contexte | | | |
| Écarté | | | |
