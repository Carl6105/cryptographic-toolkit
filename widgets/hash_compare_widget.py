import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QComboBox, QMessageBox
)
from modules import hash_compare

class HashCompareWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.file1_label = QLabel("No file selected.")
        self.file2_label = QLabel("No file selected.")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        self.hash_algos = QComboBox()
        self.hash_algos.addItems(["sha256", "sha1", "md5"])

        self.select_file1_btn = QPushButton("Select File 1")
        self.select_file2_btn = QPushButton("Select File 2")
        self.compare_btn = QPushButton("Compare Hashes")

        layout.addWidget(QLabel("Hash Algorithm:"))
        layout.addWidget(self.hash_algos)
        layout.addWidget(self.select_file1_btn)
        layout.addWidget(self.file1_label)
        layout.addWidget(self.select_file2_btn)
        layout.addWidget(self.file2_label)
        layout.addWidget(self.compare_btn)
        layout.addWidget(QLabel("Comparison Result:"))
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        self.select_file1_btn.clicked.connect(self.select_file1)
        self.select_file2_btn.clicked.connect(self.select_file2)
        self.compare_btn.clicked.connect(self.compare_hashes)

        self.file1 = ""
        self.file2 = ""

    def select_file1(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File 1")
        if path:
            self.file1 = path
            self.file1_label.setText(f"File 1: {os.path.basename(path)}")

    def select_file2(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File 2")
        if path:
            self.file2 = path
            self.file2_label.setText(f"File 2: {os.path.basename(path)}")

    def compare_hashes(self):
        if not self.file1 or not self.file2:
            QMessageBox.warning(self, "Missing Files", "Please select both files.")
            return

        algo = self.hash_algos.currentText()
        try:
            hash1 = hash_compare.file_hash(self.file1, algo)
            hash2 = hash_compare.file_hash(self.file2, algo)
            same = "✅ MATCH" if hash1 == hash2 else "❌ DIFFERENT"

            result = f"Hash 1:\n{hash1}\n\nHash 2:\n{hash2}\n\nResult: {same}"
            self.result_area.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Hash comparison failed:\n{str(e)}")
