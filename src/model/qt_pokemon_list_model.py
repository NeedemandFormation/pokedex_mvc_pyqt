from PyQt5.QtCore import QAbstractListModel
from PyQt5.Qt import Qt



# Modèle de liste pour QListView Spécificité de PyQt
class PokemonListModel(QAbstractListModel):

    def __init__(self, pokemons = []):
        super().__init__()
        self.pokemons = pokemons
    
    def rowCount(self, parent):
        return len(self.pokemons)
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            pokemon = self.pokemons[index.row()]
            return pokemon.display() # Affichage personnalisé
        return None
    
    def update_data(self, new_pokemons):
        # Notifier le début du changement
        self.beginResetModel()
        self.pokemons = new_pokemons
        # Notifier la fin du changement
        self.endResetModel()

    def get_selected_items(self, selected_indexes):
        return [
                self.data(index, Qt.DisplayRole) for index in selected_indexes
        ]
    
    def get_selected_ids(self, selected_indexes):
        ids = list()
        for index in selected_indexes:
            pokemon = self.pokemons[index.row()]
            ids.append(pokemon.id)
        return ids;