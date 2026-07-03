import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.resize(900, 700)
window.show()

app.exec()
