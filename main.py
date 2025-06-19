import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, QStackedWidget, QLabel
)
from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtCore import Qt, QTimer
from ui import style

# Import all widgets
from widgets.file_signer_widget import FileSignerWidget
from widgets.cert_parser_widget import CertParserWidget
from widgets.hash_compare_widget import HashCompareWidget
from widgets.jwt_tamper_widget import JWTTamperWidget
from widgets.password_strength_widget import PasswordStrengthWidget
from widgets.encoding_tools_widget import EncodingToolsWidget
from widgets.rsa_visualizer_widget import RSAVisualizerWidget
from widgets.avalanche_sim_widget import AvalancheSimWidget
from widgets.key_exchange_widget import KeyExchangeWidget
from widgets.file_crypto_widget import FileCryptoWidget
from widgets.qr_generator_widget import QRCodeGeneratorWidget
from widgets.vault_widget import VaultWidget
from widgets.shredder_widget import FileShredderWidget


class CryptoToolkitApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(os.path.join('assets', 'logo.png')))
        self.setWindowTitle("Cryptographic Toolkit")
        self.setMinimumSize(1000, 650)

        # Main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Sidebar navigation
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(230)
        self.sidebar.setStyleSheet("QListWidget::item:selected { background-color: #00ffff; color: black; }")
        main_layout.addWidget(self.sidebar)

        # Stacked widget for all feature screens
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Define feature widgets with icons
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icons')
        self.features = [
            ("File Sign / Verify", "file_sign.png", FileSignerWidget()),
            ("Certificate Parser", "cert.png", CertParserWidget()),
            ("Hash Comparator", "hash.png", HashCompareWidget()),
            ("JWT Tamper Tool", "jwt.png", JWTTamperWidget()),
            ("Password Strength", "password.png", PasswordStrengthWidget()),
            ("Base64 / Hex Tools", "encoding.png", EncodingToolsWidget()),
            ("RSA Key Visualizer", "rsa.png", RSAVisualizerWidget()),
            ("Avalanche Simulator", "avalanche.png", AvalancheSimWidget()),
            ("Diffie-Hellman Exchange", "dh.png", KeyExchangeWidget()),
            ("File Encrypt / Decrypt", "file_crypto.png", FileCryptoWidget()),
            ("QR Code Generator", "qr.png", QRCodeGeneratorWidget()),
            ("Encrypted Notes Vault", "vault.png", VaultWidget()),
            ("File Shredder", "shredder.png", FileShredderWidget())
        ]

        for title, icon_file, widget in self.features:
            item = QListWidgetItem(QIcon(os.path.join(icon_path, icon_file)), title)
            self.sidebar.addItem(item)
            self.stack.addWidget(widget)

        # Connect navigation
        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)
        self.sidebar.setCurrentRow(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style.neon_style())

    # --- Optional Splash Screen ---
    splash_movie = QMovie("assets/splash.gif")
    splash_label = QLabel()
    splash_label.setMovie(splash_movie)
    splash_label.setWindowFlags(Qt.WindowType.SplashScreen | Qt.WindowType.FramelessWindowHint)
    splash_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    splash_movie.start()
    splash_label.show()

    window = CryptoToolkitApp()

    QTimer.singleShot(2500, splash_label.close)  # Show splash for 2.5s
    QTimer.singleShot(2500, lambda: window.show())

    sys.exit(app.exec())