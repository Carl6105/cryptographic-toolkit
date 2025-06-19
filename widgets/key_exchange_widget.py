from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
)
from modules import key_exchange_chat


class KeyExchangeWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.steps_area = QTextEdit()
        self.steps_area.setReadOnly(True)

        self.simulate_button = QPushButton("Simulate Diffie-Hellman Key Exchange")

        layout.addWidget(QLabel("Diffie-Hellman Key Exchange Simulator"))
        layout.addWidget(self.simulate_button)
        layout.addWidget(QLabel("Exchange Steps"))
        layout.addWidget(self.steps_area)

        self.setLayout(layout)

        self.simulate_button.clicked.connect(self.run_simulation)

    def run_simulation(self):
        steps = key_exchange_chat.simulate_dh_key_exchange()
        self.steps_area.setPlainText("\n\n".join(steps))