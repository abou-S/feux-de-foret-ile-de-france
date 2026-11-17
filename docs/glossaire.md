# Glossaire — Île-de-France

Dernière mise à jour : 2026-11-17

Les termes sont classés par ordre alphabétique, une section par terme. Toute modification passe par un ticket et une pull request relue par le chef de projet. On ne supprime jamais un terme : on le marque « obsolète », avec la raison et la date.

## Build-up Index (BUI) — Indice d'accumulation de sécheresse

- **Définition :** Indicateur combinant l'état d'humidité de la couche organique intermédiaire et celui des couches organiques profondes pour représenter l'accumulation de conditions favorables à la combustion.
- **Sources et colonnes :** Copernicus CEMS, jeu « Fire danger indices historical data », variable affichée Build-up index. Nom technique de variable dans les fichiers : à vérifier.
- **Divergences :** À distinguer du Drought Code et du Duff Moisture Code, qui décrivent séparément des couches de matières organiques. Aucune divergence entre sources vérifiée, car une seule source est retenue.
- **Règle retenue :** Proposition : garder cet indicateur séparé des deux composantes, sans les assimiler. Décision du groupe non prise ; lien vers le journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de la variable Build-up index sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Dispositif renforcé

- **Définition :** Ensemble des moyens supplémentaires de surveillance et de prévention mentionnés dans la commande du SDIS, notamment les patrouilles et le guet.
- **Sources et colonnes :** Message de commande du SDIS transmis dans le projet ; aucune variable correspondante identifiée dans le jeu Copernicus CEMS.
- **Divergences :** La commande ne précise ni le nombre de personnes et d'engins engagés, ni les actions nécessaires pour qu'un dispositif soit considéré comme « renforcé ».
- **Règle retenue :** À décider avec le groupe et le SDIS : établir les critères d'activation et les moyens inclus. Lien vers la décision à ajouter au journal.
- **Unité ou granularité :** À définir (activation par jour, département ou secteur ; moyens humains et matériels).
- **Exemple :**  « patrouilles » et le « guet » ; 
- **Statut :** à vérifier.
- **Origine de la définition :** Message de commande du SDIS transmis au groupe ; non défini par Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Drought Code (DC) — Indice de sécheresse profonde

- **Définition :** Indicateur de l'humidité présente dans les couches organiques profondes et compactes du sol forestier.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Drought code. Nom technique dans le fichier : à vérifier.
- **Divergences :** À ne pas confondre avec le Duff Moisture Code, associé à une couche organique moins profonde. Aucune divergence entre producteurs étudiée.
- **Règle retenue :** Proposition : décrire la sécheresse profonde indépendamment de la sécheresse des couches intermédiaires. Lien vers une décision validée à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** .
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Drought code sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Duff Moisture Code (DMC) — Indice d'humidité de la couche organique intermédiaire

- **Définition :** Indicateur de l'humidité de matières organiques forestières moyennement profondes et peu compactées, situées approximativement entre 5 et 10 cm de profondeur selon la description fournie.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Duff moisture code. Nom technique dans le fichier : à vérifier.
- **Divergences :** Ne caractérise pas la même couche que le Fine Fuel Moisture Code (combustibles superficiels) ou le Drought Code (couches profondes).
- **Règle retenue :** Proposition : utiliser le DMC pour la couche intermédiaire uniquement ; décision collective et lien au journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Duff moisture code sur la fiche Copernicus CEMS, complétée par l'extrait fourni dans la conversation.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Feu de forêt

- **Définition :** Incendie touchant une zone forestière.
- **Sources et colonnes :** Message de commande du SDIS ;
- **Divergences :** Le SDIS parle de « départs de feu », tandis que la fiche Copernicus décrit des conditions favorables aux incendies ; ces notions ne désignent pas la même mesure.
- **Règle retenue :** À décider : préciser quels incendies et départs de feu entrent dans le comptage. Lien vers la décision du journal à ajouter.
- **Unité ou granularité :** Événement individuel (proposé) ; critères de dénombrement à confirmer.
- **Exemple :** .
- **Statut :** à vérifier.
- **Origine de la définition :** Formulation de la commande du SDIS ; limites établies à partir de l'objet du jeu Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Fine Fuel Moisture Code (FFMC) — Indice d'humidité des combustibles fins

- **Définition :** Indicateur de l'humidité des éléments végétaux fins proches de la surface, comme les aiguilles, feuilles mortes et petites brindilles, qui peuvent s'enflammer rapidement.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Fine fuel moisture code. Nom technique dans le fichier : à vérifier.
- **Divergences :** Mesure un compartiment de combustible plus superficiel que le Duff Moisture Code et le Drought Code.
- **Règle retenue :** Proposition : réserver ce terme à l'état des combustibles fins superficiels, sans l'utiliser comme nombre de départs de feu. Décision et lien au journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Fine fuel moisture code sur la fiche Copernicus CEMS et extrait détaillé fourni dans la conversation.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Fire Danger Index (FDI) — Indice de danger d'incendie

- **Définition :** Indicateur synthétique associé aux conditions favorables à l'apparition d'un feu et à sa propagation ; il ne compte pas les incendies réellement survenus.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Fire danger index. Nom technique dans le fichier : à vérifier.
- **Divergences :** Ne doit pas être assimilé au Fire Weather Index ou aux catégories de la Météo des forêts sans vérifier leurs méthodes et échelles respectives.
- **Règle retenue :** Proposition : utiliser le nom complet FDI pour éviter les confusions avec FWI ; comparaison des seuils à décider et documenter dans le journal.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** .
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Fire danger index sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Fire Weather Index (FWI) — Indice forêt-météo

