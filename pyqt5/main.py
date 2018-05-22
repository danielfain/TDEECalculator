import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('tdee calculator')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.windowSize = QtCore.QRect(0, 0, 500, 500)
        self.windowSize.moveCenter(self.centerPoint)
        self.setGeometry(self.windowSize)
        self.view()

    def view(self):
        label1 = QtWidgets.QLabel(self)
        label1.setText('Height in cm:')
        self.show()

    """
    def tdee_calculator(self, self.mass, self.cm, self.age, self.gender):
        bmrMale = (10 * self.mass + 6.25 * self.cm - 5 * self.age) + 5
        bmrFemale = (10 * self.mass + 6.25 * self.cm - 5 * self.age) - 151

        if self.gender == 'male':
            return int(bmrMale)
        else:
            return int(bmrFemale)
    """

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())