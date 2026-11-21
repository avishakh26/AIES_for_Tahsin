"""TaskFlow AI - offline autonomous task management. Run: python main.py"""
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PySide6.QtGui import QFont, QIcon  # noqa: E402
from PySide6.QtWidgets import QApplication, QMessageBox  # noqa: E402

from core.app_context import AppContext  # noqa: E402
from ui.main_window import MainWindow  # noqa: E402
from ui.theme import Theme  # noqa: E402
from utils.constants import APP_NAME, ASSETS_DIR  # noqa: E402


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setWindowIcon(QIcon(str(ASSETS_DIR / "icons" / "app.svg")))
    app.setFont(QFont("Segoe UI", 10))
    try:
        ctx = AppContext()
    except Exception as exc:  # database cannot be opened, etc.
        logging.exception("Startup failed")
        QMessageBox.critical(None, APP_NAME, f"TaskFlow AI could not start:\n\n{exc}")
        return 1
    Theme.apply(ctx.settings.get("theme"))
    window = MainWindow(ctx)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
