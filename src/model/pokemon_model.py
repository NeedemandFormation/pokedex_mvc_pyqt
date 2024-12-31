from dataclasses import dataclass
import sqlite3
from typing import List
from PyQt5.Qt import Qt
from .entities import Pokemon
from persistance.db_sqlite import DBSqlite


# La classe model qui contient les requetes SQL
class PokemonModel: 
    
    def __init__(self) -> None:
        co = DBSqlite.get_connection()
        self.connection = co
    
    def get_all(self) -> List[Pokemon]:
        """Recupère tous les pokemeons

        Returns:
            List[Pokemon]: Liste de pokemon
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, nom, type, niveau FROM pokemons")
        out = [
            Pokemon(id=ligne[0], name=ligne[1], type=ligne[2], level=ligne[3]) 
            for ligne in cursor.fetchall()
        ]
        cursor.close()
        return out

    def level_up(self, id_pokemon):
        """Monter d'un niveau

        Args:
            id_pokemon (int): identifiant
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE pokemons SET niveau = niveau + 1 WHERE id = ?", (id_pokemon,))
        self.connection.commit()
        cursor.close()

    def add(self, pokemon: Pokemon) -> Pokemon:
        """AJoute un pokemon a la base de données

        Args:
            pokemon (Pokemon): entité Pokemon

        Returns:
            Pokemon: Pokemon avec un id autoincrémenté
        """
        
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO pokemons (nom, type, niveau) VALUES (?, ?, ?)", 
            (pokemon.name, pokemon.type, pokemon.level)
        )
        self.connection.commit()
        pokemon.id = cursor.lastrowid
        cursor.close()
        return pokemon



