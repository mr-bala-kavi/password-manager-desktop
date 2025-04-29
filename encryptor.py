# encryptor.py

from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    """
    Generate a Fernet key based on the user's master password.
    """
    password_bytes = password.encode()
    hashed = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(hashed)

def encrypt_data(data: bytes, password: str) -> bytes:
    """
    Encrypt data using password-derived key.
    """
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(token: bytes, password: str) -> bytes:
    """
    Decrypt data using password-derived key.
    """
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(token)
