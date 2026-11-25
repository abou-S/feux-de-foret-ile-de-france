import pandas as pd

from pipeline.gold import calendrier, departements, points_meteo, feux_de_foret, suivi_journalier_departement, danger_journalier_point_meteo

J = pd.Timestamp


def feux(lignes):
    """lignes : (id, annee, date, departement, insee)"""
    return pd.DataFrame([{'id_feu': i, 'annee': a, 'date': J(d), 'code_departement': dep, 'code_insee': insee,
                          'commune': 'X', 'surface_m2': 10.0, 'precision_surface': 'Estimées', 'cause': None}
                         for i, a, d, dep, insee in lignes],
                        columns=['id_feu', 'annee', 'date', 'code_departement', 'code_insee', 'commune', 'surface_m2',
                                 'precision_surface', 'cause'])


def mdf(lignes):
    """lignes : (date_concernee, departement, niveau)"""
    return pd.DataFrame([{'date_concernee': J(d), 'code_departement': dep, 'nom_departement': 'Nom ' + dep,
                          'niveau_j1': n} for d, dep, n in lignes],
                        columns=['date_concernee', 'code_departement', 'nom_departement', 'niveau_j1']).astype({'niveau_j1': 'Int64'})


def cop_points(lignes):
    """lignes : (date, departement, fwi). Les autres indices valent fwi + 1 (ffmc) ... fwi + 5 (bui)."""
    return pd.DataFrame([{'date': J(d), 'code_departement': dep, 'commune': 'P', 'latitude': 48.0 + k,
                          'longitude': 2.0, 'fwi': f, 'ffmc': f + 1, 'dmc': f + 2, 'dc': f + 3, 'isi': f + 4,
                          'bui': f + 5} for k, (d, dep, f) in enumerate(lignes)],
                        columns=['date', 'code_departement', 'commune', 'latitude', 'longitude',
                                 'fwi', 'ffmc', 'dmc', 'dc', 'isi', 'bui'])


VIDE_POINTS = cop_points([])


def test_nb_feux_bspp_inconnu():
    t = suivi_journalier_departement(mdf([('2025-07-01', '92', 1)]), VIDE_POINTS, feux([('2025-1', 2025, '2025-07-01', '77', '77186')]))
    assert t.loc[t['code_departement'] == '92', 'nb_feux'].isna().all()


def test_nb_feux_annee_sans_bdiff():
    t = suivi_journalier_departement(mdf([('2026-07-01', '77', 1)]), VIDE_POINTS, feux([('2025-1', 2025, '2025-07-01', '77', '77186')]))
    ligne = t[(t['date'] == J('2026-07-01')) & (t['code_departement'] == '77')]
    assert ligne['nb_feux'].isna().all()


def test_nb_feux_zero():
    t = suivi_journalier_departement(mdf([('2025-07-02', '77', 1)]), VIDE_POINTS, feux([('2025-1', 2025, '2025-07-01', '77', '77186')]))
    ligne = t[(t['date'] == J('2025-07-02')) & (t['code_departement'] == '77')]
    assert ligne['nb_feux'].tolist() == [0]


def test_feux_tous_rattaches():
    f = feux([('2025-1', 2025, '2025-07-01', '77', 'a'), ('2025-2', 2025, '2025-07-01', '77', 'b'),
              ('2025-3', 2025, '2025-07-01', '77', 'c')])
    t = suivi_journalier_departement(mdf([('2025-07-01', '77', 2)]), cop_points([('2025-07-01', '77', 12.0)]), f)
    ligne = t[(t['date'] == J('2025-07-01')) & (t['code_departement'] == '77')]
    assert ligne['nb_feux'].tolist() == [3]
    assert t['nb_feux'].sum() == 3


def test_seulement_ile_de_france():
    t = suivi_journalier_departement(mdf([('2025-07-01', '77', 1), ('2025-07-01', '13', 3)]), VIDE_POINTS, feux([]))
    assert set(t['code_departement']) == {'77'}


def test_niveau_vide_hors_saison():
    f = feux([('2025-1', 2025, '2025-04-10', '77', '77186')])
    t = feux_de_foret(f, mdf([('2025-07-01', '77', 2)]), cop_points([('2025-04-10', '77', 8.0)]))
    assert t['niveau_mdf_j1'].isna().all()
    assert t['fwi_departement'].tolist() == [8.0]


def test_fwi_departement_est_la_moyenne_des_points():
    f = feux([('2025-1', 2025, '2025-07-01', '77', '77186')])
    t = feux_de_foret(f, mdf([]), cop_points([('2025-07-01', '77', 10.0), ('2025-07-01', '77', 20.0)]))
    assert t['fwi_departement'].tolist() == [15.0]


