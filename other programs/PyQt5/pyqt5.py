import sys  
from PyQt5 import QtWidgets
app = QtWidgets.QApplication(sys.argv)  
widget = QtWidgets.QWidget()  
widget.resize(400, 100)  
widget.setWindowTitle("hello.")
widget.show()
exit(app.exec_()) 
