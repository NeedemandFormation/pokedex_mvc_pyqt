from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                           QStackedWidget, QPushButton, QVBoxLayout, 
                           QLabel, QHBoxLayout)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de QStackedWidget")
        self.setGeometry(100, 100, 400, 300)

        # Widget central qui contiendra tout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Création du layout principal
        layout = QVBoxLayout(central_widget)
        
        # Création des boutons de navigation
        button_layout = QHBoxLayout()
        btn_page1 = QPushButton("Page 1")
        btn_page2 = QPushButton("Page 2")
        btn_page3 = QPushButton("Page 3")
        
        button_layout.addWidget(btn_page1)
        button_layout.addWidget(btn_page2)
        button_layout.addWidget(btn_page3)
        button_layout.addStretch()
        
        # Création du QStackedWidget
        self.stack = QStackedWidget()
        
        # Création des pages
        page1 = QWidget()
        page1.setStyleSheet('background-color:lightblue;')
        page2 = QWidget()
        page2.setStyleSheet('background-color:lightgreen;')
        page3 = QWidget()
        page3.setStyleSheet('background-color:lightyellow;')
        
        # Configuration de la page 1
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QLabel("Contenu de la page 1"))
        
        # Configuration de la page 2
        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QLabel("Contenu de la page 2"))
        
        # Configuration de la page 3
        page3_layout = QVBoxLayout(page3)
        page3_layout.addWidget(QLabel("Contenu de la page 3"))
        
        # Ajout des pages au QStackedWidget
        self.stack.addWidget(page1)
        self.stack.addWidget(page2)
        self.stack.addWidget(page3)
        
        # Connexion des boutons aux changements de page
        btn_page1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn_page2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn_page3.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        
        # Ajout des layouts au layout principal
        layout.addLayout(button_layout)
        layout.addWidget(self.stack)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())