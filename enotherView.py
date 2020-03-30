import os, sys, datetime
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QDesktopWidget, QGroupBox, QListView,
                             QTextEdit,
                            )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMainWindow()
    

####    Settings to main window and start position
    def initMainWindow(self):
    ####    Check available screen geometry
        screenGeometry = QDesktopWidget().screenGeometry()
        availableScreen = QDesktopWidget().availableGeometry()
    ##########################################

        workspace = QWidget(self)
        self.setWindowTitle("Eventeger")
        self.statusBar().showMessage("We are ready!", 900)

        self.setGeometry(310, 320, 250, 150)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(screenGeometry.width()//2.5, screenGeometry.height()-200)
        self.setCentralWidget(workspace)
        
        globalVBox = QVBoxLayout()
        workspace.setLayout(globalVBox)

        upperLayout = QHBoxLayout()
        centerLayout = QHBoxLayout()
        footerLayout = QHBoxLayout()

        textEdit = QTextEdit()
        textEdit.setMaximumHeight(44)
        textEdit2 = QTextEdit()
        textEdit3 = QTextEdit()
        textEdit3.setMaximumHeight(100)

        sndBtn = QPushButton("Send")
        sndBtn.setMaximumHeight(44)

        footerLayout.addWidget(textEdit)
        footerLayout.addWidget(sndBtn)


        globalVBox.addWidget(textEdit3)
        globalVBox.addWidget(textEdit2)
        globalVBox.addLayout(footerLayout)
        
        # globalVBox.addLayout(upperHBox)
        # globalVBox.addLayout(centerHBox)
        # globalVBox.addLayout(downHBox)

        self.show()
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
