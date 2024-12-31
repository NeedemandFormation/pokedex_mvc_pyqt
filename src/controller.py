from typing import List
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from src.model import PokemonModel
from src.model import PokemonListModel
from src.view.main_window import MainWindow
from src.model.entities import Pokemon
from src.signals import Signals

class Controller() : 

    def __init__(self):
        self.signals = Signals()
        self.model = PokemonModel()
        self.view = MainWindow(self.signals)  
             
        self.slot_load_pokemons()
        # Connexion des models
        self.signals.request_pokemons.connect(self.slot_load_pokemons)
        self.signals.pokemon_added.connect(self.slot_add_pokemon)
        self.signals.pokemons_level_up.connect(self.slot_level_up)

    def slot_level_up(self, list : List[int]):
        """Slot pour level up

        Args:
            list (List[int]): Liste d'identifiant
        """
        try:
            for id in list:
                self.model.level_up(id)
            self.signals.request_pokemons.emit()
        except Exception as e:
            print(f"Erreur lors du level up : {e}")
        
    def slot_add_pokemon(self,pokemon : Pokemon):
        """Slot pour l'ajout d'un pokemon en bdd

        Args:
            pokemon (Pokemon): Pokemon à ajouter
        """
        try:
            self.model.add(pokemon)
        except Exception as e:
            print(f"Erreur lors de l'ajout : {e}")

    def slot_load_pokemons(self):
        """Chargement des pokemons
        """
        try:
            # Simulation d'un chargement
            pokemons =self.model.get_all()
            self.view.model.update_data(pokemons)            
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")


    


