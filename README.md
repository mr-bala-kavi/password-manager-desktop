# 🔐 Password Manager Desktop

A **secure desktop password manager** built with **PyQt6**, designed to store and manage user credentials with encryption and a modern dark-themed interface.

🌐 Hosted at: [github.com/mr-bala-kavi/password-manager-desktop](https://github.com/mr-bala-kavi/password-manager-desktop)

This application allows users to securely save website credentials, generate strong passwords, and access them with a master password.

---

## 🚀 Features

- 🔑 **Secure Authentication**: Sign up and log in with a username and master password, hashed using **bcrypt** for security.
- 🛡 **Encrypted Storage**: Store website credentials (site, username, password) in an encrypted file (`vault.enc`) using **Fernet encryption** derived from the master password.
- 🔁 **Password Generation**: Generate random, 20-character passwords using a secure mix of letters, digits, and punctuation.
- 🕒 **Auto-Lock**: Automatically logs out after 1 minute of inactivity to prevent unauthorized access.
- 📋 **Clipboard Integration**: Copy passwords to the clipboard with a single click.
- 👁 **Password Visibility**: Toggle between showing and hiding passwords in the vault table.
- 🌙 **Dark Theme**: Sleek, user-friendly dark theme for the graphical interface.

---

## 📦 Requirements

- Python 3.8 or higher
- Dependencies (specified in `requirements.txt`):
  - `PyQt6==6.3.1`
  - `bcrypt==4.0.1`
  - `cryptography==38.0.3`

---

## ⚙️ Installation

```bash
# Clone the repository:
git clone https://github.com/mr-bala-kavi/password-manager-desktop.git
cd password-manager-desktop

# (Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt

# Run the application:
python main.py
```

---

## 🧑‍💻 Usage

1. **Sign Up**: On the login window, click *"New User? Sign Up"* to create an account with a username and master password.
2. **Log In**: Enter your username and master password to access the vault.
3. **Manage Credentials**:
   - Input a website, username, and password, or click *"Generate Strong Password"* for a secure password.
   - Click *"Save Password"* to store the credentials securely.
   - View saved credentials in the table, use *"Show/Hide"* to toggle password visibility, or *"Copy"* to copy passwords to the clipboard.
4. **Auto-Lock**: The application locks after 1 minute of inactivity (no keyboard or mouse input), requiring re-authentication.

---

## 🗂 Project Structure

- `main.py`: Initializes the PyQt6 application and applies the dark theme.
- `login.py`: Manages user authentication (login/signup) with bcrypt password hashing.
- `vault.py`: Implements the vault interface for adding, viewing, and managing credentials.
- `storage.py`: Handles loading and saving encrypted vault data using Fernet.
- `encryptor.py`: Provides encryption/decryption functions with a password-derived key.
- `users.py`: Alternative user management module (not used in the main application).
- `users.json`: Stores usernames and bcrypt-hashed passwords.
- `vault.enc`: Stores encrypted vault data.
- `requirements.txt`: Lists required Python packages.

---

## 🔒 Security Details

- **Password Hashing**: User passwords are hashed with `bcrypt` and stored in `users.json`.
- **Encryption**: Vault data is encrypted using `Fernet` with a SHA-256-derived key from the master password.
- **Secure Key Derivation**: The encryption key is generated from the master password, ensuring data is only accessible with the correct password.
- **Auto-Lock**: Enhances security by locking the application after inactivity.

---

## ⚠️ Limitations

- ❌ **No Password Recovery**: If the master password is lost, vault data cannot be decrypted.
- 🗃 **Unused Module**: The `users.py` module uses SHA-256 hashing and is not integrated into the main application (which uses bcrypt in `login.py`).
- 🕒 **Fixed Auto-Lock**: The 1-minute auto-lock timer is not configurable.
- 👤 **Single User**: The application does not support multiple users on the same device with separate vaults.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request.

📢 Please report bugs or suggest features via GitHub Issues.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact

For questions or support, contact the repository owner via [GitHub](https://github.com/mr-bala-kavi/password-manager-desktop) or open an issue.

---

Made with ❤️ by Kavi

