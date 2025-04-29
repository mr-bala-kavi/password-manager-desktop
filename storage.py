# storage.py

import json
import os
import base64
import hashlib
from cryptography.fernet import Fernet

VAULT_FILE = "vault.enc"

def derive_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def load_vault(master_password):
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(derive_key(master_password))
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data)
    except:
        return None

def save_vault(data, master_password):
    fernet = Fernet(derive_key(master_password))
    encrypted_data = fernet.encrypt(json.dumps(data).encode())

    with open(VAULT_FILE, "wb") as file:
        file.write(encrypted_data)
