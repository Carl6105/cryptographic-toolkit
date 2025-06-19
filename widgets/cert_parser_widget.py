from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QMessageBox
from modules import cert_parser

class CertParserWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.pem_input = QTextEdit()
        self.pem_input.setPlaceholderText("Paste PEM-encoded certificate here...")

        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        self.load_button = QPushButton("Load from File")
        self.parse_button = QPushButton("Parse Certificate")

        layout.addWidget(QLabel("X.509 Certificate Parser"))
        layout.addWidget(self.pem_input)
        layout.addWidget(self.load_button)
        layout.addWidget(self.parse_button)
        layout.addWidget(QLabel("Certificate Details"))
        layout.addWidget(self.result_output)

        self.setLayout(layout)

        self.load_button.clicked.connect(self.load_from_file)
        self.parse_button.clicked.connect(self.parse_certificate)

    def load_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Certificate File", filter="PEM Files (*.pem)")
        if file_path:
            with open(file_path, "r") as f:
                self.pem_input.setText(f.read())

    def parse_certificate(self):
        pem_data = self.pem_input.toPlainText()
        result = cert_parser.parse_certificate(pem_data)
        if "error" in result:
            QMessageBox.critical(self, "Parsing Failed", result["error"])
        else:
            output = "\n".join([f"{k}: {v}" for k, v in result.items()])
            self.result_output.setText(output)