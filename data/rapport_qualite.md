# Rapport de qualité

| Règle | Table | Décision | Lignes en échec | Résultat |
|---|---|---|---|---|
| id_feu unique | feux | bloquer | 0 | réussite |
| date d'alerte et département renseignés | feux | bloquer | 0 | réussite |
| département en Île-de-France | feux | alerter | 0 | réussite |
| surface ≥ 0 (sinon rejet) | feux | alerter | 0 | réussite |
| un seul niveau par (jour, département) | meteo_des_forets | bloquer | 0 | réussite |
| niveau entre 1 et 4 | meteo_des_forets | bloquer | 0 | réussite |
| même nombre de départements chaque jour, aucun jour manquant dans la saison | meteo_des_forets | alerter | 0 | réussite |
| un seul enregistrement par (jour, département) et par (jour, point) | copernicus | bloquer | 0 | réussite |
| FWI ≥ 0 (sinon rejet) | copernicus | alerter | 0 | réussite |
