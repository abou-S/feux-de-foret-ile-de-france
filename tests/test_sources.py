from pipeline.sources import lire_bdiff, lire_meteo_des_forets

ENTETE_BDIFF = 'Année;Numéro;Département;"Code INSEE";"Date de première alerte"'
LIGNES_BDIFF = ['2025;694;"77";"77186";"2025-04-01 13:33:40"', '2025;695;"77";"77333";"2025-05-02 10:00:00"']


def ecrire(chemin, lignes):
    chemin.write_text('\n'.join(lignes) + '\n', encoding='utf-8')
    return chemin


def test_lire_bdiff_deux_lignes_info(tmp_path):
    f = ecrire(tmp_path / 'a.csv', ['"Nombre d\'incendies : 2"', '"Critères de sélection =>"', ENTETE_BDIFF, *LIGNES_BDIFF])
    df = lire_bdiff(f)
    assert list(df.columns) == ['Année', 'Numéro', 'Département', 'Code INSEE', 'Date de première alerte']
    assert len(df) == 2
    assert df.loc[0, 'Département'] == '77'


def test_lire_bdiff_trois_lignes_info(tmp_path):
    f = ecrire(tmp_path / 'b.csv', ['"Certaines données sont associées à l\'ancienne version"', '"Nombre"', '"Critères"',
                                    ENTETE_BDIFF, *LIGNES_BDIFF])
    df = lire_bdiff(f)
    assert len(df) == 2
    assert df.loc[1, 'Numéro'] == '695'


def test_lire_mdf_virgule_dep_nom(tmp_path):
    f = ecrire(tmp_path / 'mdf_2025.csv', ['date,num_dep,niveau_j1,niveau_j2,dep_nom', '2025-06-03T14:50:06Z,1,1,1,Ain'])
    df = lire_meteo_des_forets(f)
    assert list(df.columns) == ['date', 'num_dep', 'niveau_j1', 'niveau_j2', 'nom_dep']


def test_lire_mdf_point_virgule(tmp_path):
    f = ecrire(tmp_path / 'mdf_2026.csv', ['date;num_dep;niveau_j1;niveau_j2;nom_dep', '2026-05-28T14:50:07Z;01;1;1;Ain'])
    df = lire_meteo_des_forets(f)
    assert list(df.columns) == ['date', 'num_dep', 'niveau_j1', 'niveau_j2', 'nom_dep']
    assert df.loc[0, 'num_dep'] == '01'


def test_lire_mdf_espaces(tmp_path):
    f = ecrire(tmp_path / 'mdf_x.csv', ['date                , num_dep, niveau_j1, niveau_j2, dep_nom',
                                       '2025-06-03T14:50:06Z,  1 ,         1,         1, Ain'])
    df = lire_meteo_des_forets(f)
    assert list(df.columns) == ['date', 'num_dep', 'niveau_j1', 'niveau_j2', 'nom_dep']
    assert df.loc[0, 'num_dep'] == '1'
    assert df.loc[0, 'nom_dep'] == 'Ain'
