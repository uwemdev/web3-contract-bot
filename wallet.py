from web3 import Web3
from cryptography.fernet import Fernet
import os

class WalletManager:
    def __init__(self, encryption_key=None):
        self.encryption_key = encryption_key or self.generate_encryption_key()
        self.fernet = Fernet(self.encryption_key)

    @staticmethod
    def generate_encryption_key():
        """Generate and save an encryption key."""
        key = Fernet.generate_key()
        with open("config/encryption_key.key", "wb") as key_file:
            key_file.write(key)
        return key

    @staticmethod
    def load_encryption_key():
        """Load the encryption key from file."""
        with open("config/encryption_key.key", "rb") as key_file:
            return key_file.read()

    def create_wallet(self):
        """Generate a new Ethereum wallet."""
        web3 = Web3()
        account = web3.eth.account.create()
        private_key = account.privateKey.hex()
        encrypted_key = self.encrypt_private_key(private_key)

        # Save wallet details to a file (optional)
        wallet_data = {
            "address": account.address,
            "encrypted_private_key": encrypted_key.decode()
        }
        self.save_wallet(wallet_data)
        return wallet_data

    def import_wallet(self, private_key):
        """Import a wallet using a private key."""
        web3 = Web3()
        account = web3.eth.account.from_key(private_key)
        encrypted_key = self.encrypt_private_key(private_key)
        return {
            "address": account.address,
            "encrypted_private_key": encrypted_key.decode()
        }

    def encrypt_private_key(self, private_key):
        """Encrypt the private key."""
        return self.fernet.encrypt(private_key.encode())

    def decrypt_private_key(self, encrypted_key):
        """Decrypt the private key."""
        return self.fernet.decrypt(encrypted_key.encode()).decode()

    @staticmethod
    def save_wallet(wallet_data):
        """Save wallet details to a file."""
        with open("config/wallets.txt", "a") as file:
            file.write(f"Address: {wallet_data['address']}\n")
            file.write(f"Encrypted Private Key: {wallet_data['encrypted_private_key']}\n")
            file.write("-" * 30 + "\n")
