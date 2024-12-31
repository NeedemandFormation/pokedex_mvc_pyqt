from typing import List
from PyQt5.QtCore import QObject, pyqtSignal, Qt

from src.model.entities import Pokemon


class Signals(QObject):
    request_pokemons = pyqtSignal()  # Signal pour demander la liste
    pokemons_loaded  = pyqtSignal(list)  # Signal pour recevoir la liste
    error_occurred = pyqtSignal(str)  # Signal pour les erreurs
    pokemon_added = pyqtSignal(Pokemon)
    pokemons_level_up  = pyqtSignal(list)