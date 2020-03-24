import sys, os, datetime
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QApplication, QMainWindow,
                                QDockWidget, QPushButton, QWidget, QDesktopWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        maxWidth = QDesktopWidget().availableGeometry().width()
        maxHeight = QDesktopWidget().availableGeometry().height()

    # MENUBAR description:
        mainmenu = self.menuBar()
        file = mainmenu.addMenu("File")
        file.addAction("Toggle Chat", self.toggleDockWidget)
        file.addAction("Close", self.close)
    ######################


        workSpace = QWidget(self)

        self.dockWidget = QDockWidget("Dock", self)
        self.dockWidget.setFloating(True)
        self.dockWidget.setVisible(True)
        self.dockWidget.setMinimumSize(300, 460)
        self.dockWidget.setMaximumSize(maxWidth/2, maxHeight)
        self.dockWidget.setBaseSize(maxWidth/2, maxHeight)
        self.dockWidget.resize(maxWidth/4, maxHeight/1.5)
        self.dockWidget.setVisible(False)
        
        # self.addDockWidget(Qt.NoDockWidgetArea, self.dockWidget)

        self.statusBar()

        toggleDockWidgetBtn = QPushButton("Show geomerty", self)
        toggleDockWidgetBtn.move(10, 40)
        toggleDockWidgetBtn.clicked.connect(self.showGeometry)
        
        self.setGeometry(300, 300, 300, 500)
        self.dockWidget.resize(333, 1000)
        self.setCentralWidget(workSpace)
        

    def toggleDockWidget(self):
        flag = False if self.dockWidget.isVisible() else True
        text = "Messenger status was changed to {}".format("visible" if flag else "hide")
        self.dockWidget.setVisible(flag)
        
        # self.dockWidget.setGeometry(650, 300, 200, 500)

        # SET DOCKWINDOW GEAMETRY AND POSITION
        qtRect = self.dockWidget.frameGeometry()
        rightPoint = QDesktopWidget().availableGeometry().bottomRight()
        qtRect.moveBottomRight(rightPoint)
        self.dockWidget.move(qtRect.bottomRight())

        self.statusBar().showMessage(text, 400)
    

    def showGeometry(self):
        availGeometry = QDesktopWidget().availableGeometry()
        print("Available geometry: ", availGeometry)
        print("Right point: ", QDesktopWidget().availableGeometry().bottomRight())
        print("DockWidget frame: ", self.dockWidget.frameGeometry())
        print("\n" + "|---|"*15 + "\n")
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())