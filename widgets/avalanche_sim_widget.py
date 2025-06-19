from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from modules import avalanche_sim


class AvalancheSimWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        self.sim_button = QPushButton("Simulate Avalanche Effect")

        layout.addWidget(QLabel("Input Text 1"))
        layout.addWidget(self.input1)
        layout.addWidget(QLabel("Input Text 2"))
        layout.addWidget(self.input2)
        layout.addWidget(self.sim_button)
        layout.addWidget(QLabel("Result"))
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        self.sim_button.clicked.connect(self.run_simulation)

    def run_simulation(self):
        text1 = self.input1.text()
        text2 = self.input2.text()

        if not text1 or not text2:
            QMessageBox.warning(self, "Input Error", "Please enter both input values.")
            return

        result = avalanche_sim.simulate_avalanche(text1, text2)
        display = (
            f"Hash 1:\n{result['hash1']}\n\n"
            f"Hash 2:\n{result['hash2']}\n\n"
            f"Bit Differences: {result['bit_diff']} of 256 bits"
        )
        self.result_area.setText(display)
