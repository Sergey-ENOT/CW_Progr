from PyQt5 import QtWidgets, QtGui
from DBStudentInterface import Ui_MainWindow
from pop_up_windows.settings_student import Ui_studentForm
import sys


class SettingsStudent(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsStudent, self).__init__()
        self.ui = Ui_studentForm()
        self.ui.setupUi(self)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonDisplayRecordsStudent.clicked.connect(self.show_settings_student)

    def show_settings_student(self):
        self.w = SettingsStudent()
        self.w.show()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
