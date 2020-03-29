import subprocess
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QListWidgetItem, QLabel
from PyQt5.QtWidgets import QVBoxLayout

# kod jest poprawionym kodem z generatora QtDesigner
# robione dla proby ale moze sie przydac

def settingFont(size, bold=False, italic=False):
    font = QtGui.QFont()
    font.setFamily("Myriad Pro")
    font.setPointSize(size)
    font.setBold(bold)
    font.setItalic(italic)
    return font


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.centralwidget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.centralwidget)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents = QWidget()
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)

        self.label = QLabel(self.centralwidget)

        self.chooseButton = self.addButton("Wybierz plik", 12, 330, 420, 130, 50)
        self.okButton = self.addButton("Zatwierdź", 14, 200, 630, 130, 50)
        self.saveButton = self.addButton("Zapisz", 16, 700, 640, 130, 50)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1100, 750)
        self.setDocumentMode(False)
        self.setDockNestingEnabled(False)

        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea.setGeometry(QtCore.QRect(100, 180, 361, 161))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.listWidget.setGeometry(QtCore.QRect(0, 0, 361, 161))
        self.listWidget.setFont(settingFont(16))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setObjectName("listWidget")

        for x in range(0, 8):
            item = QListWidgetItem()
            item.setText("pacjent00" + str(x + 1))
            self.listWidget.addItem(item)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label.setGeometry(QtCore.QRect(180, 20, 731, 131))
        self.label.setFont(settingFont(28))
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 370, 361, 41))
        self.textEdit.setFont(settingFont(13))
        self.textEdit.setText("Wprowadź scieżkę pliku wraz z jego nazwą")

        self.ekgView = QtWidgets.QGraphicsView(self.centralwidget)
        self.ekgView.setGeometry(QtCore.QRect(530, 180, 461, 161))
        self.ekgView.setObjectName("ekgView")

        self.vectroView = QtWidgets.QGraphicsView(self.centralwidget)
        self.vectroView.setGeometry(QtCore.QRect(530, 370, 461, 231))
        self.vectroView.setObjectName("vectroView")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 190, 41, 21))
        self.label_2.setFont(settingFont(14, True))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 380, 201, 21))
        self.label_3.setFont(settingFont(14, True))
        self.label_3.setObjectName("label_3")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionRelease = QtWidgets.QAction(self)
        self.actionRelease.setObjectName("actionRelease")

        self.actionInfo = QtWidgets.QAction(self)
        self.actionInfo.setObjectName("actionInfo")

        self.actionRelease_2 = QtWidgets.QAction(self)
        self.actionRelease_2.setObjectName("actionRelease_2")

        self.actionAuthors = QtWidgets.QAction(self)
        self.actionAuthors.setObjectName("actionAuthors")

        self.actionAdd_patient = QtWidgets.QAction(self)
        self.actionAdd_patient.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAdd_patient.setObjectName("actionAdd_patient")

        self.menuFile.addAction(self.actionAdd_patient)

        self.menuAbout.addAction(self.actionInfo)
        self.menuAbout.addAction(self.actionRelease_2)
        self.menuAbout.addAction(self.actionAuthors)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # dodac wszystko do mainLayout
        #
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.centralwidget)

        # otwarcie exploratora dla proby
        self.actionAdd_patient.triggered.connect(lambda: subprocess.Popen('explorer'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wektrokardiogram"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Oprogramowanie do wczytywania oraz prezentacji wektrokardiogramu"))

        self.label_2.setText(_translate("MainWindow", "EKG"))
        self.label_3.setText(_translate("MainWindow", "WEKTROKARDIOGRAM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionRelease.setText(_translate("MainWindow", "Release"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionRelease_2.setText(_translate("MainWindow", "Release"))
        self.actionAuthors.setText(_translate("MainWindow", "Authors"))
        self.actionAdd_patient.setText(_translate("MainWindow", "Add patient"))
        self.actionAdd_patient.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def addButton(self, text, fontSize, xCoord, yCoord, width, heigh):
        pushButton = QtWidgets.QPushButton(self.centralwidget)
        pushButton.setGeometry(QtCore.QRect(xCoord, yCoord, width, heigh))
        pushButton.setFont(settingFont(fontSize))
        pushButton.setText(text)
        return pushButton


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


run()
