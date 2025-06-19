from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from modules import symmetric

class EncryptWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.password = QLineEdit()
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        layout.addWidget(QLabel("Plaintext / Ciphertext JSON:"))
        layout.addWidget(self.input_text)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_area)

        self.setLayout(layout)

        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        plaintext = self.input_text.text()
        password = self.password.text()
        result = symmetric.encrypt_aes(plaintext, password)
        self.output_area.setText(str(result))

    def decrypt_text(self):
        import ast
        try:
            encrypted_data = ast.literal_eval(self.input_text.text())
            password = self.password.text()
            result = symmetric.decrypt_aes(encrypted_data, password)
            self.output_area.setText(result)
        except Exception as e:
            self.output_area.setText(f"[Error] {e}")
