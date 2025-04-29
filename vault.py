# vault.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QAbstractItemView
)
from PyQt6.QtGui import QClipboard
from PyQt6.QtCore import QTimer, Qt, QEvent
import secrets
import string
from storage import load_vault, save_vault
from PyQt6.QtWidgets import QApplication



class VaultWindow(QWidget):
    def __init__(self, master_password):
        super().__init__()
        self.master_password = master_password
        self.setWindowTitle("SecureVault - Vault")
        self.setGeometry(150, 150, 600, 500)

        self.layout = QVBoxLayout()

        self.site_input = QLineEdit()
        self.site_input.setPlaceholderText("Website/Service Name")
        self.layout.addWidget(self.site_input)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username/Email")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.layout.addWidget(self.password_input)

        self.generate_button = QPushButton("Generate Strong Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.save_button = QPushButton("Save Password")
        self.save_button.clicked.connect(self.save_password)
        self.layout.addWidget(self.save_button)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Site", "Username", "Password", "Show/Hide", "Copy"])
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

        self.vault = {}
        self.load_vault()

        # Auto-lock
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.auto_logout)
        self.reset_inactivity_timer()
        self.installEventFilter(self)

    def load_vault(self):
        self.vault = load_vault(self.master_password) or {}
        self.refresh_table()

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(20))
        self.password_input.setText(password)

    def save_password(self):
        site = self.site_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if site and username and password:
            self.vault[site] = {"username": username, "password": password}
            save_vault(self.vault, self.master_password)
            QMessageBox.information(self, "Saved", f"Password for {site} saved successfully!")
            self.site_input.clear()
            self.username_input.clear()
            self.password_input.clear()
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields!")

    def refresh_table(self):
        self.table.setRowCount(0)
        for row, (site, creds) in enumerate(self.vault.items()):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(site))
            self.table.setItem(row, 1, QTableWidgetItem(creds["username"]))

            password_item = QTableWidgetItem("********")
            password_item.setData(Qt.ItemDataRole.UserRole, creds["password"])
            self.table.setItem(row, 2, password_item)

            show_btn = QPushButton("Show")
            show_btn.clicked.connect(lambda _, r=row: self.toggle_password(r))
            self.table.setCellWidget(row, 3, show_btn)

            copy_btn = QPushButton("Copy")
            copy_btn.clicked.connect(lambda _, r=row: self.copy_password(r))
            self.table.setCellWidget(row, 4, copy_btn)

    def toggle_password(self, row):
        item = self.table.item(row, 2)
        actual_password = item.data(Qt.ItemDataRole.UserRole)
        current_text = item.text()
        if current_text == "********":
            item.setText(actual_password)
            self.table.cellWidget(row, 3).setText("Hide")
        else:
            item.setText("********")
            self.table.cellWidget(row, 3).setText("Show")

    def copy_password(self, row):
        item = self.table.item(row, 2)
        password = item.data(Qt.ItemDataRole.UserRole)
        QApplication.clipboard().setText(password)
        QMessageBox.information(self, "Copied", "Password copied to clipboard!")

    # ========== Auto-Lock ==========
    def reset_inactivity_timer(self):
        self.inactivity_timer.start(1 * 60 * 1000)  # 1 minute

    def auto_logout(self):
        QMessageBox.information(self, "Auto Lock", "Session timed out. Logging out.")
        self.logout()

    def logout(self):
        from login import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def eventFilter(self, source, event):
        if event.type() in [QEvent.Type.KeyPress, QEvent.Type.MouseMove]:
            self.reset_inactivity_timer()
        return super().eventFilter(source, event)
