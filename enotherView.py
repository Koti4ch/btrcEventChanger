import os, sys, datetime
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QDesktopWidget, QGroupBox, QListView,
                             QTextEdit, QTreeView, QScrollArea, QLabel, QFrame
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

        # self.setGeometry(932, 553, 250, 150)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(screenGeometry.width()//2.5, screenGeometry.height()-200)
        self.setCentralWidget(workspace)
        
        
        globalVBox = QVBoxLayout()
        workspace.setLayout(globalVBox)

        upperLayout = QHBoxLayout()
        centerLayout = QHBoxLayout()
        footerLayout = QHBoxLayout()

        self.messagesArea = QScrollArea()
        self.messagesArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        messageAreaZone = QWidget()
        self.messageAreaLayout = QVBoxLayout()
        messageAreaZone.setLayout(self.messageAreaLayout)
        testText = QLabel()
        testText.setWordWrap(True)
        testText.setText("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
        self.messageAreaLayout.addWidget(testText)
        # self.messagesArea.setLayout(QVBoxLayout())
        self.messagesArea.setMinimumHeight(150)
        self.messagesArea.setWidgetResizable(True)

        self.messagesArea.setWidget(messageAreaZone)
        # self.messagesArea.adjustSize()

        print(messageAreaZone.geometry())
        print(self.messagesArea.geometry())
        # for _ in range(25):
        #     messageAreaZone.layout().addWidget(QLabel(str(_)))
        
        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(44)

        sndBtn = QPushButton("Send")
        sndBtn.setMaximumHeight(44)
        sndBtn.clicked.connect(self.sendMsg)


        centerLayout.addWidget(self.messagesArea)

        footerLayout.addWidget(self.textEdit)
        footerLayout.addWidget(sndBtn)

        globalVBox.addLayout(centerLayout)
        globalVBox.addLayout(footerLayout)

        # globalVBox.addLayout(upperHBox)
        # globalVBox.addLayout(centerHBox)
        # globalVBox.addLayout(downHBox)

        self.show()


####    CSS styles for application widgets  #
    def initStyleSheets(self):
        self.setStyleSheet('''
                    QPushButton {
                        border-radius: 3px;
                    }
                    QPushButton::hover {
                        border-radius: 3px;
                        border-width: 2px;
                        font:   12px;
                        padding: 2px;
                    }
        ''')
##############################################



####    Position functionality =)   #
    def centralPosition(self):
        print("Available:", QDesktopWidget().availableGeometry())
        centerPoint = QDesktopWidget().availableGeometry().center()
        print("Screen center:", centerPoint)
        frameCenter = self.frameGeometry()
        print("Frame center:", frameCenter)



        frameCenter.moveCenter(centerPoint)
        self.move(frameCenter.topLeft())
        print("Move to center")
#####################################


####    Send msg                    #
    def sendMsg(self):
        msgText = self.textEdit.toPlainText()
        msgTime = datetime.datetime.now().strftime("%H:%M:%S")
        # self.messageAreaLayout.addWidget(msgText)
        frame = MessageFrame()
        # frame.initFrameUI(self)
        self.messageAreaLayout.addWidget(frame.initFrameUI(self, msgText))
        self.textEdit.clear()
        print()
####################################


class MessageFrame(object):
    def initFrameUI(self, MainWindow, text):
        msgFrame = QFrame()
        msgFrame.setFrameShape(QFrame.WinPanel)
        msgFrame.setFrameShadow(QFrame.Raised)

        frameLayout = QVBoxLayout(msgFrame)

        nameLabel = QLabel('Name:')
        
        msgLabel = QLabel(text)
        msgLabel.setWordWrap(True)
        
        timeLabel = QLabel(datetime.datetime.now().strftime("%H:%M:%S"))
        timeLabel.setAlignment(QtCore.Qt.AlignRight)
        
        dateSeparator = QGroupBox()

        frameLayout.addWidget(nameLabel)
        frameLayout.addWidget(msgLabel)
        frameLayout.addWidget(timeLabel)
        return msgFrame
        print("init")


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
