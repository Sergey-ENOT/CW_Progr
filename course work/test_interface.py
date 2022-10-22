from PyQt5 import QtWidgets, QtGui
from DBStudentInterface import Ui_MainWindow
from pop_up_windows.settings_student import Ui_studentForm
from pop_up_windows.add_student import Ui_addStudentForm
from pop_up_windows.edit_student import Ui_editStudentForm
import sys


class SettingsStudent(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsStudent, self).__init__()
        self.ui = Ui_studentForm()
        self.ui.setupUi(self)


class AddStudent(QtWidgets.QWidget):
    def __init__(self):
        super(AddStudent, self).__init__()
        self.ui = Ui_addStudentForm()
        self.ui.setupUi(self)


class EditStudent(QtWidgets.QWidget):
    def __init__(self):
        super(EditStudent, self).__init__()
        self.ui = Ui_editStudentForm()
        self.ui.setupUi(self)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonSettingsColumnsStudent.clicked.connect(self.show_settings_student)
        self.ui.pushButtonAddRecordStudent.clicked.connect(self.show_add_student)
        self.ui.pushButtonEditRecordStudent.clicked.connect(self.show_edit_student)

    def show_settings_student(self):
        self.set_student_win = SettingsStudent()
        self.set_student_win.show()

    def show_add_student(self):
        self.add_student_win = AddStudent()
        self.add_student_win.show()

    def show_edit_student(self):
        self.edit_student_win = EditStudent()
        self.edit_student_win.show()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
