import os, sys, datetime
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QDesktopWidget, QGroupBox, QListView,
                             QTextEdit, QTreeView, QScrollArea, QLabel, QFrame, QSizePolicy
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
        self.messagesArea.setWidgetResizable(True)
        messageAreaZone = QWidget()
        self.messageAreaLayout = QVBoxLayout()
        self.messageAreaLayout.setSpacing(20)
        messageAreaZone.setLayout(self.messageAreaLayout)
        ##### Start test message
        # testText = MessageFrame()
        # self.messageAreaLayout.addWidget(testText.initFrameUI(self, "TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TESTTESTTESTTESTTESTTESTTESTTEST"))
        self.messagesArea.setMinimumHeight(150)
        self.messagesArea.setWidgetResizable(True)

        self.messagesArea.setWidget(messageAreaZone)

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
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameCenter = self.frameGeometry()

        frameCenter.moveCenter(centerPoint)
        self.move(frameCenter.topLeft())

    def bottomRightPosition(self):
        bottom_right_point = QDesktopWidget().availableGeometry().bottomRight()
        frame_geometry = self.frameGeometry()

        frame_geometry.moveBottomRight(bottom_right_point)
        self.move(frame_geometry.bottomRight())
#####################################


####    Send msg                    #
    def sendMsg(self):
        msgText = self.textEdit.toHtml()
        msgTime = datetime.datetime.now().strftime("%H:%M:%S")

        frame = MessageFrame()
        self.messageAreaLayout.addWidget(frame.initFrameUI(self, msgText))
        self.textEdit.clear()
####################################


    def test(self):
        self.threadTask1 = ThreadThe1st(self)
        self.threadTask1.start()

        self.threadTask2 = ThreadThe2nd(self)
        self.threadTask2.start()

        self.threadTask3 = ThreadThe3rd(self)
        self.threadTask3.start()

        self.threadTask4 = ThreadThe4th(self)
        self.threadTask4.start()




class MessageFrame(object):
    def initFrameUI(self, MainWindow, text):
        msgFrame = QFrame()
        msgFrame.setFrameShape(QFrame.WinPanel)
        msgFrame.setFrameShadow(QFrame.Raised)
        msgFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        frameLayout = QVBoxLayout(msgFrame)
        frameLayout.setContentsMargins(5,2,5,3)

        nameLabel = QLabel(os.getlogin() + ":")
        
        msgLabel = QLabel(text)
        msgLabel.setWordWrap(True)
        msgLabel.setFrameShadow(QFrame.Raised)
        msgLabel.setMargin(2)
        
        timeLabel = QLabel(datetime.datetime.now().strftime("%H:%M:%S"))
        timeLabel.setAlignment(QtCore.Qt.AlignRight)
        
        dateSeparator = QGroupBox()

        frameLayout.addWidget(nameLabel)
        frameLayout.addWidget(msgLabel)
        frameLayout.addWidget(timeLabel)
        print("init messageFrame:\n", text)
        return msgFrame



class ThreadThe1st(QtCore.QThread):
    signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ThreadThe1st, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            QtCore.QThread.msleep(100)
            print("1 - - - "*5)


class ThreadThe2nd(QtCore.QThread):
    signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ThreadThe2nd, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            QtCore.QThread.msleep(200)
            print("- 2 - - "*5)


class ThreadThe3rd(QtCore.QThread):
    signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ThreadThe3rd, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            QtCore.QThread.msleep(300)
            print("- - 3 - "*5)


class ThreadThe4th(QtCore.QThread):
    signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ThreadThe4th, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            QtCore.QThread.msleep(250)
            print("- - - 4 "*5)


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
