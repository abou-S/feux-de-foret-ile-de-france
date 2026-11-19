# Glossaire — Île-de-France

Dernière mise à jour : 2026-11-19

Les termes sont classés par ordre alphabétique, une section par terme. Toute modification passe par un ticket et une pull request relue par le chef de projet. On ne supprime jamais un terme : on le marque « obsolète », avec la raison et la date.

## BSPP (Brigade de sapeurs-pompiers de Paris)

- **Définition :** service de pompiers militaires qui défend Paris et la petite couronne (75, 92, 93, 94). Il remplace le SDIS sur ces quatre départements.
- **Sources et colonnes :** Interventions SIS (ligne Numéro = « BSPP », Département = « Paris »). BDIFF (« nombre d'incendies inconnu » pour 75, 92, 93, 94 en 2025).
- **Divergences :** dans les interventions SIS, les quatre départements tiennent sur une seule ligne. Dans la Météo des forêts, ils ont chacun leur ligne, avec les mêmes niveaux.
- **Règle retenue :** à décider (voir décision 004 du journal).
- **Unité ou granularité :** un service, quatre départements.
- **Exemple :** interventions SIS 2024, BSPP : 223 feux de végétations pour Paris et la petite couronne.
- **Statut :** validé
- **Origine de la définition :** description du jeu « Interventions réalisées par les services d'incendie et de secours » sur data.gouv.fr.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

## Build-up Index (BUI / `fbupinx`) — Indice d'accumulation de sécheresse

- **Définition :** Indicateur combinant l'état d'humidité de la couche organique intermédiaire et celui des couches organiques profondes pour représenter l'accumulation de conditions favorables à la combustion.
- **Sources et colonnes :** Copernicus CEMS, jeu « Fire danger indices historical data », variable affichée Build-up index, variable technique dans les fichiers GRIB2 : `fbupinx`.
- **Divergences :** À distinguer du Drought Code et du Duff Moisture Code, qui décrivent séparément des couches de matières organiques. Aucune divergence entre sources vérifiée, car une seule source est retenue.
- **Règle retenue :** Proposition : garder cet indicateur séparé des deux composantes, sans les assimiler. Décision du groupe non prise ; lien vers le journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de la variable Build-up index sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Départ de feu

- **Définition :** le moment et l'endroit où un feu commence, même s'il est éteint tout de suite.
- **Sources et colonnes :** BDIFF (une ligne par incendie de forêt, « Date de première alerte »). Interventions SIS (« Feux de végétations », un total par département et par an).
- **Divergences :** la BDIFF ne compte que les incendies de forêt, avec la date et l'heure où l'info arrive au CODIS. Les interventions SIS comptent aussi les feux de champs ou de broussailles, sans date. Pour le 77, 55 feux dans la BDIFF en 2025 contre 225 feux de végétations dans le fichier SIS 2024 : deux années différentes, mais l'écart de définition est net.
- **Règle retenue :** à décider. Proposition : un départ de feu = une fiche de la BDIFF.
- **Unité ou granularité :** un feu, à la commune.
- **Exemple :** BDIFF, fiche 2025-694, Pont-Scorff (56), alerte le 01/01/2025 à 01h08.
- **Statut :** proposé
- **Origine de la définition :** page « Définitions » du portail BDIFF, puis proposition du groupe.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

## Département

- **Définition :** territoire identifié par un code (77 pour la Seine-et-Marne). Pour les pompiers, il peut aussi désigner le territoire d'un service d'incendie.
- **Sources et colonnes :** BDIFF (Département), Météo des forêts (num_dep, de 01 à 95 plus 2A et 2B), interventions SIS (Numéro, Département).
- **Divergences :** la Météo des forêts compte 96 départements, avec une ligne pour chacun des quatre départements de la BSPP. Les interventions SIS les regroupent sur une seule ligne « Paris ». Les codes sont du texte (`01`, `2B`), pas des nombres.
- **Règle retenue :** à décider.
- **Unité ou granularité :** un département.
- **Exemple :** 77 = Seine-et-Marne.
- **Statut :** à vérifier
- **Origine de la définition :** fichiers des trois sources, à confirmer avec le COG de l'INSEE.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

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

## Drought Code (DC / `drtcode`) — Indice de sécheresse profonde

- **Définition :** Indicateur de l'humidité présente dans les couches organiques profondes et compactes du sol forestier.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Drought code, variable technique dans les fichiers GRIB2 : `drtcode`.
- **Divergences :** À ne pas confondre avec le Duff Moisture Code, associé à une couche organique moins profonde. Aucune divergence entre producteurs étudiée.
- **Règle retenue :** Proposition : décrire la sécheresse profonde indépendamment de la sécheresse des couches intermédiaires. Lien vers une décision validée à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** .
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Drought code sur la fiche Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## Duff Moisture Code (DMC / `dufmcode`) — Indice d'humidité de la couche organique intermédiaire

- **Définition :** Indicateur de l'humidité de matières organiques forestières moyennement profondes et peu compactées, situées approximativement entre 5 et 10 cm de profondeur selon la description fournie.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Duff moisture code, variable technique dans les fichiers GRIB2 : `dufmcode`.
- **Divergences :** Ne caractérise pas la même couche que le Fine Fuel Moisture Code (combustibles superficiels) ou le Drought Code (couches profondes).
- **Règle retenue :** Proposition : utiliser le DMC pour la couche intermédiaire uniquement ; décision collective et lien au journal à ajouter.
- **Unité ou granularité :** Sans unité ; estimation quotidienne sur une grille géographique.
- **Exemple :** 
- **Statut :** à vérifier.
- **Origine de la définition :** Description de Duff moisture code sur la fiche Copernicus CEMS, complétée par l'extrait fourni dans la conversation.
- **Ajouté par :** Daryl William Fabo, 2026-11-17.

## `fdsrte` — Indice quotidien de sévérité des incendies

- **Définition :** Indice qui estime la difficulté potentielle à maîtriser un incendie selon les conditions de danger du jour.
- **Sources et colonnes :** Copernicus CEMS — `fdsrte`.
- **Divergences :** Aucune identifiée.
- **Règle retenue :** À définir.
- **Unité ou granularité :** Indice numérique sans unité, quotidien.
- **Exemple :** Valeur réelle non vérifiée.
- **Statut :** à vérifier
- **Origine de la définition :** Documentation Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-19.

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

## Feu de végétation

- **Définition :** feu qui touche de la végétation (forêt, mais aussi champs, broussailles, bords de route). Plus large qu'un feu de forêt.
- **Sources et colonnes :** Interventions SIS (« Feux de végétations »).
- **Divergences :** la BDIFF ne garde que les feux qui démarrent ou se propagent en forêt. Le fichier SIS ne définit pas la colonne, on ne sait pas ce qu'elle inclut.
- **Règle retenue :** à décider.
- **Unité ou granularité :** un nombre d'interventions par département et par an.
- **Exemple :** SIS 2024, Seine-et-Marne : 225.
- **Statut :** à vérifier
- **Origine de la définition :** déduite du nom de la colonne, pas confirmée par la documentation.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

## Fine Fuel Moisture Code (FFMC / `ffmcode`) — Indice d'humidité des combustibles fins

- **Définition :** Indicateur de l'humidité des éléments végétaux fins proches de la surface, comme les aiguilles, feuilles mortes et petites brindilles, qui peuvent s'enflammer rapidement.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Fine fuel moisture code, variable technique dans les fichiers GRIB2 : `ffmcode`.
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

## Fire Weather Index (FWI / `fwinx`) — Indice forêt-météo

- **Définition :** Indicateur météorologique synthétisant notamment la propagation initiale potentielle et l'accumulation de sécheresse pour décrire l'intensité potentielle d'un feu.
- **Sources et colonnes :** Copernicus CEMS, variable affichée Fire weather index, variable technique dans les fichiers GRIB2 : `fwinx`.
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

## `infsinx` — Indice de propagation initiale

- **Définition :** Indice qui estime la vitesse potentielle de propagation d'un incendie au début de son développement.
- **Sources et colonnes :** Copernicus CEMS — `infsinx`.
- **Divergences :** Aucune identifiée.
- **Règle retenue :** À définir.
- **Unité ou granularité :** Indice numérique sans unité, quotidien.
- **Exemple :** Valeur réelle non vérifiée.
- **Statut :** à vérifier
- **Origine de la définition :** Documentation Copernicus CEMS.
- **Ajouté par :** Daryl William Fabo, 2026-11-19.

## Jour avec feu

- **Définition :** jour où au moins un départ de feu a eu lieu dans le département.
- **Sources et colonnes :** BDIFF (« Date de première alerte », Département). Pas dans les sources : c'est un terme du groupe pour la question G2.
- **Divergences :** la date de la Météo des forêts est celle de la publication, en UTC. L'indice du lendemain est publié la veille. Il faut fixer à quel jour du feu on rattache quel niveau.
- **Règle retenue :** à décider (voir décision 002 du journal).
- **Unité ou granularité :** un jour × un département.
- **Exemple :** le 77 a un feu le 08/04/2025 (Le Vaudoué, 04h07) : jour avec feu.
- **Statut :** proposé
- **Origine de la définition :** proposition du groupe.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

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

## Niveau de danger (Météo des forêts)

- **Définition :** niveau de danger de feu prévu pour un département : 1 faible (vert), 2 modéré (jaune), 3 élevé (orange), 4 très élevé (rouge).
- **Sources et colonnes :** Météo des forêts (niveau_j1, niveau_j2).
- **Divergences :** la direction parle de « danger élevé » sans préciser le niveau : 3, ou 3 et 4 ? Le niveau tient compte de la forêt et des zones sensibles de chaque département : un niveau 3 n'a pas le même sens partout.
- **Règle retenue :** à décider.
- **Unité ou granularité :** un niveau de 1 à 4, par département et par jour.
- **Exemple :** Seine-et-Marne, 17/06/2026 : niveau 2.
- **Statut :** à vérifier (sens de niveau_j1 et niveau_j2 non confirmé par la documentation)
- **Origine de la définition :** présentation PDF de Météo-France, jointe au jeu « Archives de la Météo des forêts ».
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

## Saison de feux

- **Définition :** période de l'année où le risque de feu est suivi et où le dispositif peut être renforcé.
- **Sources et colonnes :** Météo des forêts (date), BDIFF (Date de première alerte).
- **Divergences :** la Météo des forêts est publiée à partir du 3 juin jusqu'en septembre (2024 et 2025), du 28/05 au 05/10 en 2026. Les feux du 77 en 2025 vont d'avril à novembre. La direction parle d'été, et aussi de printemps.
- **Règle retenue :** à décider.
- **Unité ou granularité :** une période de dates.
- **Exemple :** MdF 2025 : du 03/06/2025 au 30/09/2025.
- **Statut :** à vérifier
- **Origine de la définition :** fichiers des archives et présentation PDF de Météo-France.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

## Seuil de déclenchement

- **Définition :** niveau de la Météo des forêts à partir duquel le SDIS 77 met en place le dispositif renforcé (patrouilles, guet…).
- **Sources et colonnes :** aucune. Le seuil actuel n'est pas dans la commande.
- **Divergences :** les chefs de centre n'ont pas tous la même idée du niveau « élevé ».
- **Règle retenue :** à décider.
- **Unité ou granularité :** un niveau de 1 à 4.
- **Exemple :** non disponible.
- **Statut :** à vérifier
- **Origine de la définition :** mail de la direction du SDIS 77.
- **Ajouté par :** Aboubacrine Seck, 2026-11-17

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
