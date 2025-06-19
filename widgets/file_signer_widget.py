import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit,
    QFileDialog, QHBoxLayout, QComboBox, QMessageBox
)

from modules import file_signer

class FileSignerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_file = ""
        self.signature = ""
        self.algorithm = "RSA"

        layout = QVBoxLayout()

        self.file_label = QLabel("No file selected.")
        self.key_info = QTextEdit()
        self.key_info.setReadOnly(True)

        self.load_file_button = QPushButton("Select File")
        self.load_private_key_button = QPushButton("Load Private Key")
        self.load_public_key_button = QPushButton("Load Public Key")

        self.algorithm_box = QComboBox()
        self.algorithm_box.addItems(["RSA", "ECC"])

        self.sign_button = QPushButton("Sign File")
        self.verify_button = QPushButton("Verify Signature")

        self.signature_display = QTextEdit()
        self.signature_display.setReadOnly(True)

        layout.addWidget(QLabel("Algorithm:"))
        layout.addWidget(self.algorithm_box)
        layout.addWidget(self.load_file_button)
        layout.addWidget(self.file_label)

        layout.addWidget(self.load_private_key_button)
        layout.addWidget(self.load_public_key_button)
        layout.addWidget(QLabel("Key Info:"))
        layout.addWidget(self.key_info)

        layout.addWidget(self.sign_button)
        layout.addWidget(QLabel("Signature (base64):"))
        layout.addWidget(self.signature_display)
        layout.addWidget(self.verify_button)

        self.setLayout(layout)

        # Connections
        self.load_file_button.clicked.connect(self.select_file)
        self.load_private_key_button.clicked.connect(self.load_private_key)
        self.load_public_key_button.clicked.connect(self.load_public_key)
        self.sign_button.clicked.connect(self.sign_file)
        self.verify_button.clicked.connect(self.verify_signature)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.selected_file = file_path
            self.file_label.setText(f"Selected: {os.path.basename(file_path)}")

    def load_private_key(self):
        key_path, _ = QFileDialog.getOpenFileName(self, "Select Private Key (.pem)")
        if key_path:
            with open(key_path, "r") as f:
                self.private_key = f.read()
                self.key_info.setText("Private Key Loaded.")

    def load_public_key(self):
        key_path, _ = QFileDialog.getOpenFileName(self, "Select Public Key (.pem)")
        if key_path:
            with open(key_path, "r") as f:
                self.public_key = f.read()
                self.key_info.setText(self.key_info.toPlainText() + "\nPublic Key Loaded.")

    def sign_file(self):
        try:
            algo = self.algorithm_box.currentText()
            signature = file_signer.sign_file(self.selected_file, self.private_key, algo)
            self.signature = signature
            self.signature_display.setText(signature)
            QMessageBox.information(self, "Success", "File signed successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Signing failed:\n{str(e)}")

    def verify_signature(self):
        try:
            algo = self.algorithm_box.currentText()
            result = file_signer.verify_file_signature(self.selected_file, self.signature, self.public_key, algo)
            if result:
                QMessageBox.information(self, "Verified", "Signature is valid.")
            else:
                QMessageBox.warning(self, "Invalid", "Signature is NOT valid.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Verification failed:\n{str(e)}")
