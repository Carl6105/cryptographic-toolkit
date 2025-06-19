import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QLineEdit, QMessageBox
)
from modules import file_crypto

class FileCryptoWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter encryption password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.encrypt_button = QPushButton("Encrypt File")
        self.decrypt_button = QPushButton("Decrypt File")

        layout.addWidget(QLabel("AES File Encryption Tool"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

        self.encrypt_button.clicked.connect(self.encrypt_file)
        self.decrypt_button.clicked.connect(self.decrypt_file)

    def encrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File to Encrypt")
        if not file_path:
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted File", filter="JSON Files (*.json)")
        if not save_path:
            return

        password = self.password_input.text()
        try:
            file_crypto.encrypt_file(file_path, password, save_path)
            QMessageBox.information(self, "Success", "File encrypted successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encryption failed:\n{str(e)}")

    def decrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Encrypted JSON File", filter="JSON Files (*.json)")
        if not file_path:
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted File", filter="Text Files (*.txt)")
        if not save_path:
            return

        password = self.password_input.text()
        try:
            file_crypto.decrypt_file(file_path, password, save_path)
            QMessageBox.information(self, "Success", "File decrypted successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decryption failed:\n{str(e)}")
