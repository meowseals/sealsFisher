from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class SealsFisher(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seals Fisher")
        self.setFixedSize(320, 240)

        self.setupUi()
        self.applyStyles()

    def setupUi(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout = QVBoxLayout(centralWidget)
        mainLayout.setContentsMargins(25, 20, 25, 20)
        mainLayout.setSpacing(0)

        # Title

        self.title = QLabel("Seals Fisher")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedHeight(25)

        mainLayout.addWidget(self.title)

        # Status

        mainLayout.addSpacing(2)

        self.status = QLabel("Status: Ready")
        self.status.setObjectName("status")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setFixedHeight(18)

        mainLayout.addWidget(self.status)

        # Statistics

        mainLayout.addSpacing(15)

        statisticsLayout = QVBoxLayout()
        statisticsLayout.setContentsMargins(1, 1, 1, 1)
        statisticsLayout.setSpacing(1)

        self.catches = QLabel("Catches: 0")
        self.failed = QLabel("Failed: 0")
        self.runtime = QLabel("Runtime: 00:00:00")

        self.catches.setObjectName("stat")
        self.failed.setObjectName("stat")
        self.runtime.setObjectName("stat")

        self.catches.setFixedHeight(16)
        self.failed.setFixedHeight(16)
        self.runtime.setFixedHeight(16)

        statisticsLayout.addWidget(self.catches)
        statisticsLayout.addWidget(self.failed)
        statisticsLayout.addWidget(self.runtime)

        mainLayout.addLayout(statisticsLayout)

        # Start button

        mainLayout.addSpacing(15)

        self.startButton = QPushButton("Start Fishing")
        self.startButton.setObjectName("startButton")
        self.startButton.setFixedHeight(36)

        mainLayout.addWidget(self.startButton)

        self.startButton.clicked.connect(self.startFishing)

        # Stop hint

        mainLayout.addSpacing(2)

        self.stopHint = QLabel("F8 Stop")
        self.stopHint.setObjectName("hint")
        self.stopHint.setAlignment(Qt.AlignCenter)

        mainLayout.addWidget(self.stopHint)

    def startFishing(self):

        self.status.setText("Status: Running")
        self.status.setObjectName("running")

        self.status.style().unpolish(self.status)
        self.status.style().polish(self.status)

        self.startButton.setText("Fishing...")

    def applyStyles(self):

        self.setStyleSheet("""

            QMainWindow {
                background-color: #111111;
            }

            QLabel {
                font-family: "Segoe UI";
            }

            #title {
                color: #ffffff;
                font-size: 22px;
                font-weight: 400;
            }

            #status {
                color: #aaaaaa;
                font-size: 13px;
            }

            #running {
                color: #55d98a;
                font-size: 14px;
            }

            #stat {
                color: #aaaaaa;
                font-size: 12px;
                padding: 0px;
                margin: 0px;
            }

            #startButton {
                background-color: #ffffff;
                color: #111111;
                border: none;
                border-radius: 5px;
                font-size: 12px;
            }

            #startButton:hover {
                background-color: #dddddd;
            }

            #startButton:pressed {
                background-color: #bbbbbb;
            }

            #hint {
                color: #ffffff;
                font-size: 12px;
            }

        """)
