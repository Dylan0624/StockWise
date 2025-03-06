import sys
from PyQt6.QtWidgets import QApplication
from GUI.stockwise_ui import StockWiseApp


def main():
    """應用程序入口"""
    app = QApplication(sys.argv)
    window = StockWiseApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()