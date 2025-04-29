# login.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog
from vault import VaultWindow
import bcrypt
import json
import os

class SignUpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New User")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup_user)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def signup_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if len(username) == 0 or len(password) == 0:
            QMessageBox.warning(self, "Input Error", "Both username and password are required!")
            return

        if signup(username, password):
            QMessageBox.information(self, "Success", "Account created successfully! Please log in.")
            self.accept()
        else:
            QMessageBox.warning(self, "Signup Failed", "Username already exists!")


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureVault - Login / Signup")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Master Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.signup_button = QPushButton("New User? Sign Up")
        self.signup_button.clicked.connect(self.open_signup_dialog)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if validate_login(username, password):
            self.vault = VaultWindow(password)
            self.vault.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Wrong username or password!")

    def open_signup_dialog(self):
        signup_dialog = SignUpDialog()
        if signup_dialog.exec() == QDialog.DialogCode.Accepted:
            pass


# === Supporting functions ===

def signup(username, password):
    try:
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                users = json.load(file)
        else:
            users = {}
    except Exception:
        users = {}

    if username in users:
        return False

    # Hash the password securely
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password.decode()

    with open('users.json', 'w') as file:
        json.dump(users, file)

    return True


def validate_login(username, password):
    if not os.path.exists('users.json'):
        return False

    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except Exception:
        return False

    if username not in users:
        return False

    stored_hashed_password = users[username].encode()

    # Check if password matches the hash
    return bcrypt.checkpw(password.encode(), stored_hashed_password)
