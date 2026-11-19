# Fiche source - BDIFF (Base de Données sur les Incendies de Forêts en France)

Explorée par : Aboubacrine Seck, le 17/11/2026

Liens :
- Portail : https://bdiff.agriculture.gouv.fr/
- Page de consultation et d'export : https://bdiff.agriculture.gouv.fr/incendies
- Définitions : https://bdiff.agriculture.gouv.fr/aide/definitions
- Fiche data.gouv.fr : https://www.data.gouv.fr/datasets/base-de-donnees-sur-les-incendies-de-forets-en-france-bdiff

Fichier ouvert : export CSV de la campagne 2025, France entière (le choix par défaut du portail). Le zip contient `Incendies.csv`, `Définitions.pdf` et `Mention légales.pdf`.

| Rubrique | Valeur |
|---|---|
| Propriétaire et système | Ministère de l'Agriculture et de la Souveraineté Alimentaire. L'application a été conçue et développée par l'IGN, et l'IGN est l'organisation qui publie la fiche sur data.gouv.fr. Les données sont saisies par un réseau de contributeurs (SDIS, DDT(M), DRAAF…) qui doivent avoir un compte. Depuis 2023, la BDIFF a fusionné avec Prométhée (l'ancien outil de l'aire méditerranéenne). |
| Mode d'accès (export, API, téléchargement) et format | Portail web : on filtre (localisation, dates, heures, surfaces, période glissante) puis on clique sur « Télécharger : CSV ». On récupère un zip avec un CSV en UTF-8, séparateur `;`. Attention, le CSV commence par 2 lignes d'information (nombre d'incendies et critères de sélection) avant la ligne des noms de colonnes. data.gouv.fr indique le format « api », mais la ressource est juste un lien vers le portail, je n'ai pas trouvé d'API documentée. |
| Grain (une ligne = ?) | Un incendie de forêt (une « fiche incendie »), avec son numéro, son année, sa commune de départ et sa date et heure de première alerte. |
| Emprise géographique | France entière : métropole et DOM (on voit du 972 dans la synthèse). La localisation la plus fine dans l'export est la commune de départ du feu (code INSEE), il n'y a pas de coordonnées. |
| Période réellement couverte par les données | Le portail dit « depuis 2006 », jusqu'à l'année précédant l'année en cours. Dans le fichier que j'ai ouvert, j'ai vérifié seulement la campagne 2025 (dates d'alerte du 01/01/2025 au 31/12/2025). Les années 2006 à 2024 n'ont pas été vérifiées dans un fichier. La fiche data.gouv.fr affiche une couverture « 2006 à 2022 », ce qui n'est plus à jour par rapport au portail. Attention aussi : les définitions des surfaces ont changé en 2023, donc les surfaces avant et après 2023 ne se comparent pas directement. |
| Date de dernière mise à jour affichée sur la fiche | Fiche data.gouv.fr : dernière mise à jour le 13/12/2025. Le portail BDIFF n'affiche pas de date de mise à jour des données (seulement la version de l'application, v6.4.7). |
| Fréquence de mise à jour | Annuelle d'après data.gouv.fr : une campagne devient publique l'année suivante. Le portail précise que des campagnes passées peuvent être modifiées après coup à la demande des DDT(M) ou DRAAF (un message l'indique alors sous le tableau). |
| Volumétrie | Campagne 2025 : 2 541 incendies, soit 2 541 lignes et 24 colonnes, environ 300 Ko pour le CSV. Pour la Seine-et-Marne en 2025 : 55 incendies, environ 3,7 ha parcourus au total. Le volume total 2006-2025 n'a pas été vérifié (je n'ai exporté qu'une année). |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Code INSEE de la commune (avec le COG, la surface boisée par commune, etc.), Département (avec la Météo des forêts, qui est départementale), Date de première alerte (jour + heure, pour croiser avec l'indice du même jour). Année + Numéro identifient une fiche incendie. |
| Données personnelles | Pas de nom ni d'adresse dans l'export. Il y a par contre le nombre de décès et de bâtiments détruits, avec la commune et l'heure exacte du feu : en croisant avec la presse, on pourrait parfois retrouver un événement et les personnes touchées. À signaler au responsable qualité et conformité. Les données des comptes utilisateurs (contributeurs) existent dans l'application mais ne sont pas dans l'export. |
| Licence | Licence Ouverte v2.0 (Etalab), d'après la fiche data.gouv.fr. Les mentions légales du portail ne parlent pas de licence de réutilisation, elles parlent seulement du RGPD pour les comptes. |
| Questions de votre analyse auxquelles elle pourrait répondre | Q1 (concentration des feux par commune) : oui, c'est la source principale, avec la commune et la surface de chaque feu. Q2 et Q3 (part des jours avec feu par niveau d'indice, par secteur) : oui en partie. La BDIFF donne le jour de chaque feu, mais il faut la croiser avec l'historique de la Météo des forêts, et le découpage en secteurs du 77 n'y est pas. Q4 (comparaison avec l'Île-de-France et la France) : en partie seulement. La surface boisée n'y est pas, et pour 2025 le portail affiche « nombre d'incendies inconnu » pour le 75, le 92, le 93 et le 94 (territoire de la BSPP). |

## Ce que j'ai remarqué en ouvrant le fichier

- Seulement les feux de forêt. La BDIFF définit un incendie de forêt comme un feu qui « démarre en forêt ou qui se propage en forêt ou au sein de terres boisées ». Les feux de champs ou de broussailles qui ne touchent pas de forêt ne sont donc pas dedans. C'est une divergence à mettre dans le glossaire (« feu de forêt » / « départ de feu »).
- Beaucoup de petits feux. En 2025 dans le 77, les exemples font 40 à 200 m². 55 feux pour 3,7 ha au total, donc la plupart sont des départs vite maîtrisés.
- Les feux du 77 en 2025 vont d'avril à novembre (avril 11, mai 9, juin 13, juillet 11, août 8, octobre 2, novembre 1). Le printemps compte autant que l'été, ce qui rejoint la remarque de la direction sur le printemps.
- Colonnes peu remplies. La nature (cause) est vide pour 1 136 feux sur 2 541. Quatre colonnes de surface sont vides pour toutes les lignes en 2025. Elles servent sans doute à l'ancien modèle d'avant 2023, à vérifier.
- 70 fiches sur 2 541 sont marquées « Données partielles ou non valides ».
- Les départements de la petite couronne n'ont aucune ligne. Pour 78, 91 et 95 il y a très peu de feux (2, 3 et 0 en 2025), donc la comparaison régionale sera fragile.
