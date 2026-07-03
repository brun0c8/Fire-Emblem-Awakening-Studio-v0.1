from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget
)

from core.file import GameFile


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fire Emblem Awakening Studio")

        self.info = QLabel("Nenhum arquivo aberto.")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.button = QPushButton("Abrir arquivo")
        self.button.clicked.connect(self.open_file)

        layout = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addWidget(self.info)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def open_file(self):

        filename, _ = QFileDialog.getOpenFileName(self)

        if not filename:
            return

        file = GameFile(filename)

        text = []

        text.append(f"Arquivo: {filename}")
        text.append(f"Tamanho: {file.size} bytes")
        text.append(f"Extensão: {file.extension}")
        text.append("")
        text.append("Magic:")
        text.append(file.magic(32).hex(" "))

        if file.is_lz11():
            text.append("")
            text.append("✔ Arquivo LZ11 detectado.")

        self.info.setText(file.path.name)
        self.output.setPlainText("\n".join(text))
