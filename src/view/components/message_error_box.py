from PyQt5.QtWidgets import QMessageBox


class MessageErrorBox(QMessageBox):

    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Critical)   # Icône d'erreur
        self.setWindowTitle("Erreur")        # Titre par défaut
        self.setText(message)                # Message d'erreur
        self.setStandardButtons(QMessageBox.Ok)  # Bouton OK par défaut

    @staticmethod
    def show_error(message, parent=None):
        """Affiche une boîte de dialogue d'erreur directement."""
        error_box = MessageErrorBox(message, parent)
        error_box.exec_()
