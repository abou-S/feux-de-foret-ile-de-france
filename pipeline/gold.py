"""Couche gold : schéma en étoile propre pour Power BI (Île-de-France seulement, décision 007).

Gold ne contient que des données préparées (nettoyées, reliées au bon grain). L'analyse (seuils,
menu par budget, taux) se fait dans Power BI."""
import numpy as np
import pandas as pd

DEP_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
DEP_BSPP = ['75', '92', '93', '94']  # nombre de feux inconnu dans la BDIFF (décision 007)
INDICES = ['ffmc', 'dmc', 'dc', 'isi', 'bui']


def departements(mdf: pd.DataFrame) -> pd.DataFrame:
    d = (mdf[mdf['code_departement'].isin(DEP_IDF)][['code_departement', 'nom_departement']]
         .drop_duplicates('code_departement').rename(columns={'nom_departement': 'nom'}))
    d['service'] = np.where(d['code_departement'].isin(DEP_BSPP), 'BSPP', 'SDIS')
    d['feux_connus'] = ~d['code_departement'].isin(DEP_BSPP)
    return d.sort_values('code_departement').reset_index(drop=True)


def communes(feux: pd.DataFrame) -> pd.DataFrame:
    return (feux[['code_insee', 'commune', 'code_departement']].drop_duplicates('code_insee')
            .rename(columns={'commune': 'nom'}).sort_values('code_insee').reset_index(drop=True))


def suivi_journalier_departement(mdf: pd.DataFrame, cop_dep: pd.DataFrame, cop_points: pd.DataFrame,
                          feux: pd.DataFrame) -> pd.DataFrame:
    """Un jour × un département d'Île-de-France : niveau, indices, nombre de feux."""
    niveau = (mdf[mdf['code_departement'].isin(DEP_IDF)]
              .rename(columns={'date_concernee': 'date', 'niveau_j1': 'niveau_mdf_j1'})[['date', 'code_departement', 'niveau_mdf_j1']])
    indices = (cop_dep[cop_dep['code_departement'].isin(DEP_IDF)]
               .rename(columns={'fwi': 'fwi_moyen'})[['date', 'code_departement', 'fwi_moyen', *INDICES]])
    fwi_max = (cop_points[cop_points['code_departement'].isin(DEP_IDF)]
               .groupby(['date', 'code_departement'], as_index=False)['fwi'].max().rename(columns={'fwi': 'fwi_max'}))

    t = niveau.merge(indices, on=['date', 'code_departement'], how='outer')
    t = t.merge(fwi_max, on=['date', 'code_departement'], how='left')

    compte = feux.groupby(['date', 'code_departement']).size().rename('n').reset_index()
    t = t.merge(compte, on=['date', 'code_departement'], how='left')
    connu = t['date'].dt.year.isin(set(feux['annee'])) & ~t['code_departement'].isin(DEP_BSPP)
    t['nb_feux'] = pd.array(np.where(connu, t['n'].fillna(0), np.nan), dtype='Float64').astype('Int64')
    t['jour_avec_feu'] = (t['nb_feux'] > 0).astype('boolean')  # vide quand nb_feux est inconnu

    colonnes = ['date', 'code_departement', 'niveau_mdf_j1', 'fwi_moyen', 'fwi_max', *INDICES, 'nb_feux', 'jour_avec_feu']
    return t[colonnes].sort_values(['date', 'code_departement']).reset_index(drop=True)


def feux_de_foret(feux: pd.DataFrame, mdf: pd.DataFrame, cop_dep: pd.DataFrame) -> pd.DataFrame:
    """Un feu, avec le niveau de la Météo des forêts et le FWI de son département ce jour-là (vides si inconnus)."""
    niveau = mdf.rename(columns={'date_concernee': 'date', 'niveau_j1': 'niveau_mdf_j1'})[['date', 'code_departement', 'niveau_mdf_j1']]
    fwi = cop_dep.rename(columns={'fwi': 'fwi_departement'})[['date', 'code_departement', 'fwi_departement']]
    t = (feux.merge(niveau, on=['date', 'code_departement'], how='left')
         .merge(fwi, on=['date', 'code_departement'], how='left'))
    t['niveau_mdf_j1'] = t['niveau_mdf_j1'].astype('Int64')
    colonnes = ['id_feu', 'date', 'code_insee', 'code_departement', 'surface_m2', 'precision_surface', 'cause',
                'niveau_mdf_j1', 'fwi_departement']
    return t[colonnes].sort_values(['date', 'id_feu']).reset_index(drop=True)


def calendrier(suivi: pd.DataFrame, feux: pd.DataFrame, mdf: pd.DataFrame) -> pd.DataFrame:
    # Tous les jours, du 1er janvier de la première année au 31 décembre de la dernière : Power BI exige une table
    # de dates sans trou pour la marquer comme « table de dates ».
    toutes = pd.concat([suivi['date'], feux['date']])
    dates = pd.Series(pd.date_range(f'{toutes.min().year}-01-01', f'{toutes.max().year}-12-31'))
    saison = set(mdf['date_concernee'])
    return pd.DataFrame({'date': dates.values, 'annee': dates.dt.year.values, 'mois': dates.dt.month.values,
                         'saison_indice': dates.isin(saison).values})



def _id_point(latitude: pd.Series, longitude: pd.Series) -> pd.Series:
    return latitude.map('{:.3f}'.format) + '_' + longitude.map('{:.3f}'.format)


def points_meteo(cop_points: pd.DataFrame) -> pd.DataFrame:
    """Un point de la grille Copernicus (environ 30 km d'écart), avec sa commune et son département."""
    d = cop_points[cop_points['code_departement'].isin(DEP_IDF)][['latitude', 'longitude', 'commune', 'code_departement']]
    d = d.drop_duplicates(['latitude', 'longitude']).copy()
    d.insert(0, 'id_point', _id_point(d['latitude'], d['longitude']))
    return d.sort_values('id_point').reset_index(drop=True)


def danger_journalier_point_meteo(cop_points: pd.DataFrame) -> pd.DataFrame:
    """Un jour × un point de la grille : le FWI. Permet à Power BI d'étudier un point précis (ex. près de Fontainebleau)."""
    p = cop_points[cop_points['code_departement'].isin(DEP_IDF)]
    f = pd.DataFrame({'date': p['date'], 'id_point': _id_point(p['latitude'], p['longitude']), 'fwi': p['fwi']})
    return f.sort_values(['date', 'id_point']).reset_index(drop=True)
