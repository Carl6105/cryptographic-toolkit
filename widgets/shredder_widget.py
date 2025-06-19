import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
)
from modules import shredder

class FileShredderWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.select_button = QPushButton("Select File to Shred")
        self.shred_button = QPushButton("Shred File")
        self.file_label = QLabel("No file selected.")

        layout.addWidget(QLabel("Secure File Shredder"))
        layout.addWidget(self.select_button)
        layout.addWidget(self.file_label)
        layout.addWidget(self.shred_button)

        self.setLayout(layout)

        self.selected_file = ""
        self.select_button.clicked.connect(self.select_file)
        self.shred_button.clicked.connect(self.shred_file)

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File to Shred")
        if path:
            self.selected_file = path
            self.file_label.setText(f"Selected: {os.path.basename(path)}")

    def shred_file(self):
        if not self.selected_file:
            QMessageBox.warning(self, "No File", "Please select a file to shred.")
            return

        try:
            shredder.shred_file(self.selected_file)
            QMessageBox.information(self, "Shredded", f"{os.path.basename(self.selected_file)} has been securely deleted.")
            self.file_label.setText("No file selected.")
            self.selected_file = ""
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to shred file:\n{str(e)}")
