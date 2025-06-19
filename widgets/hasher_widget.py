from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
from modules import hasher

class HasherWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_edit = QLineEdit()
        self.algos = QComboBox()
        self.algos.addItems(hasher.get_supported_algorithms())
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.hash_button = QPushButton("Hash")

        layout.addWidget(QLabel("Input Text:"))
        layout.addWidget(self.input_edit)
        layout.addWidget(QLabel("Hash Algorithm:"))
        layout.addWidget(self.algos)
        layout.addWidget(self.hash_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_area)

        self.setLayout(layout)
        self.hash_button.clicked.connect(self.run_hash)

    def run_hash(self):
        text = self.input_edit.text()
        algo = self.algos.currentText()
        result = hasher.hash_string(text, algorithm=algo)
        self.output_area.setText(result)
