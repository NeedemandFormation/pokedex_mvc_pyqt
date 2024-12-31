from PyQt5.QtWidgets import QMainWindow, QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListView, QMessageBox
from PyQt5.Qt import Qt
from src.model.entities import Pokemon
from src.model.qt_pokemon_list_model import PokemonListModel
from src.signals import Signals
from src.view.components.message_error_box import MessageErrorBox
from src.view.components.custom_button import CustomButton


class MainWindow(QMainWindow):
        
    def __init__(self, signals : Signals):
        super().__init__()
        self.setWindowTitle("Liste des Pokémons")
        self.setGeometry(100, 100, 800, 600) # x, y, width, height
        self.main_layout = QVBoxLayout() 
        self.signals = signals  # Sigla et Slot de PyQt
        
        # principaux composants en attributs      
        self.model = PokemonListModel() # extends de QtModel
        self.pokemon_name_input = QLineEdit()
        self.pokemon_type_input = QLineEdit()
        self.pokemon_level_input = QLineEdit()
        
        # Création du widget central
        central_widget = QWidget() 
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.main_layout)
 
        self.init_ui()
    
    def init_ui(self):
        
        # Form
        form_layout =  QFormLayout()       
        form_layout.addRow(QLabel("Nom:"), self.pokemon_name_input)
        form_layout.addRow(QLabel("Type:"), self.pokemon_type_input)
        form_layout.addRow(QLabel("Niveau:"), self.pokemon_level_input)
        self.main_layout.addLayout(form_layout)

        # les boutons
        button_layout = QHBoxLayout()
        btn_add = CustomButton("Ajouter Pokémon")
        btn_add.clicked.connect(self.slot_add_pokemon)
        button_layout.addWidget(btn_add)
        btn_up = CustomButton("Level Up")
        btn_up.clicked.connect(self.slot_level_up)
        button_layout.addWidget(btn_up)
        self.main_layout.addLayout(button_layout)
       
        # List
        pokemon_list_view = QListView()
        pokemon_list_view.setModel(self.model) # attache à notre model Qt
        pokemon_list_view.setSelectionMode(QListView.MultiSelection) # Permettre la sélection multiple
        self.main_layout.addWidget(pokemon_list_view) 
        
    def slot_level_up(self):
        """Affiche les éléments sélectionnés dans une boîte de dialogue."""
        selection_model = self.model.parent().selectionModel()  # Accès au sélectionneur depuis le modèle
        selected_indexes = selection_model.selectedIndexes()
        if selected_indexes:
            selected_ids = self.model.get_selected_ids(selected_indexes)
            self.signals.pokemons_level_up.emit(selected_ids)
        else:
            QMessageBox.information(self, "Aucune sélection", "Aucun élément sélectionné.")


    def slot_add_pokemon(self):
        """Les slots peuvent être définie dans le controleur ou dans la vue
        """
        pokemon = Pokemon()
        pokemon.name = self.pokemon_name_input.text()
        pokemon.type = self.pokemon_type_input.text()
        pokemon.level = self.pokemon_level_input.text()
        
        if pokemon.is_valid():  # Vérification des champs
            self.signals.pokemon_added.emit(pokemon)  # Émet le signal avec les données => Voir controller
            self.pokemon_name_input.clear()  # Réinitialise le champ
            self.pokemon_type_input.clear()  # Réinitialise le champ
        else:
            error_box = MessageErrorBox("Veuillez remplir tous les champs.",self)
            error_box.exec_()


