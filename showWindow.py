from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_IrProjectDemo
import sys

class Ui_Dialog(QDialog, ui_IrProjectDemo.Ui_Dialog):
    def __init__(self, text, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self)
        QDialog.exec_
        #self.updateUi()

def main():
    app = QApplication(sys.argv)
    UI = Ui_Dialog( "Diablo3" )
    UI.show()
    app.exec_()

if __name__ == "__main__":
    main()
