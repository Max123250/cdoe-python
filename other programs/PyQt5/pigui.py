from PyQt5 import QtCore,QtGui,uic
import sys
form = uic.loadUiType("pig.ui")[0]
class Window(QtGui.QWindow,form):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
app = QtGuilication(sys.argv)
window = Window()
window.show()
app.exec_()