def test_fwi_max():
    t = suivi_journalier_departement(mdf([]), cop_points([('2025-07-01', '77', 10.0), ('2025-07-01', '77', 20.0)]), feux([]))
    assert t['fwi_max'].tolist() == [20.0]
    assert t['fwi_moyen'].tolist() == [15.0]


def test_moyenne_et_max_de_chaque_indice():
    """Chaque indice a sa moyenne (nom court, comme avant) et son max sur les points du département."""
    t = suivi_journalier_departement(mdf([]), cop_points([('2025-07-01', '77', 10.0), ('2025-07-01', '77', 20.0)]), feux([]))
    ligne = t.iloc[0]
    for k, indice in enumerate(['ffmc', 'dmc', 'dc', 'isi', 'bui'], start=1):
        assert ligne[indice] == 15.0 + k
        assert ligne[f'{indice}_max'] == 20.0 + k


def test_colonnes_existantes_en_premier():
    """Les nouvelles colonnes sont ajoutées à la fin : Power BI lit les 12 premières sans changement."""
    t = suivi_journalier_departement(mdf([('2025-07-01', '77', 1)]), VIDE_POINTS, feux([]))
    assert list(t.columns) == ['date', 'code_departement', 'niveau_mdf_j1', 'fwi_moyen', 'fwi_max', 'ffmc', 'dmc', 'dc',
                               'isi', 'bui', 'nb_feux', 'jour_avec_feu',
                               'ffmc_max', 'dmc_max', 'dc_max', 'isi_max', 'bui_max']


def test_departements_bspp():
    d = departements(mdf([('2025-07-01', '77', 1), ('2025-07-01', '92', 1)]))
    assert d.set_index('code_departement').loc['92', 'service'] == 'BSPP'
    assert not d.set_index('code_departement').loc['92', 'feux_connus']
    assert d.set_index('code_departement').loc['77', 'feux_connus']


def test_calendrier_saison():
    m = mdf([('2025-07-01', '77', 1)])
    t = suivi_journalier_departement(m, cop_points([('2025-04-01', '77', 1.0), ('2025-07-01', '77', 1.0)]), feux([]))
    d = calendrier(t, feux_de_foret(feux([]), m, VIDE_POINTS), m).set_index('date')
    assert d.loc[J('2025-07-01'), 'saison_indice'] and not d.loc[J('2025-04-01'), 'saison_indice']
    assert d.loc[J('2025-04-01'), 'mois'] == 4



def test_jour_avec_feu():
    f = feux([('2025-1', 2025, '2025-07-01', '77', 'a')])
    t = suivi_journalier_departement(mdf([('2025-07-01', '77', 1), ('2025-07-02', '77', 1), ('2025-07-01', '92', 1)]),
                              VIDE_POINTS, f).set_index(['date', 'code_departement'])
    assert t.loc[(J('2025-07-01'), '77'), 'jour_avec_feu'] == True
    assert t.loc[(J('2025-07-02'), '77'), 'jour_avec_feu'] == False
    assert pd.isna(t.loc[(J('2025-07-01'), '92'), 'jour_avec_feu'])   # BSPP : inconnu, pas « non »


def test_points_meteo():
    p = cop_points([('2025-07-01', '77', 10.0), ('2025-07-01', '77', 20.0)])
    p = pd.concat([p, p.assign(date=J('2025-07-02'))])
    d = points_meteo(p)
    assert list(d.columns) == ['id_point', 'latitude', 'longitude', 'commune', 'code_departement']
    assert len(d) == 2 and d['id_point'].is_unique


def test_danger_journalier_point_meteo():
    p = cop_points([('2025-07-01', '77', 10.0), ('2025-07-01', '77', 20.0)])
    f = danger_journalier_point_meteo(p)
    assert list(f.columns) == ['date', 'id_point', 'fwi', 'ffmc', 'dmc', 'dc', 'isi', 'bui']
    assert sorted(f['fwi'].tolist()) == [10.0, 20.0]
    assert sorted(f['bui'].tolist()) == [15.0, 25.0]
    assert set(f['id_point']) <= set(points_meteo(p)['id_point'])


def test_calendrier_sans_trou():
    """Power BI exige des jours consécutifs pour une table de dates."""
    f = feux([('2016-1', 2016, '2016-03-22', '77', 'a')])
    m = mdf([('2025-07-01', '77', 1)])
    s = suivi_journalier_departement(m, VIDE_POINTS, f)
    c = calendrier(s, feux_de_foret(f, m, VIDE_POINTS), m)
    attendu = pd.date_range('2016-01-01', '2025-12-31')
    assert c['date'].tolist() == list(attendu)
