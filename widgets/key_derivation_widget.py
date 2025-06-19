from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
from modules import key_derivation

class KeyDerivationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")

        self.kdf_selector = QComboBox()
        self.kdf_selector.addItems(key_derivation.get_supported_kdfs())

        self.salt_output = QLineEdit()
        self.salt_output.setReadOnly(True)

        self.generate_button = QPushButton("Generate Key")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(QLabel("Select Key Derivation Function:"))
        layout.addWidget(self.kdf_selector)
        layout.addWidget(QLabel("Salt (Auto-generated):"))
        layout.addWidget(self.salt_output)
        layout.addWidget(self.generate_button)
        layout.addWidget(QLabel("Derived Key (base64):"))
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.generate_button.clicked.connect(self.generate_key)

    def generate_key(self):
        password = self.password_input.text()
        kdf_name = self.kdf_selector.currentText()
        salt = key_derivation.generate_salt()
        self.salt_output.setText(key_derivation.key_to_base64(salt))

        if kdf_name == "PBKDF2":
            key = key_derivation.derive_key_pbkdf2(password, salt)
        elif kdf_name == "Scrypt":
            key = key_derivation.derive_key_scrypt(password, salt)
        elif kdf_name == "Argon2":
            key = key_derivation.derive_key_argon2(password, salt)
        else:
            self.output.setText("Unknown KDF selected.")
            return

        self.output.setText(key_derivation.key_to_base64(key))
