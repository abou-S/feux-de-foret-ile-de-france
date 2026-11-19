# pipeline/

Le code qui consolide les sources en trois couches :

- **bronze** : les fichiers bruts, tels qu'ils ont été téléchargés ou exportés ;
- **silver** : les données nettoyées, typées et harmonisées, après les règles de qualité ;
- **gold** : les tables prêtes pour les indicateurs (un feu, un jour × un département).

Les données produites vont dans `data/`. À compléter quand le modèle de l'entrepôt sera validé.
