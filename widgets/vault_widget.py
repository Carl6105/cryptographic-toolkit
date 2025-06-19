from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog,
    QLineEdit, QTextEdit, QMessageBox
)
from modules import vault

class VaultWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter vault password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.note_editor = QTextEdit()
        self.note_editor.setPlaceholderText("Write or view your secure note here...")

        self.save_button = QPushButton("Save Encrypted Note")
        self.load_button = QPushButton("Load Encrypted Note")

        layout.addWidget(QLabel("Encrypted Notes Vault"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.note_editor)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        self.setLayout(layout)

        self.save_button.clicked.connect(self.save_note)
        self.load_button.clicked.connect(self.load_note)

    def save_note(self):
        content = self.note_editor.toPlainText()
        password = self.password_input.text()

        if not content or not password:
            QMessageBox.warning(self, "Missing Info", "Enter both note content and password.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted Note", filter="Vault Files (*.vault)")
        if not save_path:
            return

        try:
            vault.save_encrypted_note(content, password, save_path)
            QMessageBox.information(self, "Success", "Note saved securely.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed:\n{str(e)}")

    def load_note(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Encrypted Note", filter="Vault Files (*.vault)")
        if not file_path:
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Missing Password", "Please enter the vault password.")
            return

        try:
            note = vault.load_encrypted_note(password, file_path)
            self.note_editor.setText(note)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Load failed:\n{str(e)}")
