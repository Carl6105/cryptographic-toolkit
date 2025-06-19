from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from modules import qr_generator
import base64

class QRCodeGeneratorWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Enter text or URL to convert to QR code...")

        self.generate_button = QPushButton("Generate QR Code")
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel("QR Code Generator"))
        layout.addWidget(self.text_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(QLabel("Generated QR Code:"))
        layout.addWidget(self.image_label)

        self.setLayout(layout)
        self.generate_button.clicked.connect(self.generate_qr)

    def generate_qr(self):
        data = self.text_input.toPlainText()
        if not data:
            return

        b64_img = qr_generator.generate_qr_base64(data)
        img_data = base64.b64decode(b64_img)

        qimg = QImage.fromData(img_data)
        pixmap = QPixmap.fromImage(qimg)
        self.image_label.setPixmap(pixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio))
