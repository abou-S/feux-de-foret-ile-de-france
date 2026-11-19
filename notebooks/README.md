# notebooks/

L'étude des données, question par question. Un notebook par question, numéroté :

- `01_etude_g2_seuil.ipynb`
- `02_etude_g3_indice_bas.ipynb`
- …

Règles :
- les notebooks lisent les données dans `../data/`, jamais ailleurs ;
- un notebook sert à explorer et comprendre. Ce qu'on garde (nettoyage, jointures) passe ensuite dans `pipeline/` ;
- ne jamais afficher le contenu de `data/.env` dans une cellule : les résultats sont enregistrés dans le notebook et partent sur GitHub.

Environnement : `source .venv/bin/activate`, puis choisir le noyau `.venv` dans VS Code.
