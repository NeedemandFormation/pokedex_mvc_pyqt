# Pokedex - Sand box

Installation : 

```
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate     # Sur Windows
pip install -r requirements.txt
```


## Signal & Slot

Les signaux et slots connectent les événements (par exemple, clics) à des actions spécifiques.

**Signal** : Un signal est un événement émis par un objet lorsqu'une action spécifique se produit, comme un clic sur un bouton ou une modification de texte.
**Slot** : Un slot est une méthode ou une fonction qui est connectée à un signal. Quand le signal est émis, le slot est automatiquement exécuté.

Points importants

    - Un signal peut être connecté à plusieurs slots. Tous les slots seront appelés lorsque le signal est émis.
    - Un slot peut être connecté à plusieurs signaux.
    - Vous pouvez déconnecter un signal d’un slot à l’aide de disconnect() : obj.my_signal.disconnect(my_slot)
    - Les signaux et slots peuvent transmettre des données : Si un signal émet un argument, le slot doit l'accepter dans sa signature.

## Connection à une base de données

- mysql.connector : MySqlConnector is a C# ADO.NET driver for MySQL, MariaDB, Amazon Aurora, Azure Database for MySQL and other MySQL-compatible databases.
- SQLAlchemy est un ORM
- Sqlite3 SQBDR : Un système de gestion de base de données relationnelle (RDBMS) est un système de gestion de base de données (SGBD) qui est basé sur le modèle relationnel tel qu'il est introduit par E. F. Codd. La plus populaire des bases de données commerciales et open source actuellement en service est basée sur le modèle de base de données relationnelle. Une brève définition d'un SGBDR peut être un SGBD dans lequel les données sont stockées sous la forme de tableaux et la relation entre les données est également stockée sous la forme de tableaux.

## Modèle Qt

La bibliothèque PyQt réalise déjà une séparation entre la vue et les données. 
- La vue = widget
- les données = modèles Qt

Le modèle Qt dans PyQt est une architecture puissante utilisée pour gérer et afficher des données dans des widgets. Elle repose sur le paradigme Modèle-Vue (Model-View), qui sépare clairement les données (le modèle) et la manière dont elles sont présentées (la vue). Cela permet de créer des interfaces graphiques flexibles et réutilisables. 

La séparation du modèle et de la vue permet :

    La réutilisation des données avec plusieurs vues.
    Une indépendance entre les données et leur affichage.

### 2. Les modèles disponibles dans Qt

Qt fournit des modèles prédéfinis pour les cas courants :

    QStringListModel : Pour gérer une liste de chaînes.
    QStandardItemModel : Un modèle général pour les données structurées.
    QFileSystemModel : Pour naviguer dans le système de fichiers.
    QAbstractItemModel : Une classe de base pour créer des modèles personnalisés.

### 3. Les types de vues dans Qt

Les vues intégrées permettent d'afficher les données du modèle dans différents formats :

    QListView : Affiche les données sous forme de liste.
    QTableView : Affiche les données sous forme de tableau.
    QTreeView : Affiche les données sous forme d'arbre.
    QColumnView : Affiche les données dans une vue en colonnes.

### 4. Fonctionnement

    Connexion du Modèle et de la Vue : Une vue est connectée à un modèle via la méthode setModel().
    Modifications automatiques : Si les données du modèle changent, la vue est automatiquement mise à jour grâce aux signaux et slots de Qt.
    Édition des données : Les données peuvent être modifiées via la vue, et le modèle relaie ces modifications aux données sous-jacentes.

### 5. Création d'un modèle personnalisé

Pour des structures de données spécifiques, vous pouvez créer votre propre modèle en héritant de QAbstractListModel, QAbstractTableModel ou QAbstractItemModel. Les méthodes principales à implémenter sont :

    rowCount() : Nombre de lignes.
    columnCount() : Nombre de colonnes (pour les tableaux).
    data() : Retourne les données pour un index donné.
    setData() : (optionnel) Permet de modifier les données.
    headerData() : Retourne les en-têtes de colonnes ou de lignes.

Un modéle personalisé est utiliser lorsqu'on souhaite personnalisé l'affichage. ou manipuler des objets personalisés.