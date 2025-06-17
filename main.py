import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QMessageBox
from crypto_utils import generate_key, save_key, load_key, encrypt_file, decrypt_file

class FileVaultApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐 Secure File Vault")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("🔑 Enter password to generate key")
        layout.addWidget(self.password_input)

        self.generate_key_btn = QPushButton("Generate & Save Key")
        self.generate_key_btn.clicked.connect(self.generate_and_save_key)
        layout.addWidget(self.generate_key_btn)

        self.encrypt_btn = QPushButton("Encrypt File")
        self.encrypt_btn.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton("Decrypt File")
        self.decrypt_btn.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_btn)

        self.setLayout(layout)

    def generate_and_save_key(self):
        key = generate_key()
        save_key(key)
        QMessageBox.information(self, "Success", "Encryption key saved as secret.key")

    def encrypt(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if file_path:
            key = load_key()
            encrypt_file(file_path, key)
            QMessageBox.information(self, "Encrypted", "File encrypted successfully!")

    def decrypt(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Decrypt (.enc)")
        if file_path:
            key = load_key()
            try:
                output_file = decrypt_file(file_path, key)
                QMessageBox.information(self, "Decrypted", f"File decrypted: {output_file}")

                # 🔥 Open the file (macOS only)
                os.system(f"open '{output_file}'")

            except:
                QMessageBox.critical(self, "Error", "Invalid key or file.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileVaultApp()
    window.show()
    sys.exit(app.exec_())