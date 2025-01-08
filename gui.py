import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox
from wallet import WalletManager

class WalletApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize wallet manager
        try:
            encryption_key = WalletManager.load_encryption_key()
        except FileNotFoundError:
            encryption_key = WalletManager.generate_encryption_key()

        self.wallet_manager = WalletManager(encryption_key)

        # GUI Layout
        self.setWindowTitle("Web3 Wallet Manager")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(QLabel("Wallet Manager"))
        layout.addWidget(self.output)

        # Buttons
        self.create_wallet_btn = QPushButton("Create Wallet")
        self.import_wallet_btn = QPushButton("Import Wallet")
        self.load_wallets_btn = QPushButton("Load Saved Wallets")

        layout.addWidget(self.create_wallet_btn)
        layout.addWidget(self.import_wallet_btn)
        layout.addWidget(self.load_wallets_btn)

        # Connect Buttons to Functions
        self.create_wallet_btn.clicked.connect(self.create_wallet)
        self.import_wallet_btn.clicked.connect(self.import_wallet)
        self.load_wallets_btn.clicked.connect(self.load_wallets)

        self.setLayout(layout)

    def create_wallet(self):
        """Create a new wallet and display details."""
        wallet = self.wallet_manager.create_wallet()
        self.output.append(f"New Wallet Created:\nAddress: {wallet['address']}")

    def import_wallet(self):
        """Import an existing wallet from a private key."""
        private_key, _ = QFileDialog.getOpenFileName(self, "Select Private Key File", "", "Text Files (*.txt);;All Files (*)")
        if private_key:
            try:
                with open(private_key, 'r') as file:
                    key = file.read().strip()
                    wallet = self.wallet_manager.import_wallet(key)
                    self.output.append(f"Wallet Imported:\nAddress: {wallet['address']}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to import wallet: {str(e)}")

    def load_wallets(self):
        """Load all saved wallets from file."""
        try:
            with open("config/wallets.txt", "r") as file:
                wallets = file.read()
                self.output.setText(wallets)
        except FileNotFoundError:
            QMessageBox.warning(self, "No Wallets Found", "No saved wallets found.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WalletApp()
    window.show()
    sys.exit(app.exec_())
