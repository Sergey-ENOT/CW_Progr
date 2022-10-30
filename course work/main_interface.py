import datetime
from datetime import date
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from db_connector import ConnectorDB
from config import host, user, password, db_name
from DBStudentInterface import Ui_MainWindow
from extensions.extension_student import ParametersStudent
from pop_up_windows.settings_student import Ui_studentForm
from pop_up_windows.add_student import Ui_addStudentForm
from pop_up_windows.edit_student import Ui_editStudentForm
import sys
import traceback


def log_uncaught_exceptions(ex_cls, ex, tb):  # error catcher
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()


sys.excepthook = log_uncaught_exceptions


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
        self.ui.pushButtonDeleteRecordStudent.clicked.connect(self.delete_student)
        self.ui.pushButtonSearchValueStudent.clicked.connect(self.display_filtered_table_students)
        self.list_student_data = []
        self.list_student_changed_data = []
        self.messagebox = QMessageBox()
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
        self.ui.comboBoxValueSearchColumnStudent.addItems(self.parameters_student.list_combo_box)

        self.add_student_win = AddStudent()
        self.add_student_win.ui.pushButtonAddStudent.clicked.connect(self.hide_insert_student)

        self.edit_student_win = EditStudent()
        self.edit_student_win.ui.pushButtonEditStudent.clicked.connect(self.hide_edit_student)

    def show_messagebox(self, level, title, text):
        if level == "critical":
            self.messagebox.setIcon(QMessageBox.Critical)
        elif level == "warning":
            self.messagebox.setIcon(QMessageBox.Warning)
        elif level == "information":
            self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.setWindowTitle(title)
        self.messagebox.setText(text)
        self.messagebox.exec_()

    def check_valid_date(self, value_date):
        if len(value_date) != 10:
            self.show_messagebox("warning", "Warning", "Некорректная длина даты\nФормат: dd.mm.YYYY")
            return 1
        elif (int(value_date[0:2])) < 1 or (int(value_date[0:2])) > 31:
            self.show_messagebox("warning", "Warning", "Недопустимое значение дня\nФормат: dd.mm.YYYY")
            return 2
        elif (value_date[3:5] == "00") or (int(value_date[3:5]) > 12):
            self.show_messagebox("warning", "Warning", "Недопустимое значение месяца\nФормат: dd.mm.YYYY")
            return 3
        return 0

    def show_settings_student(self):
        self.set_student_win.show()

    def get_settings_student(self):
        self.parameters_student.clear_list()
        self.parameters_student.current_len_lcn = 0
        if self.set_student_win.ui.checkBox_gradebook.isChecked():
            self.parameters_student.list_checkBoxes.append("gradebook")
            self.parameters_student.list_columns_name.append("№ Зачётной книжки")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_family.isChecked():
            self.parameters_student.list_checkBoxes.append("surname")
            self.parameters_student.list_columns_name.append("Фамилия")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_name.isChecked():
            self.parameters_student.list_checkBoxes.append("name")
            self.parameters_student.list_columns_name.append("Имя")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_patronymic.isChecked():
            self.parameters_student.list_checkBoxes.append("patronymic")
            self.parameters_student.list_columns_name.append("Отчество")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_group.isChecked():
            self.parameters_student.list_checkBoxes.append("study_group")
            self.parameters_student.list_columns_name.append("Группа")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_date_birthday.isChecked():
            self.parameters_student.list_checkBoxes.append("date_of_birth")
            self.parameters_student.list_columns_name.append("Дата рождения")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_town.isChecked():
            self.parameters_student.list_checkBoxes.append("town")
            self.parameters_student.list_columns_name.append("Город")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_street.isChecked():
            self.parameters_student.list_checkBoxes.append("street")
            self.parameters_student.list_columns_name.append("Улица")
            self.parameters_student.current_len_lcn += 1
        if self.set_student_win.ui.checkBox_house.isChecked():
            self.parameters_student.list_checkBoxes.append("house")
            self.parameters_student.list_columns_name.append("Дом")
            self.parameters_student.current_len_lcn += 1

    def hide_settings_student(self):
        self.get_settings_student()
        self.set_student_win.hide()

    def select_students(self, column=None, value=None):
        self.student_connector.create_connection()
        if (column is None) and (value is None):
            if len(self.parameters_student.list_checkBoxes) == 9:
                self.parameters_student.result_select = self.student_connector.select_data()
                self.parameters_student.all_columns = True
                print("selected all")
            else:
                self.parameters_student.result_select = self.student_connector.select_data(self.parameters_student.list_checkBoxes)
                self.parameters_student.all_columns = False
                print("selected with parameters")
        elif not (column is None) and not (column is None):
            if len(self.parameters_student.list_checkBoxes) == 9:
                self.parameters_student.result_select = self.student_connector.select_filtered_data(column, value)
                self.parameters_student.all_columns = True
                print("selected all")
            else:
                self.parameters_student.result_select = self.student_connector.select_filtered_data(
                                                                                column,
                                                                                value,
                                                                                self.parameters_student.list_checkBoxes)
                self.parameters_student.all_columns = False
                print("selected with parameters")
        self.student_connector.close_connection()

    def display_table_students(self):
        self.select_students()
        if self.parameters_student.first_show:
            self.get_settings_student()
            self.parameters_student.first_show = False

        for i in range(self.ui.tableWidgetStudent.rowCount()):
            self.ui.tableWidgetStudent.removeColumn(i)

        data = self.parameters_student.result_select
        if len(data) > 0:
            self.ui.tableWidgetStudent.setColumnWidth(0, 150)
        numrows = len(data)
        numcolumns = len(self.parameters_student.list_columns_name)
        self.ui.tableWidgetStudent.setColumnCount(numcolumns)
        self.ui.tableWidgetStudent.setHorizontalHeaderLabels(self.parameters_student.list_columns_name)
        self.ui.tableWidgetStudent.setRowCount(numrows)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetStudent.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetStudent.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetStudent.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_students(self):
        db_column = self.parameters_student.dict_combo_box[self.ui.comboBoxValueSearchColumnStudent.currentText()]
        search_text = self.ui.lineEditSearchValueStudent.text().strip()

        self.select_students(db_column, search_text)

        for i in range(self.ui.tableWidgetStudent.rowCount()):
            self.ui.tableWidgetStudent.removeColumn(i)

        data = self.parameters_student.result_select
        if len(data) > 0:
            self.ui.tableWidgetStudent.setColumnWidth(0, 150)
        numrows = len(data)
        numcolumns = len(self.parameters_student.list_columns_name)
        self.ui.tableWidgetStudent.setColumnCount(numcolumns)
        self.ui.tableWidgetStudent.setHorizontalHeaderLabels(self.parameters_student.list_columns_name)
        self.ui.tableWidgetStudent.setRowCount(numrows)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetStudent.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetStudent.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetStudent.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def show_add_student(self):
        self.add_student_win.show()
        self.add_student_win.ui.lineEditGradebook.setText("")
        self.add_student_win.ui.lineEditFamily.setText("")
        self.add_student_win.ui.lineEditName.setText("")
        self.add_student_win.ui.lineEditPatronymic.setText("")
        self.add_student_win.ui.lineEditGroup.setText("")
        self.add_student_win.ui.lineEditDateBirthday.setText("")
        self.add_student_win.ui.lineEditTown.setText("")
        self.add_student_win.ui.lineEditStreet.setText("")
        self.add_student_win.ui.lineEditHouse.setText("")

    def insert_student(self):
        getted_date = self.add_student_win.ui.lineEditDateBirthday.text().replace(" ", "")
        checked_date = self.check_valid_date(getted_date)
        try:
            if len(self.add_student_win.ui.lineEditGradebook.text().strip()) == 0:
                print("Incorrect gradebook")
                self.show_messagebox("warning", "Warning", "Пустой номер\nзачётной книжки")
                return False
            elif checked_date != 0:
                return False
            else:
                self.parameters_student.error = "default"
                custom_date = getted_date[6:10] + "-" + getted_date[3:5] + "-" + getted_date[0:2]
                self.student_connector.create_connection()
                self.student_connector.insert_data(
                                                self.parameters_student,
                                                gradebook=self.add_student_win.ui.lineEditGradebook.text().strip(),
                                                surname=self.add_student_win.ui.lineEditFamily.text().strip(),
                                                name=self.add_student_win.ui.lineEditName.text().strip(),
                                                patronymic=self.add_student_win.ui.lineEditPatronymic.text().strip(),
                                                study_group=self.add_student_win.ui.lineEditGroup.text().strip(),
                                                date_of_birth=custom_date,
                                                town=self.add_student_win.ui.lineEditTown.text().strip(),
                                                street=self.add_student_win.ui.lineEditStreet.text().strip(),
                                                house=self.add_student_win.ui.lineEditHouse.text().strip()
                                                )
                self.student_connector.close_connection()
                if self.parameters_student.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
                    return False
                return True
        except Exception as error:
            print("Error: ", error)
            self.student_connector.close_connection()
            return False

    def hide_insert_student(self):
        insert_return = self.insert_student()
        if insert_return:
            self.add_student_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно добавлена")
            self.get_settings_student()
            self.display_table_students()

    def show_edit_student(self):
        if self.parameters_student.first_show:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи таблицы")
        elif self.parameters_student.current_len_lcn != self.parameters_student.static_len_lcn:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "настроить отображение всех столбцов")
        elif not self.parameters_student.all_columns:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести все записи таблицы")
        elif self.ui.tableWidgetStudent.currentRow() == -1:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "выбрать запись в таблице")
        else:
            self.edit_student_win.show()
            current_row = self.ui.tableWidgetStudent.currentRow()
            self.parameters_student.pk["gradebook"] = self.ui.tableWidgetStudent.item(current_row, 0).text()
            self.list_student_data = [self.ui.tableWidgetStudent.item(current_row, i).text()
                                      for i in range(self.parameters_student.static_len_lcn)]
            self.list_student_changed_data = [self.edit_student_win.ui.lineEditGradebook,
                                              self.edit_student_win.ui.lineEditFamily,
                                              self.edit_student_win.ui.lineEditName,
                                              self.edit_student_win.ui.lineEditPatronymic,
                                              self.edit_student_win.ui.lineEditGroup,
                                              self.edit_student_win.ui.lineEditDateBirthday,
                                              self.edit_student_win.ui.lineEditTown,
                                              self.edit_student_win.ui.lineEditStreet,
                                              self.edit_student_win.ui.lineEditHouse]

            for i in range(self.parameters_student.static_len_lcn):
                self.list_student_changed_data[i].setText(self.list_student_data[i])

    def comparison_values_student(self):
        self.parameters_student.clear_dict()
        for i in range(self.parameters_student.static_len_lcn):
            if self.list_student_data[i] != self.list_student_changed_data[i].text().strip():
                if self.parameters_student.list_checkBoxes[i] == "date_of_birth":
                    custom_date = self.list_student_changed_data[i].text()[6:10] + "-" \
                                  + self.list_student_changed_data[i].text()[3:5] + "-" \
                                  + self.list_student_changed_data[i].text()[0:2]
                    self.parameters_student.dict_changed_data[self.parameters_student.list_checkBoxes[i]] \
                        = custom_date
                else:
                    self.parameters_student.dict_changed_data[self.parameters_student.list_checkBoxes[i]] \
                                                                            = self.list_student_changed_data[i].text()

    def edit_student(self):
        getted_date = self.edit_student_win.ui.lineEditDateBirthday.text().replace(" ", "")
        checked_date = self.check_valid_date(getted_date)
        try:
            if len(self.edit_student_win.ui.lineEditGradebook.text().strip()) == 0:
                print("Incorrect gradebook")
                self.show_messagebox("warning", "Warning", "Пустой номер\nзачётной книжки")
                return False
            elif checked_date != 0:
                return False
            else:
                self.parameters_student.error = "default"
                self.comparison_values_student()
                self.student_connector.create_connection()
                self.student_connector.update_data(self.parameters_student,
                                                   self.parameters_student.pk,
                                                   self.parameters_student.dict_changed_data)
                self.student_connector.close_connection()
                if self.parameters_student.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
                    return False
            return True
        except Exception as error:
            print("Error: ", error)
            self.student_connector.close_connection()
            return False

    def hide_edit_student(self):
        edit_return = self.edit_student()
        if edit_return:
            self.edit_student_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно отредактирована")
            self.get_settings_student()
            self.display_table_students()

    def delete_student(self):
        try:
            if self.parameters_student.first_show:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести записи таблицы")
            elif "gradebook" not in set(self.parameters_student.list_checkBoxes):
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "настроить отображение номера зачётной книжки")
            elif self.ui.tableWidgetStudent.horizontalHeaderItem(0).text() != "№ Зачётной книжки":
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести номер зачётной книжки")
            elif self.ui.tableWidgetStudent.currentRow() == -1:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "выбрать запись в таблице")
            else:
                self.parameters_student.error = "default"
                current_row = self.ui.tableWidgetStudent.currentRow()
                pk_gradebook = self.ui.tableWidgetStudent.item(current_row, 0).text()
                msg_box = QMessageBox.question(self, "Подтверждение удаления",
                                               f"Вы хотите удалить студента с номером\nзачётной книжки {pk_gradebook}?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg_box == QMessageBox.Yes:
                    self.student_connector.create_connection()
                    self.student_connector.delete_data(self.parameters_student, "gradebook", pk_gradebook)
                    self.student_connector.close_connection()
                    if self.parameters_student.error != "default":
                        self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
                    self.show_messagebox("information", "Information", "Запись успешно удалена")
                    self.get_settings_student()
                    self.display_table_students()
        except Exception as error:
            print("Error: ", error)
            self.student_connector.close_connection()


app = QtWidgets.QApplication([])
student_connector = ConnectorDB(host, user, password, db_name, "student")
application = MyWindow(ParametersStudent(), student_connector)
application.show()

sys.exit(app.exec())
