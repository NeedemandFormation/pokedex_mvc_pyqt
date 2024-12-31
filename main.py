import sys
from PyQt5.QtWidgets import QApplication
from src.controller import Controller

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
     
        # Controleur
        controller = Controller()  
        controller.view.show()


        sys.exit(app.exec_())
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
      