import os, sys, datetime
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QDesktopWidget, QGroupBox, QListView,
                             QTextEdit, QTreeView
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

        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(44)

        listView = QListView()
        listView.setMinimumHeight(150)
        # listView.setWordWrap(True)
        # listView.setWrapping(True)
        listView.setSpacing(3)
        self.entry = QtGui.QStandardItemModel()
        listView.setModel(self.entry)
        self.entry.setColumnCount(2)

        treeView = QTreeView()
        treeView.setMinimumHeight(150)
        treeView.setModel(self.entry)
        treeView.setHeaderHidden(True)
        

        sndBtn = QPushButton("Send")
        sndBtn.setMaximumHeight(44)
        sndBtn.clicked.connect(self.sendMsg)

        centerLayout.addWidget(treeView)

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
        msgText = QtGui.QStandardItem(self.textEdit.toPlainText())
        msgTime = QtGui.QStandardItem(datetime.datetime.now().strftime("%H:%M:%S"))
        # self.entry.appendRow(msg)
        self.entry.appendRow([msgText, msgTime])
        self.textEdit.clear()
####################################


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
