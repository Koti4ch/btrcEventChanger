import sys, os, datetime
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QApplication, QMainWindow,
                                QDockWidget, QPushButton, QWidget, QDesktopWidget,
                                QSystemTrayIcon, QMenu, QAction)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        maxWidth = QDesktopWidget().availableGeometry().width()
        maxHeight = QDesktopWidget().availableGeometry().height()
        workSpace = QWidget(self)

    ####    MainWindow Configuration
        self.setWindowTitle("Application")
        self.setWindowIcon(QIcon("icon.png"))

        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"))
        self.tray_icon.show()

    ####    Tray MENU   #################
        trayIconMenu = QMenu(self)
        trayIconMenu.addAction("Show Main Window", self.showMainWindow)
        trayIconMenu.addAction("Switch chat", self.toggleDockWidget)
        trayIconMenu.addAction("Quit", self.close)
        self.tray_icon.setContextMenu(trayIconMenu)

    ######################################
        

    # MENUBAR description:
        mainmenu = self.menuBar()
        file = mainmenu.addMenu("File")
        file.addAction("isFloating", self.floatingInfo)
        file.addAction("Toggle Chat", self.toggleDockWidget)
        file.addAction("Close", self.close)
    ######################



        self.dockWidget = QDockWidget("Messenger", self)
        self.dockWidget.setFloating(True)
        self.dockWidget.setVisible(True)
        self.dockWidget.setMinimumSize(300, 460)
        self.dockWidget.setMaximumSize(maxWidth/2, maxHeight)
        self.dockWidget.setBaseSize(maxWidth/2, maxHeight)
        self.dockWidget.resize(maxWidth/4, maxHeight/1.5)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setVisible(False)
        

        

        self.statusBar()

        toggleDockWidgetBtn = QPushButton("Show geomerty", self)
        toggleDockWidgetBtn.move(10, 40)
        toggleDockWidgetBtn.clicked.connect(self.showGeometry)
    
    ####     TEST BUTONS     ####
        hideBtn = QPushButton("hide main", self)
        hideBtn.move(10, 70)
        hideBtn.clicked.connect(self.hideMainWindow)
    #######################################################
        
        self.setGeometry(300, 300, 300, 500)
        self.dockWidget.resize(333, 1000)
        self.setCentralWidget(workSpace)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)
        

    def toggleDockWidget(self):
        flag = False if self.dockWidget.isVisible() else True
        text = "Messenger status was changed to {}".format("visible" if flag else "hide")
        self.dockWidget.setVisible(flag)
        
        # self.dockWidget.setGeometry(650, 300, 200, 500)

    ####     SET DOCKWINDOW GEAMETRY AND POSITION
        qtRect = self.dockWidget.frameGeometry()
        rightPoint = QDesktopWidget().availableGeometry().bottomRight()
        
    ####    FOR LINUX POSITION    ###############################
        # qtRect.moveBottomRight(rightPoint)
        # self.dockWidget.move(qtRect.bottomRight())
    ####    FOR WINDOWS POSITION    #############################
        qtRect.moveBottomRight(rightPoint)
        self.dockWidget.move(qtRect.topLeft())
    ##############################################################

        self.statusBar().showMessage(text, 500)
    
    ####    test functionality
    def showGeometry(self):
        availGeometry = QDesktopWidget().availableGeometry()
        print("Available geometry: ", availGeometry)
        print("Right point: ", QDesktopWidget().availableGeometry().bottomRight())
        print("DockWidget frame bottomRight: ", self.dockWidget.frameGeometry().bottomRight())
        print("DockWidget frame topLeft: ", self.dockWidget.frameGeometry().topLeft())
        print("\n" + "|---|"*15 + "\n")

    def hideMainWindow(self):
        self.hide()
    
    def showMainWindow(self):
        self.show()

    def floatingInfo(self):
        flag = False if self.dockWidget.isFloating() else True
        print("dockWidget status is: ", flag)
        self.dockWidget.setFloating(flag)
        

    ##########################################################################
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
