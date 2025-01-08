import os

# Define folder structure
folders = [
    "config",
    "utils"
]

files = {
    "main.py": "# Entry point for the application\n\nif __name__ == '__main__':\n    print('Web3 Contract Interaction Bot')\n",
    "wallet.py": "# Wallet management functions\n\nclass Wallet:\n    pass\n",
    "contract.py": "# Smart contract interaction functions\n\nclass Contract:\n    pass\n",
    "gui.py": "# GUI interface setup\n\nclass GUI:\n    pass\n",
    "config/contract_abi.json": "{}\n",  # Empty JSON file
    "config/settings.json": "{\n  \"rpc_url\": \"http://localhost:8545\",\n  \"network\": \"mainnet\"\n}\n",
    "utils/encryption.py": "# Encryption utilities for private keys\n\ndef encrypt():\n    pass\n\ndef decrypt():\n    pass\n",
    "utils/helpers.py": "# Helper functions\n\ndef log():\n    pass\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Project structure created successfully!")
