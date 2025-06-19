from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
)
from modules import rsa_visualizer

class RSAVisualizerWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.generate_button = QPushButton("Generate RSA Keypair")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        layout.addWidget(QLabel("RSA Key Structure Visualizer"))
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        self.generate_button.clicked.connect(self.show_rsa_structure)

    def show_rsa_structure(self):
        rsa_info = rsa_visualizer.simulate_rsa_keygen()
        display = ""
        for label, value in rsa_info.items():
            display += f"{label}:\n{value}\n\n"
        self.result_area.setText(display)
