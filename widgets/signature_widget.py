from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox
from modules import asymmetric_rsa, asymmetric_ecc

class SignatureWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.message_input = QLineEdit()
        self.key_input = QTextEdit()
        self.signature_input = QTextEdit()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.algos = QComboBox()
        self.algos.addItems(["RSA", "ECC"])

        self.sign_button = QPushButton("Sign")
        self.verify_button = QPushButton("Verify")

        layout.addWidget(QLabel("Message:"))
        layout.addWidget(self.message_input)
        layout.addWidget(QLabel("Key (PEM format):"))
        layout.addWidget(self.key_input)
        layout.addWidget(QLabel("Signature (for verification):"))
        layout.addWidget(self.signature_input)
        layout.addWidget(QLabel("Algorithm:"))
        layout.addWidget(self.algos)
        layout.addWidget(self.sign_button)
        layout.addWidget(self.verify_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)

        self.sign_button.clicked.connect(self.sign_message)
        self.verify_button.clicked.connect(self.verify_message)

    def sign_message(self):
        msg = self.message_input.text()
        key = self.key_input.toPlainText()
        algo = self.algos.currentText()

        try:
            if algo == "RSA":
                sig = asymmetric_rsa.sign_message(key, msg)
            else:
                sig = asymmetric_ecc.sign_ecc_message(key, msg)
            self.output.setText(sig)
        except Exception as e:
            self.output.setText(f"[Error] {e}")

    def verify_message(self):
        msg = self.message_input.text()
        key = self.key_input.toPlainText()
        sig = self.signature_input.toPlainText()
        algo = self.algos.currentText()

        try:
            if algo == "RSA":
                valid = asymmetric_rsa.verify_signature(key, msg, sig)
            else:
                valid = asymmetric_ecc.verify_ecc_signature(key, msg, sig)
            self.output.setText("Signature valid ✅" if valid else "Invalid signature ❌")
        except Exception as e:
            self.output.setText(f"[Error] {e}")
