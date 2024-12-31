import sqlite3
from sqlite3 import Connection
from typing import Optional

class DBSqlite:

    _connection : Optional[Connection] = None

    @classmethod
    def get_connection(cls): 
        if cls._connection is None:
            cls._connection = sqlite3.connect("persistance/pokedex.db")
            cls.create_tables()
            cls.insert_initial()
        return cls._connection

    @classmethod
    def create_tables(cls):
        co = cls.get_connection()
        cursor = co.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                type TEXT,
                niveau INTEGER,
                UNIQUE(nom) ON CONFLICT IGNORE
            )
        ''')
        cursor.close()
        co.commit

    @classmethod
    def insert_initial(cls):
        co = cls.get_connection()
        cursor = co.cursor()
        initial_data = [
            ("Pikachu", "Électrique", 25),
            ("Bulbizarre", "Plante", 15),
            ("Salamèche", "Feu", 20)
        ]
        cursor.executemany("INSERT OR IGNORE INTO pokemons (nom, type, niveau) VALUES (?, ?, ?)", initial_data)
        cursor.close()
        co.commit()

    @classmethod
    def fermer(cls):
        """Ferme la connexion à la base de données"""
        if cls._connection is not None:
            cls._connexion.close()

