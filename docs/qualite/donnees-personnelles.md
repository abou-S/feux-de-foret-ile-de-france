# Les données personnelles

Dernière mise à jour : 2026-11-20

Une donnée personnelle est une information qui permet d'identifier une personne, directement (nom, adresse) ou indirectement (en croisant plusieurs informations). On a vérifié chaque source qu'on utilise.

## Source par source

| Source | Données personnelles ? | Détail |
|---|---|---|
| BDIFF | **Non dans nos données, mais un risque à surveiller** | Pas de nom, pas d'adresse, pas de coordonnées. Il existe trois colonnes sensibles : `Nombre de décès`, `Nombre de bâtiments totalement détruits`, `… partiellement détruits`. Pour nos 291 feux d'Île-de-France, elles valent 0 ou sont vides. Si un jour un feu avait un décès, la commune, le jour et l'heure exacte permettraient de retrouver la victime dans la presse |
| Météo des forêts | Non | un niveau par département et par jour |
| Copernicus | Non | des indices météorologiques sur une grille |
| Interventions SIS | Non | des totaux par département et par an |

## Ce qu'on a fait (minimisation)

- **Les colonnes décès et bâtiments ne sont pas chargées dans l'entrepôt.** Aucune de nos questions n'en a besoin : elles restent seulement dans le fichier brut.
- **Aucune donnée plus fine que la commune et le jour** n'arrive dans l'entrepôt.
- **Les comptes des contributeurs de la BDIFF** (nom, e-mail) existent dans l'application, mais ne sont pas dans l'export public.
- **Notre clé d'API Météo-France** n'est pas une donnée personnelle, mais c'est un secret : elle reste dans `data/.env`, ignoré par git.

## Conclusion

L'entrepôt ne contient **aucune donnée personnelle**. Toutes nos sources sont publiques, sous licence ouverte.

## À surveiller

- **Les relevés du SDIS 77** que nous allons demander pour 2026 (décision 002) pourraient contenir des données personnelles : adresses d'intervention, victimes, noms des agents. Avant de les charger, il faudra n'en garder que la date, la commune et le type de feu (minimisation), et ne jamais les déposer telles quelles dans le dépôt.
- **Si une source ajoutée contient des coordonnées précises de feux**, elles pourraient désigner une propriété privée : il faudra les ramener à la commune.
