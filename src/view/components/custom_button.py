from PyQt5.QtWidgets import QPushButton

class CustomButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setup_style()

    def setup_style(self):
        """Appliquer un style personnalisé au bouton."""
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5e87;
            }
        """)

    def set_loading_state(self, is_loading):
        """Changer l'état pour indiquer qu'une action est en cours."""
        if is_loading:
            self.setText("Chargement...")
            self.setEnabled(False)
        else:
            self.setText("Valider")
            self.setEnabled(True)
