from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox
from modules import jwt_handler
import json

class JWTWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.payload_input = QLineEdit()
        self.key_input = QLineEdit()
        self.algorithm_select = QComboBox()
        self.algorithm_select.addItems(["HS256", "RS256", "ES256"])

        self.create_button = QPushButton("Create JWT")
        self.verify_button = QPushButton("Verify JWT")
        self.jwt_input = QLineEdit()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(QLabel("Payload (JSON):"))
        layout.addWidget(self.payload_input)
        layout.addWidget(QLabel("Key / Secret:"))
        layout.addWidget(self.key_input)
        layout.addWidget(QLabel("Algorithm:"))
        layout.addWidget(self.algorithm_select)
        layout.addWidget(self.create_button)
        layout.addWidget(QLabel("JWT to verify (optional):"))
        layout.addWidget(self.jwt_input)
        layout.addWidget(self.verify_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)

        self.create_button.clicked.connect(self.create_jwt)
        self.verify_button.clicked.connect(self.verify_jwt)

    def create_jwt(self):
        try:
            payload = json.loads(self.payload_input.text())
            key = self.key_input.text()
            algo = self.algorithm_select.currentText()
            token = jwt_handler.create_jwt(payload, key, algo)
            self.output.setText(token)
        except Exception as e:
            self.output.setText(f"[Error] {e}")

    def verify_jwt(self):
        try:
            token = self.jwt_input.text()
            key = self.key_input.text()
            algo = self.algorithm_select.currentText()
            result = jwt_handler.verify_jwt(token, key, algo)
            self.output.setText(json.dumps(result, indent=2))
        except Exception as e:
            self.output.setText(f"[Error] {e}")
