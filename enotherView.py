import os, sys, datetime
from PyQt5 import QtCore, QtGui
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

        # self.setGeometry(932, 553, 250, 150)
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

        listView = QListView()
        listView.setMinimumHeight(150)
        self.entry = QtGui.QStandardItemModel()
        listView.setModel(self.entry)
        

        sndBtn = QPushButton("Send")
        sndBtn.setMaximumHeight(44)
        sndBtn.clicked.connect(textEdit.append("text"))

        centerLayout.addWidget(listView)

        footerLayout.addWidget(textEdit)
        footerLayout.addWidget(sndBtn)

        globalVBox.addLayout(centerLayout)
        globalVBox.addLayout(footerLayout)

        # globalVBox.addLayout(upperHBox)
        # globalVBox.addLayout(centerHBox)
        # globalVBox.addLayout(downHBox)

        self.show()



####    Position functionality =)   #
    def centralPosition(self):
        print("Available:", QDesktopWidget().availableGeometry())
        centerPoint = QDesktopWidget().availableGeometry().center()
        print("Screen center:", centerPoint)
        frameCenter = self.frameGeometry()
        print("Frame center:", frameCenter)



        frameCenter.moveCenter(centerPoint)
        self.move(frameCenter.topLeft())
        # move(frameCenter.center())
        print("Move to center")
#####################################
####    Send mdg                    #
    def sendMsg(self):
        self.entry.appendRow("msg")
####################################


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
