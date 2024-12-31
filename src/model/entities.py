
from dataclasses import dataclass


@dataclass
class Pokemon:
    id: int = None
    name: str = None
    type: str = None
    level: int = 1

    def is_valid(self)->bool:
        """Est ce que les attributs du pokemon sont valides

        Returns:
            bool: True si les attributs sont valides
        """
        verdict = True
        verdict &= bool(self.name)   
        verdict &= bool(self.type)  # Vérifie si le type est valide
        verdict &= isinstance(self.level, int) and self.level >= 0  # Vérifie level
        return verdict
    
    def display(self) -> str:
        """Retourne une affichage pour un pokemon

        Returns:
            str: chaine contenant les informations du pokemon
        """
        return f"ID: {self.id}, Nom: {self.name}, Type: {self.type}, Niveau: {self.level}"
