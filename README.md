# Cryptographic Toolkit

A powerful, modular desktop application built with **PyQt6** that enables cryptographic operations including hashing, encryption/decryption, signing, verification, JWT manipulation, and more. Designed for security professionals, developers, and enthusiasts who want an all-in-one toolkit with a clean GUI.

---

## Features

- **File Signing & Verification** (RSA/ECC)
- **X.509 Certificate Parsing**
- **File Hash Comparison** (SHA-256, MD5, SHA-1, etc.)
- **JWT Decoder & Payload Tampering Tool**
- **Password Strength Evaluation**
- **Base64 and Hex Encoding/Decoding**
- **RSA Key Components Visualization**
- **Avalanche Effect Simulator for Hashes**
- **Diffie-Hellman Key Exchange Simulation**
- **File Encryption & Decryption (AES-256-CBC)**
- **QR Code Generator (Base64 PNG output)**
- **Encrypted Notes Vault**
- **Secure File Shredder**

---

## Getting Started

### Prerequisites

- Python 3.8+
- Recommended to use a virtual environment

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Carl6105/cryptographic-toolkit.git
   cd cryptographic-toolkit

2. Install dependencies:
pip install PyQt6 cryptography pycryptodome qrcode[pil]

3. Running the Application
python main.py

The app window will open, providing a sidebar navigation to all toolkit modules.

# Folder Structure
cryptographic-toolkit/
├── main.py                  # Main application launcher
├── modules/                 # Backend crypto modules (logic)
│   ├── file_signer.py
│   ├── cert_parser.py
│   ├── hash_compare.py
│   ├── jwt_tamper.py
│   ├── password_strength.py
│   ├── encoding_tools.py
│   ├── rsa_visualizer.py
│   ├── avalanche_sim.py
│   ├── key_exchange_chat.py
│   ├── file_crypto.py
│   ├── qr_generator.py
│   ├── vault.py
│   └── shredder.py
├── widgets/                 # PyQt6 widgets for each feature
│   ├── file_signer_widget.py
│   ├── cert_parser_widget.py
│   ├── hash_compare_widget.py
│   ├── jwt_tamper_widget.py
│   ├── password_strength_widget.py
│   ├── encoding_tools_widget.py
│   ├── rsa_visualizer_widget.py
│   ├── avalanche_sim_widget.py
│   ├── key_exchange_widget.py
│   ├── file_crypto_widget.py
│   ├── qr_generator_widget.py
│   ├── vault_widget.py
│   └── shredder_widget.py
├── requirements.txt         # Project dependencies
└── README.md

# Usage Notes
Security: This toolkit is intended for educational and development use. Do not use for production cryptographic operations without proper security review.

File Encryption: Uses AES-256 with PBKDF2 key derivation. Ensure strong passwords.

File Shredder: Implements basic file overwrite; does not guarantee recovery prevention on SSDs or journaling filesystems.

JWT Tampering: Generates unsigned tokens for testing only.

Contribution
Contributions, issues, and feature requests are welcome!
Feel free to fork and submit pull requests.

License
MIT License © 2025 Carl

Contact
For questions or support, reach out to Carl via GitHub or email.

Happy cryptographing! 🔐🚀