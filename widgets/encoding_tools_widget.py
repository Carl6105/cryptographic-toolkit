from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QMessageBox
)
from modules import encoding_tools

class EncodingToolsWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Base64 Encode", "Base64 Decode", "Hex Encode", "Hex Decode"])

        self.input_area = QTextEdit()
        self.input_area.setPlaceholderText("Enter text or encoded input here...")

        self.process_button = QPushButton("Process")
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        layout.addWidget(QLabel("Select Operation:"))
        layout.addWidget(self.mode_selector)
        layout.addWidget(QLabel("Input:"))
        layout.addWidget(self.input_area)
        layout.addWidget(self.process_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_area)

        self.setLayout(layout)
        self.process_button.clicked.connect(self.process_encoding)

    def process_encoding(self):
        try:
            mode = self.mode_selector.currentText()
            data = self.input_area.toPlainText()

            if mode == "Base64 Encode":
                result = encoding_tools.encode_base64(data)
            elif mode == "Base64 Decode":
                result = encoding_tools.decode_base64(data)
            elif mode == "Hex Encode":
                result = encoding_tools.encode_hex(data)
            elif mode == "Hex Decode":
                result = encoding_tools.decode_hex(data)
            else:
                result = "Unknown operation"

            self.output_area.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Operation failed:\n{str(e)}")
