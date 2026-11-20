# Couche bronze : provenance des fichiers

Les fichiers de ce dossier sont les copies brutes des sources. **On ne les modifie jamais** (pas d'ouverture avec « Align » ou « Format » dans VS Code, pas d'enregistrement depuis Excel). Le pipeline les lit, et écrit ses résultats ailleurs (`data/silver/`, `data/gold/`).

Pour vérifier qu'un fichier n'a pas été modifié : `shasum -a 256 <fichier>`, à comparer avec l'empreinte ci-dessous.

| Fichier | Source | Comment il a été obtenu | Date d'extraction | Empreinte SHA-256 |
|---|---|---|---|---|
| `bdiff/incendies_idf_2024_2025.csv` | BDIFF, https://bdiff.agriculture.gouv.fr/incendies | Export CSV manuel du portail. Critères : date de première alerte du 01/01/2024 au 31/12/2025, zone de défense Île-de-France, type de feu F (forêt). Fichier `Incendies.csv` du zip, seulement renommé | 2026-11-19 | `b99caf12729e420fcc23c939f4ac57d3b035f977e2b5850ba01cc899eb43cd6c` |
| `bdiff/Incendies_2016_2025.csv` | BDIFF, https://bdiff.agriculture.gouv.fr/incendies | Export CSV manuel du portail. Critères : date de première alerte du 01/01/2016 au 31/12/2025, zone de défense Île-de-France, type de feu F. 291 feux (251 dans le 77). **3 lignes d'information** avant l'en-tête (dont un avertissement sur l'ancienne version du formulaire). **C'est le fichier BDIFF de référence** : il contient aussi tous les feux de `incendies_idf_2024_2025.csv` (vérifié, identiques) | 2026-11-20 | `8b17fab3b900b3864a4117742a06ea7186b1300dd5be19816086d4763f6f680b` |
| `meteo_des_forets/mdf_2024.csv` | Archives de la Météo des forêts, Météo-France (data.gouv.fr) | Téléchargement de https://meteofrance.s3.sbg.io.cloud.ovh.net/data/BULLETIN/MDF/mdf_2024.csv.gz, décompressé | 2026-11-19 | `53c1b0d89633afd3dbae17004affca64998654d77db7047e0abd607a8f2d6568` |
| `meteo_des_forets/mdf_2025.csv` | Idem | Idem, `mdf_2025.csv.gz` | 2026-11-19 | `383c34692ed322c5ef14ef8b5c02c7b03d07c08a060eeeda2a98f0586313e15a` |
| `meteo_des_forets/mdf_2026.csv` | Idem | Idem, `mdf_2026.csv.gz` | 2026-11-19 | `5542af01679987c277edb49ccaf6651dc0b7dd6e1f76a91c152b1fd0a8dc05b3` |

## Ce qu'il faut savoir avant de les lire

- **BDIFF :** séparateur `;`, encodage UTF-8, **2 ou 3 lignes d'information avant l'en-tête** selon l'export : chercher la ligne qui commence par `Année;`. Utiliser `Incendies_2016_2025.csv` ; `incendies_idf_2024_2025.csv` est gardé pour l'historique. Les départements 75, 92, 93 et 94 (BSPP) n'ont aucune ligne : leur nombre de feux est inconnu, ce n'est pas 0 (voir décision 007).
- **Météo des forêts :** le format change selon l'année.
  - 2024 : séparateur `,`, colonne `nom_dep`.
  - 2025 : séparateur `,`, colonne `dep_nom`.
  - 2026 : séparateur `;`, colonne `nom_dep`.
  - Dans les trois, `num_dep` n'a pas de zéro devant (`1` et non `01`), et `date` est l'heure de publication en UTC.
- **Licences :** Licence Ouverte v2.0 (fiches data.gouv.fr). Aucune donnée personnelle.

## Mettre à jour un fichier

On ajoute un nouveau fichier daté plutôt que d'écraser l'ancien, et on ajoute une ligne à ce tableau.
