from PyQt4 import QtCore, QtGui
import string

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        creates window parts
        :param MainWindow: The main window
        """

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(681, 650)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        # create buttons
        self.calibrateButton = QtGui.QPushButton(self.centralWidget)
        self.calibrateButton.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.calibrateButton.setObjectName(_fromUtf8("calibrateButton"))
        self.importButton = QtGui.QPushButton(self.centralWidget)
        self.importButton.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.exportButton = QtGui.QPushButton(self.centralWidget)
        self.exportButton.setGeometry(QtCore.QRect(10, 70, 111, 23))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))

        # create labels
        self.label = {}
        for i in range(26):
            self.label[string.lowercase[i]] = QtGui.QLabel(self.centralWidget)
            self.label[string.lowercase[i]].setGeometry(QtCore.QRect(15, 103 + 20 * i, 16, 16))
            self.label[string.lowercase[i]].setObjectName(_fromUtf8("label" + format(string.lowercase[i])))

        # create edit boxes
        self.edit = {}
        for i in range(26):
            self.edit[string.lowercase[i]] = QtGui.QLineEdit(self.centralWidget)
            self.edit[string.lowercase[i]].setGeometry(QtCore.QRect(30, 100 + 20 * i, 21, 20))
            self.edit[string.lowercase[i]].setObjectName(_fromUtf8("edit" + string.lowercase[i]))

        # create text boxes
        self.ciphertext = QtGui.QPlainTextEdit(self.centralWidget)
        self.ciphertext.setGeometry(QtCore.QRect(130, 10, 541, 310))
        self.ciphertext.setObjectName(_fromUtf8("ciphertext"))
        self.plaintext = QtGui.QPlainTextEdit(self.centralWidget)
        self.plaintext.setGeometry(QtCore.QRect(130, 330, 541, 310))
        self.plaintext.setObjectName(_fromUtf8("plaintext"))

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        # self.connectUiEvents()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Gives text & labels & stuff to parts of the window
        :param MainWindow: the main window, I guess
        """

        MainWindow.setWindowTitle(_translate("MainWindow", "Stuff Decrypter 3000", None))

        # label buttons
        self.calibrateButton.setText(_translate("MainWindow", "Calibrate", None))
        self.importButton.setText(_translate("MainWindow", "Import ciphertext", None))
        self.exportButton.setText(_translate("MainWindow", "Export plaintext", None))

        # give the labels text
        for i in range(26):
            self.label[string.lowercase[i]].setText(_translate("MainWindow", string.lowercase[i] + ":", None))

        # give the edit boxes placeholders
        for i in range(26):
            self.edit[string.lowercase[i]].setText(_translate("MainWindow", string.lowercase[i], None))



