# main.py

import sys
from PyQt6.QtWidgets import QApplication
from login import LoginWindow

def main():
    app = QApplication(sys.argv)

    # Apply Dark Theme
    dark_stylesheet = """
    QWidget {
        background-color: #121212;
        color: #e0e0e0;
        font-size: 14px;
    }
    QPushButton {
        background-color: #1e1e1e;
        border: 1px solid #333;
        padding: 5px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #333;
    }
    QLineEdit, QPlainTextEdit, QTextEdit {
        background-color: #1e1e1e;
        border: 1px solid #333;
        padding: 5px;
        border-radius: 5px;
        color: #e0e0e0;
    }
    QTableWidget {
        background-color: #1e1e1e;
        border: 1px solid #333;
        gridline-color: #444;
        color: #e0e0e0;
    }
    QHeaderView::section {
        background-color: #222;
        color: #ddd;
        border: 1px solid #444;
    }
    QLabel {
        color: #e0e0e0;
    }
    """
    app.setStyleSheet(dark_stylesheet)

    # Launch the Login Window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
