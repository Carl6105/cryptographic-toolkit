from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from modules.visualizer import simulate_diffie_hellman

class VisualizationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.button = QPushButton("Simulate Diffie-Hellman Key Exchange")

        layout.addWidget(self.button)
        layout.addWidget(QLabel("Step-by-step Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.button.clicked.connect(self.simulate)

    def simulate(self):
        steps = simulate_diffie_hellman()
        self.output.setPlainText("\n".join(steps))
