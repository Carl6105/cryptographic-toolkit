<p align="center">
  <img src="assets/logo.png" width="120" alt="Cryptographic Toolkit Logo">
  <h1 align="center">🔐 Cryptographic Toolkit</h1>
  <p align="center">
    A modular PyQt6 desktop app for crypto operations, designed for devs & security enthusiasts.
  </p>
  <p align="center">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
    <img alt="GUI" src="https://img.shields.io/badge/GUI-PyQt6-orange">
    <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows-blue">
  </p>
</p>

---
### ✨ Features

| Category                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 🖋️ File Signing & Verification  | RSA & ECC-based digital signature creation & validation                     |
| 📜 Certificate Parser        | X.509 certificate viewer and metadata extraction                            |
| 🔍 Hash Comparison           | Compare SHA-256, MD5, SHA-1 digests for file integrity                      |
| 🧩 JWT Analyzer              | Decode, edit, and test JWT tokens with live payload manipulation            |
| 🔐 Password Strength         | Check entropy and strength using custom scoring                             |
| 🧬 Encoding Tools            | Base64 & Hex encode/decode for any input                                    |
| 🧠 RSA Visualizer            | Visual explanation of RSA key structure                                     |
| ⚡ Avalanche Simulator       | Demonstrates avalanche effect in hashing algorithms                         |
| 🔄 Key Exchange Simulation   | Step-by-step Diffie-Hellman interactive simulation                          |
| 🗂️ File Encryption/Decryption| AES-256-CBC mode using password-derived key with salt                       |
| 📷 QR Code Generator         | Create PNG QR codes from input strings or base64                            |
| 📝 Encrypted Notes Vault     | Secure note saving using symmetric crypto                                   |
| 🗑️ File Shredder             | Overwrites and deletes sensitive files (basic secure delete)                |


## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.8+**
- Recommended: Create a virtual environment

### 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/Carl6105/cryptographic-toolkit.git

# Install dependencies
pip install -r requirements.txt
If you don't have a requirements.txt, use:
pip install PyQt6 cryptography pycryptodome qrcode[pil]
```

### 🖥️ Running the Application

```bash
python main.py
```
The main window will launch with a stylish neon-themed UI.
Use the sidebar navigation to explore each crypto module.
Comes with custom icons 🎉

### 🔐 Usage Notes
This app is educational & experimental — not intended for production crypto.

Encryption uses AES-256 with PBKDF2-derived key.

Shredder performs basic overwrite (not effective on SSDs or journaling FS).

JWT Module creates unsigned tokens for dev testing only.

### 🤝 Contribution
Contributions are welcome!

Fork the repo

Create a new branch: git checkout -b my-feature

Commit your changes

Push and open a pull request 🚀

### 📄 License
This project is licensed under the MIT License

© 2025 Carl6105

### 📬 Contact
For support, feedback, or questions:

GitHub: @Carl6105

Email: shaikaadil60@gmail.com

❤️ Support

If this project helped you, feel free to ⭐ star the repo and share it!

Happy Cryptographing! 🔐🚀