- **Définition :** Indicateur météorologique synthétisant notamment la propagation initiale potentielle et l'accumulation de sécheresse pour décrire l'intensité potentielle d'un feu.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Fire weather index. Nom technique dans le fichier : à vérifier.
- **Divergences :** Le FWI est une valeur d'indice ; il ne doit pas être confondu avec un incendie constaté ni être directement interprété comme l'un des niveaux de la Météo des forêts sans règle de correspondance validée.
- **Règle retenue :** Proposition : conserver le FWI numérique comme indicateur distinct ; modalités d'éventuelle catégorisation à décider. Lien vers le journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Fire weather index sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Indice

- **Définition :** Valeur calculée à partir de conditions météorologiques et/ou de l'état des combustibles, destinée à représenter une dimension du danger d'incendie.
- **Sources et colonnes :** Commande du SDIS (« indice ») ; fiche Copernicus CEMS présentant plusieurs indices, dont FDI et FWI. Aucune colonne générique unique « indice » identifiée.
- **Divergences :** Dans la commande, le mot peut renvoyer aux niveaux annoncés par la Météo des forêts ; dans Copernicus, il désigne plusieurs variables numériques distinctes.
- **Règle retenue :** À décider : toujours nommer l'indice utilisé et son échelle dans les analyses. Lien vers la décision du journal à ajouter.
- **Unité ou granularité :** Dépend de l'indice ; FDI et FWI sont affichés sans unité, à résolution quotidienne et spatiale quadrillée.
- **Exemple :**
- **Origine de la définition :** Message du SDIS et intitulés des variables de Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Météo des forêts

- **Définition :** Information utilisée par le SDIS pour qualifier le niveau de danger d'incendie
- **Sources et colonnes :** Message du SDIS ; aucune variable intitulée « Météo des forêts » dans le jeu Copernicus CEMS retenu.
- **Divergences :** La Météo des forêts citée par le SDIS et les indices météorologiques Copernicus ne doivent pas être traités comme identiques sans correspondance démontrée.
- **Règle retenue :** À décider : déterminer l'indicateur opérationnel exact et les niveaux utilisés par le SDIS, puis consigner la décision dans le journal.
- **Unité ou granularité :** Niveau de danger par territoire et période ; échelle opérationnelle précise à vérifier.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Message de commande du SDIS ; absence de définition équivalente identifiée sur la fiche Copernicus.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Spread Component (SC) — Composante de propagation

- **Définition :** Indicateur de la vitesse potentielle de propagation du front principal d'un incendie.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Spread component. Nom technique dans le fichier : à vérifier.
- **Divergences :** Décrit une propagation potentielle, et non la vitesse effectivement observée lors d'un incendie ; à distinguer aussi du Fire Weather Index, plus synthétique.
- **Règle retenue :** Proposition : l'utiliser exclusivement comme indicateur de propagation potentielle. Décision et lien vers le journal à ajouter.
- **Unité ou granularité :** Sans unité selon la fiche Copernicus ; estimation quotidienne sur une grille géographique.
- **Exemple :** Aucune valeur réelle inspectée ; à compléter après consultation des observations.
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Spread component sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.



## Dispositif renforcé

- **Définition :** Ensemble des moyens supplémentaires de surveillance et de prévention mentionnés dans la commande du SDIS, notamment les patrouilles et le guet.
- **Sources et colonnes :** Message de commande du SDIS transmis dans le projet ; aucune variable correspondante identifiée dans le jeu Copernicus CEMS.
- **Divergences :** La commande ne précise ni le nombre de personnes et d'engins engagés, ni les actions nécessaires pour qu'un dispositif soit considéré comme « renforcé ».
- **Règle retenue :** À décider avec le groupe et le SDIS : établir les critères d'activation et les moyens inclus. Lien vers la décision à ajouter au journal.
- **Unité ou granularité :** À définir (activation par jour, département ou secteur ; moyens humains et matériels).
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Message de commande du SDIS transmis au groupe ; non défini par Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Drought Code (DC) — Indice de sécheresse profonde

- **Définition :** Indicateur de l'humidité présente dans les couches organiques profondes et compactes du sol forestier.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Drought code. Nom technique dans le fichier : à vérifier.
- **Divergences :** À ne pas confondre avec le Duff Moisture Code, associé à une couche organique moins profonde. Aucune divergence entre producteurs étudiée.
- **Règle retenue :** Proposition : décrire la sécheresse profonde indépendamment de la sécheresse des couches intermédiaires. Lien vers une décision validée à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Drought code sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Duff Moisture Code (DMC) — Indice d'humidité de la couche organique intermédiaire

- **Définition :** Indicateur de l'humidité de matières organiques forestières moyennement profondes et peu compactées, situées approximativement entre 5 et 10 cm de profondeur selon la description fournie.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Duff moisture code. Nom technique dans le fichier : à vérifier.
- **Divergences :** Ne caractérise pas la même couche que le Fine Fuel Moisture Code (combustibles superficiels) ou le Drought Code (couches profondes).
- **Règle retenue :** Proposition : utiliser le DMC pour la couche intermédiaire uniquement ; décision collective et lien au journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Duff moisture code sur la fiche Copernicus CEMS, complétée par l'extrait fourni dans la conversation.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.




