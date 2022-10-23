from PyQt5 import QtWidgets, QtCore
from db_connector import ConnectorDB
from config import host, user, password, db_name
from DBStudentInterface import Ui_MainWindow
from extensions.extension_student import ParametersStudent
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
    def __init__(self, ext_student, st_conn):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.student_connector = st_conn
        self.parameters_student = ext_student
        self.ui.pushButtonSettingsColumnsStudent.clicked.connect(self.show_settings_student)
        self.ui.pushButtonDisplayRecordsStudent.clicked.connect(self.display_table_students)
        self.ui.pushButtonAddRecordStudent.clicked.connect(self.show_add_student)
        self.ui.pushButtonEditRecordStudent.clicked.connect(self.show_edit_student)
        self.update_ui()

    def update_ui(self):
        self.set_student_win = SettingsStudent()
        self.set_student_win.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.set_student_win.ui.pushButtonApplySettingsStudent.clicked.connect(self.hide_settings_student)
        self.set_student_win.ui.checkBox_gradebook.setChecked(True)
        self.set_student_win.ui.checkBox_family.setChecked(True)
        self.set_student_win.ui.checkBox_name.setChecked(True)
        self.set_student_win.ui.checkBox_patronymic.setChecked(True)
        self.set_student_win.ui.checkBox_group.setChecked(True)
        self.set_student_win.ui.checkBox_date_birthday.setChecked(True)
        self.set_student_win.ui.checkBox_town.setChecked(True)
        self.set_student_win.ui.checkBox_street.setChecked(True)
        self.set_student_win.ui.checkBox_house.setChecked(True)

    def show_settings_student(self):
        self.set_student_win.show()

    def get_settings_student(self):
        self.parameters_student.clear_list()
        if self.set_student_win.ui.checkBox_gradebook.isChecked():
            self.parameters_student.list_checkBoxes.append("gradebook")
            self.parameters_student.list_columns_name.append("№ Зачётной книжки")
        if self.set_student_win.ui.checkBox_family.isChecked():
            self.parameters_student.list_checkBoxes.append("surname")
            self.parameters_student.list_columns_name.append("Фамилия")
        if self.set_student_win.ui.checkBox_name.isChecked():
            self.parameters_student.list_checkBoxes.append("name")
            self.parameters_student.list_columns_name.append("Имя")
        if self.set_student_win.ui.checkBox_patronymic.isChecked():
            self.parameters_student.list_checkBoxes.append("patronymic")
            self.parameters_student.list_columns_name.append("Отчество")
        if self.set_student_win.ui.checkBox_group.isChecked():
            self.parameters_student.list_checkBoxes.append("study_group")
            self.parameters_student.list_columns_name.append("Группа")
        if self.set_student_win.ui.checkBox_date_birthday.isChecked():
            self.parameters_student.list_checkBoxes.append("date_of_birth")
            self.parameters_student.list_columns_name.append("Дата рождения")
        if self.set_student_win.ui.checkBox_town.isChecked():
            self.parameters_student.list_checkBoxes.append("town")
            self.parameters_student.list_columns_name.append("Город")
        if self.set_student_win.ui.checkBox_street.isChecked():
            self.parameters_student.list_checkBoxes.append("street")
            self.parameters_student.list_columns_name.append("Улица")
        if self.set_student_win.ui.checkBox_house.isChecked():
            self.parameters_student.list_checkBoxes.append("house")
            self.parameters_student.list_columns_name.append("Дом")

        # print(self.set_student_win.ui.checkBox_gradebook.isChecked())
        # self.ui.tableWidgetStudent.removeColumn(0)

    def hide_settings_student(self):
        self.get_settings_student()
        self.set_student_win.hide()

    def select_students(self):
        self.student_connector.create_connection()
        if len(self.parameters_student.list_checkBoxes) == 9:
            self.parameters_student.result_select = self.student_connector.select_data()
            print("selected all")
        else:
            self.parameters_student.result_select = self.student_connector.select_data(self.parameters_student.list_checkBoxes)
            print("selected with parameters")
        self.student_connector.close_connection()

    def display_table_students(self):
        self.select_students()
        for i in range(self.ui.tableWidgetStudent.rowCount()):
            self.ui.tableWidgetStudent.removeColumn(i)
        self.ui.tableWidgetStudent.setColumnCount(len(self.parameters_student.list_columns_name))
        self.ui.tableWidgetStudent.setHorizontalHeaderLabels(self.parameters_student.list_columns_name)

    def show_add_student(self):
        self.add_student_win = AddStudent()
        self.add_student_win.show()

    def show_edit_student(self):
        self.edit_student_win = EditStudent()
        self.edit_student_win.show()


app = QtWidgets.QApplication([])
student_connector = ConnectorDB(host, user, password, db_name, "student")
application = MyWindow(ParametersStudent(), student_connector)
application.show()

sys.exit(app.exec())
