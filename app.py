import sys
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings

BASE = Path(__file__).resolve().parent

class TerraVision(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TERRAVISION | Explorador Geográfico da Serra da Prata")
        self.resize(1440, 900)
        self.setMinimumSize(1050, 680)
        self.view = QWebEngineView(self)
        settings = self.view.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.view.setUrl(QUrl.fromLocalFile(str(BASE / "interface.html")))
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TerraVision()
    window.show()
    sys.exit(app.exec())
