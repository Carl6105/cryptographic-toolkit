from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QMessageBox
)
from modules import jwt_tamper
import json

class JWTTamperWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Paste JWT token here")

        self.decode_button = QPushButton("Decode JWT")
        self.payload_area = QTextEdit()
        self.payload_area.setPlaceholderText("JWT payload (editable)...")

        self.tamper_button = QPushButton("Generate Tampered JWT")
        self.output_token = QTextEdit()
        self.output_token.setReadOnly(True)

        layout.addWidget(QLabel("JWT Input:"))
        layout.addWidget(self.token_input)
        layout.addWidget(self.decode_button)
        layout.addWidget(QLabel("Decoded Payload:"))
        layout.addWidget(self.payload_area)
        layout.addWidget(self.tamper_button)
        layout.addWidget(QLabel("Tampered JWT Output:"))
        layout.addWidget(self.output_token)

        self.setLayout(layout)

        self.decode_button.clicked.connect(self.decode_jwt)
        self.tamper_button.clicked.connect(self.generate_tampered_jwt)

    def decode_jwt(self):
        token = self.token_input.text()
        decoded = jwt_tamper.decode_jwt(token)

        if "error" in decoded:
            QMessageBox.critical(self, "Error", f"Invalid JWT:\n{decoded['error']}")
            return

        self.payload_area.setPlainText(
            json.dumps(decoded["payload"], indent=4)
        )

    def generate_tampered_jwt(self):
        try:
            token = self.token_input.text()
            new_payload = json.loads(self.payload_area.toPlainText())
            new_token = jwt_tamper.tamper_jwt(token, new_payload)
            self.output_token.setText(new_token)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Tampering failed:\n{str(e)}")
