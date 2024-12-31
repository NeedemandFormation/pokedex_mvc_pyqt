from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QListView, QPushButton
from dataclasses import dataclass
from typing import List
from PyQt5.QtCore import QAbstractListModel

# Modèle de données
@dataclass
class Pokemon:
    id: int
    name: str
    types: List[str]

# Signals centralisés
class Signals(QObject):
    request_pokemons = pyqtSignal()  # Signal pour demander la liste
    pokemons_loaded = pyqtSignal(list)  # Signal pour recevoir la liste
    error_occurred = pyqtSignal(str)  # Signal pour les erreurs

# Vue
class PokemonListView(QMainWindow):
    def __init__(self, signals):
        super().__init__()
        self.signals = signals
        self.setup_ui()
        
        # Connexion des signaux
        self.signals.pokemons_loaded.connect(self.on_pokemons_loaded)
        self.signals.error_occurred.connect(self.on_error)
    
    def setup_ui(self):
        self.setWindowTitle("Liste des Pokémons")
        main_widget = QWidget()
        layout = QVBoxLayout()
        
        # Bouton pour demander le rechargement
        self.refresh_button = QPushButton("Rafraîchir la liste")
        self.refresh_button.clicked.connect(self.request_pokemons)
        
        # Liste
        self.pokemon_list = QListView()
        self.pokemon_list.setModel(PokemonListModel([]))
        
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.pokemon_list)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
    
    def request_pokemons(self):
        self.refresh_button.setEnabled(False)
        self.signals.request_pokemons.emit()
    
    def on_pokemons_loaded(self, pokemons):
        self.pokemon_list.setModel(PokemonListModel(pokemons))
        self.refresh_button.setEnabled(True)
    
    def on_error(self, message):
        self.refresh_button.setEnabled(True)
        # Ici vous pourriez afficher une boîte de dialogue d'erreur

# Modèle de liste pour QListView
class PokemonListModel(QAbstractListModel):
    def __init__(self, pokemons):
        super().__init__()
        self.pokemons = pokemons
    
    def rowCount(self, parent):
        return len(self.pokemons)
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            pokemon = self.pokemons[index.row()]
            return f"{pokemon.id:03d} - {pokemon.name}"

# Contrôleur
class PokemonController:
    def __init__(self):
        self.signals = Signals()
        self.view = PokemonListView(self.signals)
        
        # Connexion du signal de requête
        self.signals.request_pokemons.connect(self.load_pokemons)
    
    def load_pokemons(self):
        try:
            # Simulation d'un chargement de données
            # Dans un cas réel, ceci pourrait être un appel API ou DB
            pokemons = [
                Pokemon(1, "Bulbizarre", ["Plante", "Poison"]),
                Pokemon(4, "Salamèche", ["Feu"]),
                Pokemon(7, "Carapuce", ["Eau"])
            ]
            
            # Émet le signal avec les données chargées
            self.signals.pokemons_loaded.emit(pokemons)
            
        except Exception as e:
            # En cas d'erreur, émet le signal d'erreur
            self.signals.error_occurred.emit(str(e))

# Point d'entrée
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    controller = PokemonController()
    controller.view.show()
    sys.exit(app.exec())