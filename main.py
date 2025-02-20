import sys

from PyQt6.QtWidgets import QApplication
from menu import MainWindow

if __name__ == "__main__":  # Запуск
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
