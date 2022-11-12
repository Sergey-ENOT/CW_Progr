import datetime
from datetime import date
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from DBStudentInterface import Ui_MainWindow
from pop_up_windows.settings_student import Ui_studentForm
from pop_up_windows.add_student import Ui_addStudentForm
from pop_up_windows.edit_student import Ui_editStudentForm
from pop_up_windows.settings_group import Ui_groupForm
from pop_up_windows.add_group import Ui_addGroupForm
from pop_up_windows.edit_group import Ui_editGroupForm
from pop_up_windows.settings_subject import Ui_subjectForm
from pop_up_windows.add_subject import Ui_addSubjectForm
from pop_up_windows.edit_subject import Ui_editSubjectForm
from pop_up_windows.settings_scholarship import Ui_scholarshipForm
from pop_up_windows.add_scholarship import Ui_addScholarshipForm
from pop_up_windows.edit_scholarship import Ui_editScholarshipForm
from pop_up_windows.settings_debt import Ui_debtForm
from pop_up_windows.add_debt import Ui_addDebtForm
from pop_up_windows.edit_debt import Ui_editDebtForm
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


class SettingsGroup(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsGroup, self).__init__()
        self.ui = Ui_groupForm()
        self.ui.setupUi(self)


class AddGroup(QtWidgets.QWidget):
    def __init__(self):
        super(AddGroup, self).__init__()
        self.ui = Ui_addGroupForm()
        self.ui.setupUi(self)


class EditGroup(QtWidgets.QWidget):
    def __init__(self):
        super(EditGroup, self).__init__()
        self.ui = Ui_editGroupForm()
        self.ui.setupUi(self)


class SettingsSubject(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsSubject, self).__init__()
        self.ui = Ui_subjectForm()
        self.ui.setupUi(self)


class AddSubject(QtWidgets.QWidget):
    def __init__(self):
        super(AddSubject, self).__init__()
        self.ui = Ui_addSubjectForm()
        self.ui.setupUi(self)


class EditSubject(QtWidgets.QWidget):
    def __init__(self):
        super(EditSubject, self).__init__()
        self.ui = Ui_editSubjectForm()
        self.ui.setupUi(self)


class SettingsScholarship(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsScholarship, self).__init__()
        self.ui = Ui_scholarshipForm()
        self.ui.setupUi(self)


class AddScholarship(QtWidgets.QWidget):
    def __init__(self):
        super(AddScholarship, self).__init__()
        self.ui = Ui_addScholarshipForm()
        self.ui.setupUi(self)


class EditScholarship(QtWidgets.QWidget):
    def __init__(self):
        super(EditScholarship, self).__init__()
        self.ui = Ui_editScholarshipForm()
        self.ui.setupUi(self)


class SettingsDebt(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsDebt, self).__init__()
        self.ui = Ui_debtForm()
        self.ui.setupUi(self)


class AddDebt(QtWidgets.QWidget):
    def __init__(self):
        super(AddDebt, self).__init__()
        self.ui = Ui_addDebtForm()
        self.ui.setupUi(self)


class EditDebt(QtWidgets.QWidget):
    def __init__(self):
        super(EditDebt, self).__init__()
        self.ui = Ui_editDebtForm()
        self.ui.setupUi(self)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, ext_student, st_conn, ext_group, gr_conn, ext_subject, sub_conn, ext_scholarship, sch_conn,
                 ext_debt, debt_conn):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagebox = QMessageBox()
        self.student_connector = st_conn
        self.parameters_student = ext_student
        self.list_student_data = []
        self.list_student_changed_data = []
        self.set_student_win = SettingsStudent()
        self.add_student_win = AddStudent()
        self.edit_student_win = EditStudent()
        self.group_connector = gr_conn
        self.parameters_group = ext_group
        self.list_group_data = []
        self.list_group_changed_data = []
        self.set_group_win = SettingsGroup()
        self.add_group_win = AddGroup()
        self.edit_group_win = EditGroup()
        self.subject_connector = sub_conn
        self.parameters_subject = ext_subject
        self.list_subject_data = []
        self.list_subject_changed_data = []
        self.set_subject_win = SettingsSubject()
        self.add_subject_win = AddSubject()
        self.edit_subject_win = EditSubject()
        self.scholarship_connector = sch_conn
        self.parameters_scholarship = ext_scholarship
        self.list_scholarship_data = []
        self.list_scholarship_changed_data = []
        self.set_scholarship_win = SettingsScholarship()
        self.add_scholarship_win = AddScholarship()
        self.edit_scholarship_win = EditScholarship()
        self.debt_connector = debt_conn
        self.parameters_debt = ext_debt
        self.list_debt_data = []
        self.list_debt_changed_data = []
        self.set_debt_win = SettingsDebt()
        self.add_debt_win = AddDebt()
        self.edit_debt_win = EditDebt()
        self.update_ui()
        self.connect_buttons()

    def update_ui(self):
        self.set_student_win.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
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

        self.set_group_win.ui.checkBox_number_group.setChecked(True)
        self.set_group_win.ui.checkBox_direction_training.setChecked(True)
        self.set_group_win.ui.checkBox_course.setChecked(True)
        self.ui.comboBoxValueSearchColumnGroup.addItems(self.parameters_group.list_combo_box)

        self.set_subject_win.ui.checkBox_id_subject.setChecked(True)
        self.set_subject_win.ui.checkBox_name_subject.setChecked(True)
        self.ui.comboBoxValueSearchColumnSubject.addItems(self.parameters_subject.list_combo_box)

        self.set_scholarship_win.ui.checkBox_id_scholarship.setChecked(True)
        self.set_scholarship_win.ui.checkBox_name_scholarship.setChecked(True)
        self.set_scholarship_win.ui.checkBox_amount.setChecked(True)
        self.ui.comboBoxValueSearchColumnScholarship.addItems(self.parameters_scholarship.list_combo_box)

        self.set_debt_win.ui.checkBox_id_debt.setChecked(True)
        self.set_debt_win.ui.checkBox_gradebook.setChecked(True)
        self.set_debt_win.ui.checkBox_id_subject.setChecked(True)
        self.set_debt_win.ui.checkBox_semester.setChecked(True)
        self.set_debt_win.ui.checkBox_date.setChecked(True)
        self.ui.comboBoxValueSearchColumnDebt.addItems(self.parameters_debt.list_combo_box)

    def connect_buttons(self):
        self.ui.pushButtonSettingsColumnsStudent.clicked.connect(self.show_settings_student)
        self.set_student_win.ui.pushButtonApplySettingsStudent.clicked.connect(self.hide_settings_student)
        self.ui.pushButtonDisplayRecordsStudent.clicked.connect(self.display_table_students)
        self.ui.pushButtonSearchValueStudent.clicked.connect(self.display_filtered_table_students)
        self.ui.pushButtonAddRecordStudent.clicked.connect(self.show_add_student)
        self.add_student_win.ui.pushButtonAddStudent.clicked.connect(self.hide_insert_student)
        self.ui.pushButtonEditRecordStudent.clicked.connect(self.show_edit_student)
        self.edit_student_win.ui.pushButtonEditStudent.clicked.connect(self.hide_edit_student)
        self.ui.pushButtonDeleteRecordStudent.clicked.connect(self.delete_student)

        self.ui.pushButtonSettingsColumnsGroup.clicked.connect(self.show_settings_group)
        self.set_group_win.ui.pushButtonApplySettingsGroup.clicked.connect(self.hide_settings_group)
        self.ui.pushButtonDisplayRecordsGroup.clicked.connect(self.display_table_groups)
        self.ui.pushButtonSearchValueGroup.clicked.connect(self.display_filtered_table_groups)
        self.ui.pushButtonAddRecordGroup.clicked.connect(self.show_add_group)
        self.add_group_win.ui.pushButtonAddGroup.clicked.connect(self.hide_insert_group)
        self.ui.pushButtonEditRecordGroup.clicked.connect(self.show_edit_group)
        self.edit_group_win.ui.pushButtonEditGroup.clicked.connect(self.hide_edit_group)
        self.ui.pushButtonDeleteRecordGroup.clicked.connect(self.delete_group)

        self.ui.pushButtonSettingsColumnsSubject.clicked.connect(self.show_settings_subject)
        self.set_subject_win.ui.pushButtonApplySettingsSubject.clicked.connect(self.hide_settings_subject)
        self.ui.pushButtonDisplayRecordsSubject.clicked.connect(self.display_table_subjects)
        self.ui.pushButtonSearchValueSubject.clicked.connect(self.display_filtered_table_subjects)
        self.ui.pushButtonAddRecordSubject.clicked.connect(self.show_add_subject)
        self.add_subject_win.ui.pushButtonAddSubject.clicked.connect(self.hide_insert_subject)
        self.ui.pushButtonEditRecordSubject.clicked.connect(self.show_edit_subject)
        self.edit_subject_win.ui.pushButtonEditSubject.clicked.connect(self.hide_edit_subject)
        self.ui.pushButtonDeleteRecordSubject.clicked.connect(self.delete_subject)

        self.ui.pushButtonSettingsColumnsScholarship.clicked.connect(self.show_settings_scholarship)
        self.set_scholarship_win.ui.pushButtonApplySettingsScholarship.clicked.connect(self.hide_settings_scholarship)
        self.ui.pushButtonDisplayRecordsScholarship.clicked.connect(self.display_table_scholarships)
        self.ui.pushButtonSearchValueScholarship.clicked.connect(self.display_filtered_table_scholarships)
        self.ui.pushButtonAddRecordScholarship.clicked.connect(self.show_add_scholarship)
        self.add_scholarship_win.ui.pushButtonAddScholarship.clicked.connect(self.hide_insert_scholarship)
        self.ui.pushButtonEditRecordScholarship.clicked.connect(self.show_edit_scholarship)
        self.edit_scholarship_win.ui.pushButtonEditScholarship.clicked.connect(self.hide_edit_scholarship)
        self.ui.pushButtonDeleteRecordScholarship.clicked.connect(self.delete_scholarship)

        self.ui.pushButtonSettingsColumnsDebt.clicked.connect(self.show_settings_debt)
        self.set_debt_win.ui.pushButtonApplySettingsDebt.clicked.connect(self.hide_settings_debt)
        self.ui.pushButtonDisplayRecordsDebt.clicked.connect(self.display_table_debts)
        self.ui.pushButtonSearchValueDebt.clicked.connect(self.display_filtered_table_debts)
        self.ui.pushButtonAddRecordDebt.clicked.connect(self.show_add_debt)
        self.add_debt_win.ui.pushButtonAddDebt.clicked.connect(self.hide_insert_debt)
        self.ui.pushButtonEditRecordDebt.clicked.connect(self.show_edit_debt)
        self.edit_debt_win.ui.pushButtonEditDebt.clicked.connect(self.hide_edit_debt)
        self.ui.pushButtonDeleteRecordDebt.clicked.connect(self.delete_debt)

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
        try:
            self.student_connector.create_connection(self.parameters_student)
            if (column is None) and (value is None):
                if len(self.parameters_student.list_checkBoxes) == 9:
                    self.parameters_student.result_select = self.student_connector.select_data(self.parameters_student)
                    self.parameters_student.all_columns = True
                    print("selected all")
                else:
                    self.parameters_student.result_select = self.student_connector.select_data(self.parameters_student,
                                                                                               self.parameters_student.list_checkBoxes)
                    self.parameters_student.all_columns = False
                    print("selected with parameters")
                self.parameters_student.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_student.list_checkBoxes) == 9:
                    self.parameters_student.result_select = self.student_connector.select_filtered_data(self.parameters_student,
                                                                                                        column, value)
                    self.parameters_student.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_student.result_select = self.student_connector.select_filtered_data(self.parameters_student,
                                                                                    column,
                                                                                    value,
                                                                                    self.parameters_student.list_checkBoxes)
                    self.parameters_student.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_student.last_display = "filtered"
            self.student_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_student.error))

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
                try:
                    self.student_connector.create_connection(self.parameters_student)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
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
                if len(self.parameters_student.dict_changed_data) == 0:
                    self.show_messagebox("information", "Information", "Изменений не обнаружено")
                    return False
                try:
                    self.student_connector.create_connection(self.parameters_student)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
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
            if self.parameters_student.last_display == "all":
                self.display_table_students()
            elif self.parameters_student.last_display == "filtered":
                self.display_filtered_table_students()

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
                    try:
                        self.student_connector.create_connection(self.parameters_student)
                        self.student_connector.delete_data(self.parameters_student, "gradebook", pk_gradebook)
                        self.student_connector.close_connection()
                        if self.parameters_student.error != "default":
                            self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
                        else:
                            self.show_messagebox("information", "Information", "Запись успешно удалена")
                            self.get_settings_student()
                            self.display_table_students()
                    except Exception:
                        self.show_messagebox("critical", "Critical", str(self.parameters_student.error))
        except Exception as error:
            print("Error: ", error)
            self.student_connector.close_connection()

    '''------------------------------------------------------------------------------------------------------'''

    def show_settings_group(self):
        self.set_group_win.show()

    def get_settings_group(self):
        self.parameters_group.clear_list()
        self.parameters_group.current_len_lcn = 0
        if self.set_group_win.ui.checkBox_number_group.isChecked():
            self.parameters_group.list_checkBoxes.append("group_id")
            self.parameters_group.list_columns_name.append("Номер группы")
            self.parameters_group.current_len_lcn += 1
        if self.set_group_win.ui.checkBox_direction_training.isChecked():
            self.parameters_group.list_checkBoxes.append("direction_of_training")
            self.parameters_group.list_columns_name.append("Уровень обучения")
            self.parameters_group.current_len_lcn += 1
        if self.set_group_win.ui.checkBox_course.isChecked():
            self.parameters_group.list_checkBoxes.append("course")
            self.parameters_group.list_columns_name.append("Курс")
            self.parameters_group.current_len_lcn += 1

    def hide_settings_group(self):
        self.get_settings_group()
        self.set_group_win.hide()

    def select_groups(self, column=None, value=None):
        try:
            self.group_connector.create_connection(self.parameters_student)
            if (column is None) and (value is None):
                if len(self.parameters_group.list_checkBoxes) == 3:
                    self.parameters_group.result_select = self.group_connector.select_data(self.parameters_group)
                    self.parameters_group.all_columns = True
                    print("selected all")
                else:
                    self.parameters_group.result_select = self.group_connector.select_data(self.parameters_group,
                                                                                           self.parameters_group.list_checkBoxes)
                    self.parameters_group.all_columns = False
                    print("selected with parameters")
                self.parameters_group.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_group.list_checkBoxes) == 3:
                    self.parameters_group.result_select = self.group_connector.select_filtered_data(self.parameters_group,
                                                                                                    column, value)
                    self.parameters_group.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_group.result_select = self.group_connector.select_filtered_data(self.parameters_group,
                                                                                    column,
                                                                                    value,
                                                                                    self.parameters_group.list_checkBoxes)
                    self.parameters_group.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_group.last_display = "filtered"
            self.group_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_group.error))

    def display_table_groups(self):
        self.select_groups()
        if self.parameters_group.first_show:
            self.get_settings_group()
            self.parameters_group.first_show = False

        for i in range(self.ui.tableWidgetGroup.rowCount()):
            self.ui.tableWidgetGroup.removeColumn(i)

        data = self.parameters_group.result_select

        numrows = len(data)
        numcolumns = len(self.parameters_group.list_columns_name)
        self.ui.tableWidgetGroup.setColumnCount(numcolumns)
        self.ui.tableWidgetGroup.setHorizontalHeaderLabels(self.parameters_group.list_columns_name)
        self.ui.tableWidgetGroup.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetGroup.setColumnWidth(0, 150)
            self.ui.tableWidgetGroup.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetGroup.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetGroup.setItem(row, column,
                                                     QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetGroup.setItem(row, column,
                                                     QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_groups(self):
        db_column = self.parameters_group.dict_combo_box[self.ui.comboBoxValueSearchColumnGroup.currentText()]
        search_text = self.ui.lineEditSearchValueGroup.text().strip()

        self.select_groups(db_column, search_text)

        for i in range(self.ui.tableWidgetGroup.rowCount()):
            self.ui.tableWidgetGroup.removeColumn(i)

        data = self.parameters_group.result_select
        numrows = len(data)
        numcolumns = len(self.parameters_group.list_columns_name)
        self.ui.tableWidgetGroup.setColumnCount(numcolumns)
        self.ui.tableWidgetGroup.setHorizontalHeaderLabels(self.parameters_group.list_columns_name)
        self.ui.tableWidgetGroup.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetGroup.setColumnWidth(0, 150)
            self.ui.tableWidgetGroup.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetGroup.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetGroup.setItem(row, column,
                                                     QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetGroup.setItem(row, column,
                                                     QtWidgets.QTableWidgetItem((data[row][column])))

    def show_add_group(self):
        self.add_group_win.show()
        self.add_group_win.ui.lineEditNumberGroup.setText("")
        self.add_group_win.ui.lineEditDirectionTraining.setText("")
        self.add_group_win.ui.lineEditCourse.setText("")

    def insert_group(self):
        try:
            if len(self.add_group_win.ui.lineEditNumberGroup.text().strip()) == 0:
                print("Incorrect number group")
                self.show_messagebox("warning", "Warning", "Пустой номер группы")
                return False
            else:
                self.parameters_group.error = "default"
                try:
                    self.group_connector.create_connection(self.parameters_group)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
                self.group_connector.insert_data(
                                                self.parameters_group,
                                                group_id=self.add_group_win.ui.lineEditNumberGroup.text().strip(),
                                                direction_of_training=self.add_group_win.ui.lineEditDirectionTraining.text().strip(),
                                                course=self.add_group_win.ui.lineEditCourse.text().strip(),
                                                )
                self.group_connector.close_connection()
                if self.parameters_group.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
                    return False
                return True
        except Exception as error:
            print("Error: ", error)
            self.group_connector.close_connection()
            return False

    def hide_insert_group(self):
        insert_return = self.insert_group()
        if insert_return:
            self.add_group_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно добавлена")
            self.get_settings_group()
            self.display_table_groups()

    def show_edit_group(self):
        if self.parameters_group.first_show:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи таблицы")
        elif self.parameters_group.current_len_lcn != self.parameters_group.static_len_lcn:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "настроить отображение всех столбцов")
        elif not self.parameters_group.all_columns:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи после настройки столбцов")
        elif self.ui.tableWidgetGroup.currentRow() == -1:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "выбрать запись в таблице")
        else:
            self.edit_group_win.show()
            current_row = self.ui.tableWidgetGroup.currentRow()
            self.parameters_group.pk["group_id"] = self.ui.tableWidgetGroup.item(current_row, 0).text()
            self.list_group_data = [self.ui.tableWidgetGroup.item(current_row, i).text()
                                    for i in range(self.parameters_group.static_len_lcn)]
            self.list_group_changed_data = [self.edit_group_win.ui.lineEditNumberGroup,
                                            self.edit_group_win.ui.lineEditDirectionTraining,
                                            self.edit_group_win.ui.lineEditCourse]

            for i in range(self.parameters_group.static_len_lcn):
                self.list_group_changed_data[i].setText(self.list_group_data[i])

    def comparison_values_group(self):
        self.parameters_group.clear_dict()
        for i in range(self.parameters_group.static_len_lcn):
            if self.list_group_data[i] != self.list_group_changed_data[i].text().strip():
                self.parameters_group.dict_changed_data[self.parameters_group.list_checkBoxes[i]] \
                                                                        = self.list_group_changed_data[i].text()

    def edit_group(self):
        try:
            if len(self.edit_group_win.ui.lineEditNumberGroup.text().strip()) == 0:
                print("Incorrect number group")
                self.show_messagebox("warning", "Warning", "Пустой номер группы")
                return False
            else:
                self.parameters_group.error = "default"
                self.comparison_values_group()
                if len(self.parameters_group.dict_changed_data) == 0:
                    self.show_messagebox("information", "Information", "Изменений не обнаружено")
                    return False
                try:
                    self.group_connector.create_connection(self.parameters_student)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
                self.group_connector.update_data(self.parameters_group,
                                                 self.parameters_group.pk,
                                                 self.parameters_group.dict_changed_data)
                self.group_connector.close_connection()
                if self.parameters_group.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
                    return False
            return True
        except Exception as error:
            print("Error: ", error)
            self.group_connector.close_connection()
            return False

    def hide_edit_group(self):
        edit_return = self.edit_group()
        if edit_return:
            self.edit_group_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно отредактирована")
            self.get_settings_group()
            print(self.parameters_group.last_display)
            if self.parameters_group.last_display == "all":
                self.display_table_groups()
            elif self.parameters_group.last_display == "filtered":
                self.display_filtered_table_groups()

    def delete_group(self):
        try:
            if self.parameters_group.first_show:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести записи таблицы")
            elif "group_id" not in set(self.parameters_group.list_checkBoxes):
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "настроить отображение номера зачётной книжки")
            elif self.ui.tableWidgetGroup.horizontalHeaderItem(0).text() != "Номер группы":
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести номер зачётной книжки")
            elif self.ui.tableWidgetGroup.currentRow() == -1:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "выбрать запись в таблице")
            else:
                self.parameters_group.error = "default"
                current_row = self.ui.tableWidgetGroup.currentRow()
                pk_group_id = self.ui.tableWidgetGroup.item(current_row, 0).text()
                msg_box = QMessageBox.question(self, "Подтверждение удаления",
                                               f"Вы хотите удалить группу с \nномером {pk_group_id}?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg_box == QMessageBox.Yes:
                    try:
                        self.group_connector.create_connection(self.parameters_group)
                        self.group_connector.delete_data(self.parameters_group, "group_id", pk_group_id)
                        self.group_connector.close_connection()
                        if self.parameters_group.error != "default":
                            self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
                        else:
                            self.show_messagebox("information", "Information", "Запись успешно удалена")
                            self.get_settings_group()
                            self.display_table_groups()
                    except Exception:
                        self.show_messagebox("critical", "Critical", str(self.parameters_group.error))
        except Exception as error:
            print("Error: ", error)
            self.group_connector.close_connection()

    '''------------------------------------------------------------------------------------------------------'''

    def show_settings_subject(self):
        self.set_subject_win.show()

    def get_settings_subject(self):
        self.parameters_subject.clear_list()
        self.parameters_subject.current_len_lcn = 0
        if self.set_subject_win.ui.checkBox_id_subject.isChecked():
            self.parameters_subject.list_checkBoxes.append("id")
            self.parameters_subject.list_columns_name.append("Id предмета")
            self.parameters_subject.current_len_lcn += 1
        if self.set_subject_win.ui.checkBox_name_subject.isChecked():
            self.parameters_subject.list_checkBoxes.append("name")
            self.parameters_subject.list_columns_name.append("Название предмета")
            self.parameters_subject.current_len_lcn += 1

    def hide_settings_subject(self):
        self.get_settings_subject()
        self.set_subject_win.hide()

    def select_subjects(self, column=None, value=None):
        try:
            self.subject_connector.create_connection(self.parameters_subject)
            if (column is None) and (value is None):
                if len(self.parameters_subject.list_checkBoxes) == 2:
                    self.parameters_subject.result_select = self.subject_connector.select_data(self.parameters_subject)
                    self.parameters_subject.all_columns = True
                    print("selected all")
                else:
                    self.parameters_subject.result_select = self.subject_connector.select_data(self.parameters_subject,
                                                                                               self.parameters_subject.list_checkBoxes)
                    self.parameters_subject.all_columns = False
                    print("selected with parameters")
                self.parameters_subject.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_subject.list_checkBoxes) == 2:
                    self.parameters_subject.result_select = self.subject_connector.select_filtered_data(self.parameters_subject,
                                                                                                        column, value)
                    self.parameters_subject.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_subject.result_select = self.subject_connector.select_filtered_data(self.parameters_subject,
                                                                                    column,
                                                                                    value,
                                                                                    self.parameters_subject.list_checkBoxes)
                    self.parameters_subject.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_subject.last_display = "filtered"
            self.subject_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))

    def display_table_subjects(self):
        self.select_subjects()
        if self.parameters_subject.first_show:
            self.get_settings_subject()
            self.parameters_subject.first_show = False

        for i in range(self.ui.tableWidgetSubject.rowCount()):
            self.ui.tableWidgetSubject.removeColumn(i)

        data = self.parameters_subject.result_select

        numrows = len(data)
        numcolumns = len(self.parameters_subject.list_columns_name)
        self.ui.tableWidgetSubject.setColumnCount(numcolumns)
        self.ui.tableWidgetSubject.setHorizontalHeaderLabels(self.parameters_subject.list_columns_name)
        self.ui.tableWidgetSubject.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetSubject.setColumnWidth(0, 150)
            self.ui.tableWidgetSubject.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetSubject.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetSubject.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetSubject.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_subjects(self):
        db_column = self.parameters_subject.dict_combo_box[self.ui.comboBoxValueSearchColumnSubject.currentText()]
        search_text = self.ui.lineEditSearchValueSubject.text().strip()

        self.select_subjects(db_column, search_text)

        for i in range(self.ui.tableWidgetSubject.rowCount()):
            self.ui.tableWidgetSubject.removeColumn(i)

        data = self.parameters_subject.result_select
        numrows = len(data)
        numcolumns = len(self.parameters_subject.list_columns_name)
        self.ui.tableWidgetSubject.setColumnCount(numcolumns)
        self.ui.tableWidgetSubject.setHorizontalHeaderLabels(self.parameters_subject.list_columns_name)
        self.ui.tableWidgetSubject.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetSubject.setColumnWidth(0, 150)
            self.ui.tableWidgetSubject.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetSubject.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetSubject.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetSubject.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def show_add_subject(self):
        self.add_subject_win.show()
        self.add_subject_win.ui.lineEditIdSubject.setText("")
        self.add_subject_win.ui.lineEditNameSubject.setText("")

    def insert_subject(self):
        try:
            if len(self.add_subject_win.ui.lineEditIdSubject.text().strip()) == 0:
                print("Incorrect id subject")
                self.show_messagebox("warning", "Warning", "Пустой id предмета")
                return False
            else:
                self.parameters_subject.error = "default"
                try:
                    self.subject_connector.create_connection(self.parameters_subject)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
                self.subject_connector.insert_data(
                                                self.parameters_subject,
                                                id=self.add_subject_win.ui.lineEditIdSubject.text().strip(),
                                                name=self.add_subject_win.ui.lineEditNameSubject.text().strip(),
                                                )
                self.subject_connector.close_connection()
                if self.parameters_subject.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
                    return False
                return True
        except Exception as error:
            print("Error: ", error)
            self.subject_connector.close_connection()
            return False

    def hide_insert_subject(self):
        insert_return = self.insert_subject()
        if insert_return:
            self.add_subject_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно добавлена")
            self.get_settings_subject()
            self.display_table_subjects()

    def show_edit_subject(self):
        if self.parameters_subject.first_show:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи таблицы")
        elif self.parameters_subject.current_len_lcn != self.parameters_subject.static_len_lcn:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "настроить отображение всех столбцов")
        elif not self.parameters_subject.all_columns:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи после настройки столбцов")
        elif self.ui.tableWidgetSubject.currentRow() == -1:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "выбрать запись в таблице")
        else:
            self.edit_subject_win.show()
            current_row = self.ui.tableWidgetSubject.currentRow()
            self.parameters_subject.pk["id"] = self.ui.tableWidgetSubject.item(current_row, 0).text()
            self.list_subject_data = [self.ui.tableWidgetSubject.item(current_row, i).text()
                                      for i in range(self.parameters_subject.static_len_lcn)]
            self.list_subject_changed_data = [self.edit_subject_win.ui.lineEditIdSubject,
                                              self.edit_subject_win.ui.lineEditNameSubject]

            for i in range(self.parameters_subject.static_len_lcn):
                self.list_subject_changed_data[i].setText(self.list_subject_data[i])

    def comparison_values_subject(self):
        self.parameters_subject.clear_dict()
        for i in range(self.parameters_subject.static_len_lcn):
            if self.list_subject_data[i] != self.list_subject_changed_data[i].text().strip():
                self.parameters_subject.dict_changed_data[self.parameters_subject.list_checkBoxes[i]] \
                                                                        = self.list_subject_changed_data[i].text()

    def edit_subject(self):
        try:
            if len(self.edit_subject_win.ui.lineEditIdSubject.text().strip()) == 0:
                print("Incorrect id subject")
                self.show_messagebox("warning", "Warning", "Пустой id предмета")
                return False
            else:
                self.parameters_subject.error = "default"
                self.comparison_values_subject()
                if len(self.parameters_subject.dict_changed_data) == 0:
                    self.show_messagebox("information", "Information", "Изменений не обнаружено")
                    return False
                try:
                    self.subject_connector.create_connection(self.parameters_student)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
                self.subject_connector.update_data(self.parameters_subject,
                                                   self.parameters_subject.pk,
                                                   self.parameters_subject.dict_changed_data)
                self.subject_connector.close_connection()
                if self.parameters_subject.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
                    return False
            return True
        except Exception as error:
            print("Error: ", error)
            self.subject_connector.close_connection()
            return False

    def hide_edit_subject(self):
        edit_return = self.edit_subject()
        if edit_return:
            self.edit_subject_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно отредактирована")
            self.get_settings_subject()
            print(self.parameters_subject.last_display)
            if self.parameters_subject.last_display == "all":
                self.display_table_subjects()
            elif self.parameters_subject.last_display == "filtered":
                self.display_filtered_table_subjects()

    def delete_subject(self):
        try:
            if self.parameters_subject.first_show:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести записи таблицы")
            elif "id" not in set(self.parameters_subject.list_checkBoxes):
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "настроить отображение id предмета")
            elif self.ui.tableWidgetSubject.horizontalHeaderItem(0).text() != "Id предмета":
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести номер зачётной книжки")
            elif self.ui.tableWidgetSubject.currentRow() == -1:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "выбрать запись в таблице")
            else:
                self.parameters_subject.error = "default"
                current_row = self.ui.tableWidgetSubject.currentRow()
                pk_subject_id = self.ui.tableWidgetSubject.item(current_row, 0).text()
                msg_box = QMessageBox.question(self, "Подтверждение удаления",
                                               f"Вы хотите удалить предмет\nс id {pk_subject_id}?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg_box == QMessageBox.Yes:
                    try:
                        self.subject_connector.create_connection(self.parameters_subject)
                        self.subject_connector.delete_data(self.parameters_subject, "id", pk_subject_id)
                        self.subject_connector.close_connection()
                        if self.parameters_subject.error != "default":
                            self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
                        else:
                            self.show_messagebox("information", "Information", "Запись успешно удалена")
                            self.get_settings_subject()
                            self.display_table_subjects()
                    except Exception:
                        self.show_messagebox("critical", "Critical", str(self.parameters_subject.error))
        except Exception as error:
            print("Error: ", error)
            self.subject_connector.close_connection()

    '''------------------------------------------------------------------------------------------------------'''

    def show_settings_scholarship(self):
        self.set_scholarship_win.show()

    def get_settings_scholarship(self):
        self.parameters_scholarship.clear_list()
        self.parameters_scholarship.current_len_lcn = 0
        if self.set_scholarship_win.ui.checkBox_id_scholarship.isChecked():
            self.parameters_scholarship.list_checkBoxes.append("id")
            self.parameters_scholarship.list_columns_name.append("Id стипендии")
            self.parameters_scholarship.current_len_lcn += 1
        if self.set_scholarship_win.ui.checkBox_name_scholarship.isChecked():
            self.parameters_scholarship.list_checkBoxes.append("name")
            self.parameters_scholarship.list_columns_name.append("Название стипендии")
            self.parameters_scholarship.current_len_lcn += 1
        if self.set_scholarship_win.ui.checkBox_amount.isChecked():
            self.parameters_scholarship.list_checkBoxes.append("amount")
            self.parameters_scholarship.list_columns_name.append("Размер")
            self.parameters_scholarship.current_len_lcn += 1

    def hide_settings_scholarship(self):
        self.get_settings_scholarship()
        self.set_scholarship_win.hide()

    def select_scholarships(self, column=None, value=None):
        try:
            self.scholarship_connector.create_connection(self.parameters_scholarship)
            if (column is None) and (value is None):
                if len(self.parameters_scholarship.list_checkBoxes) == 3:
                    self.parameters_scholarship.result_select = self.scholarship_connector.select_data(self.parameters_scholarship)
                    self.parameters_scholarship.all_columns = True
                    print("selected all")
                else:
                    self.parameters_scholarship.result_select = self.scholarship_connector.select_data(self.parameters_scholarship,
                                                                                               self.parameters_scholarship.list_checkBoxes)
                    self.parameters_scholarship.all_columns = False
                    print("selected with parameters")
                self.parameters_scholarship.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_scholarship.list_checkBoxes) == 3:
                    self.parameters_scholarship.result_select = self.scholarship_connector.select_filtered_data(self.parameters_scholarship,
                                                                                                        column, value)
                    self.parameters_scholarship.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_scholarship.result_select = self.scholarship_connector.select_filtered_data(self.parameters_scholarship,
                                                                                    column,
                                                                                    value,
                                                                                    self.parameters_scholarship.list_checkBoxes)
                    self.parameters_scholarship.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_scholarship.last_display = "filtered"
            self.scholarship_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))

    def display_table_scholarships(self):
        self.select_scholarships()
        if self.parameters_scholarship.first_show:
            self.get_settings_scholarship()
            self.parameters_scholarship.first_show = False

        for i in range(self.ui.tableWidgetScholarship.rowCount()):
            self.ui.tableWidgetScholarship.removeColumn(i)

        data = self.parameters_scholarship.result_select

        numrows = len(data)
        numcolumns = len(self.parameters_scholarship.list_columns_name)
        self.ui.tableWidgetScholarship.setColumnCount(numcolumns)
        self.ui.tableWidgetScholarship.setHorizontalHeaderLabels(self.parameters_scholarship.list_columns_name)
        self.ui.tableWidgetScholarship.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetScholarship.setColumnWidth(0, 150)
            self.ui.tableWidgetScholarship.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetScholarship.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetScholarship.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetScholarship.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_scholarships(self):
        db_column = self.parameters_scholarship.dict_combo_box[self.ui.comboBoxValueSearchColumnScholarship.currentText()]
        search_text = self.ui.lineEditSearchValueScholarship.text().strip()

        self.select_scholarships(db_column, search_text)

        for i in range(self.ui.tableWidgetSubject.rowCount()):
            self.ui.tableWidgetScholarship.removeColumn(i)

        data = self.parameters_scholarship.result_select
        numrows = len(data)
        numcolumns = len(self.parameters_scholarship.list_columns_name)
        self.ui.tableWidgetScholarship.setColumnCount(numcolumns)
        self.ui.tableWidgetScholarship.setHorizontalHeaderLabels(self.parameters_scholarship.list_columns_name)
        self.ui.tableWidgetScholarship.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetScholarship.setColumnWidth(0, 150)
            self.ui.tableWidgetScholarship.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetScholarship.setItem(row, column, QtWidgets.QTableWidgetItem(
                                                                    (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetScholarship.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetScholarship.setItem(row, column,
                                                       QtWidgets.QTableWidgetItem((data[row][column])))

    def show_add_scholarship(self):
        self.add_scholarship_win.show()
        self.add_scholarship_win.ui.lineEditIdScholarship.setText("")
        self.add_scholarship_win.ui.lineEditNameScholarship.setText("")
        self.add_scholarship_win.ui.lineEditAmount.setText("")

    def insert_scholarship(self):
        try:
            if len(self.add_scholarship_win.ui.lineEditIdScholarship.text().strip()) == 0:
                print("Incorrect id scholarship")
                self.show_messagebox("warning", "Warning", "Пустой id стипендии")
                return False
            else:
                self.parameters_scholarship.error = "default"
                try:
                    self.scholarship_connector.create_connection(self.parameters_scholarship)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
                self.scholarship_connector.insert_data(
                                                self.parameters_scholarship,
                                                id=self.add_scholarship_win.ui.lineEditIdScholarship.text().strip(),
                                                name=self.add_scholarship_win.ui.lineEditNameScholarship.text().strip(),
                                                amount=self.add_scholarship_win.ui.lineEditAmount.text().strip(),
                                                )
                self.scholarship_connector.close_connection()
                if self.parameters_scholarship.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
                    return False
                return True
        except Exception as error:
            print("Error: ", error)
            self.scholarship_connector.close_connection()
            return False

    def hide_insert_scholarship(self):
        insert_return = self.insert_scholarship()
        if insert_return:
            self.add_scholarship_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно добавлена")
            self.get_settings_scholarship()
            self.display_table_scholarships()

    def show_edit_scholarship(self):
        if self.parameters_scholarship.first_show:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи таблицы")
        elif self.parameters_scholarship.current_len_lcn != self.parameters_scholarship.static_len_lcn:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "настроить отображение всех столбцов")
        elif not self.parameters_scholarship.all_columns:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи после настройки столбцов")
        elif self.ui.tableWidgetScholarship.currentRow() == -1:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "выбрать запись в таблице")
        else:
            self.edit_scholarship_win.show()
            current_row = self.ui.tableWidgetScholarship.currentRow()
            self.parameters_scholarship.pk["id"] = self.ui.tableWidgetScholarship.item(current_row, 0).text()
            self.list_scholarship_data = [self.ui.tableWidgetScholarship.item(current_row, i).text()
                                          for i in range(self.parameters_scholarship.static_len_lcn)]
            self.list_scholarship_changed_data = [self.edit_scholarship_win.ui.lineEditIdScholarship,
                                                  self.edit_scholarship_win.ui.lineEditNameScholarship,
                                                  self.edit_scholarship_win.ui.lineEditAmount]

            for i in range(self.parameters_scholarship.static_len_lcn):
                self.list_scholarship_changed_data[i].setText(self.list_scholarship_data[i])

    def comparison_values_scholarship(self):
        self.parameters_scholarship.clear_dict()
        for i in range(self.parameters_scholarship.static_len_lcn):
            if self.list_scholarship_data[i] != self.list_scholarship_changed_data[i].text().strip():
                self.parameters_scholarship.dict_changed_data[self.parameters_scholarship.list_checkBoxes[i]] \
                                                                        = self.list_scholarship_changed_data[i].text()

    def edit_scholarship(self):
        try:
            if len(self.edit_scholarship_win.ui.lineEditIdScholarship.text().strip()) == 0:
                print("Incorrect id scholarship")
                self.show_messagebox("warning", "Warning", "Пустой id стипендии")
                return False
            else:
                self.parameters_scholarship.error = "default"
                self.comparison_values_scholarship()
                if len(self.parameters_scholarship.dict_changed_data) == 0:
                    self.show_messagebox("information", "Information", "Изменений не обнаружено")
                    return False
                try:
                    self.scholarship_connector.create_connection(self.parameters_scholarship)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
                self.scholarship_connector.update_data(self.parameters_scholarship,
                                                       self.parameters_scholarship.pk,
                                                       self.parameters_scholarship.dict_changed_data)
                self.scholarship_connector.close_connection()
                if self.parameters_scholarship.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
                    return False
            return True
        except Exception as error:
            print("Error: ", error)
            self.scholarship_connector.close_connection()
            return False

    def hide_edit_scholarship(self):
        edit_return = self.edit_scholarship()
        if edit_return:
            self.edit_scholarship_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно отредактирована")
            self.get_settings_scholarship()
            print(self.parameters_scholarship.last_display)
            if self.parameters_scholarship.last_display == "all":
                self.display_table_scholarships()
            elif self.parameters_scholarship.last_display == "filtered":
                self.display_filtered_table_scholarships()

    def delete_scholarship(self):
        try:
            if self.parameters_scholarship.first_show:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести записи таблицы")
            elif "id" not in set(self.parameters_scholarship.list_checkBoxes):
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "настроить отображение id предмета")
            elif self.ui.tableWidgetScholarship.horizontalHeaderItem(0).text() != "Id стипендии":
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести id стипендии")
            elif self.ui.tableWidgetScholarship.currentRow() == -1:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "выбрать запись в таблице")
            else:
                self.parameters_scholarship.error = "default"
                current_row = self.ui.tableWidgetScholarship.currentRow()
                pk_scholarship_id = self.ui.tableWidgetScholarship.item(current_row, 0).text()
                msg_box = QMessageBox.question(self, "Подтверждение удаления",
                                               f"Вы хотите удалить стипендию\nс id {pk_scholarship_id}?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg_box == QMessageBox.Yes:
                    try:
                        self.scholarship_connector.create_connection(self.parameters_scholarship)
                        self.scholarship_connector.delete_data(self.parameters_subject, "id", pk_scholarship_id)
                        self.scholarship_connector.close_connection()
                        if self.parameters_scholarship.error != "default":
                            self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
                        else:
                            self.show_messagebox("information", "Information", "Запись успешно удалена")
                            self.get_settings_scholarship()
                            self.display_table_scholarships()
                    except Exception:
                        self.show_messagebox("critical", "Critical", str(self.parameters_scholarship.error))
        except Exception as error:
            print("Error: ", error)
            self.scholarship_connector.close_connection()

    '''------------------------------------------------------------------------------------------------------'''

    def show_settings_debt(self):
        self.set_debt_win.show()

    def get_settings_debt(self):
        self.parameters_debt.clear_list()
        self.parameters_debt.current_len_lcn = 0
        if self.set_debt_win.ui.checkBox_id_debt.isChecked():
            self.parameters_debt.list_checkBoxes.append("id")
            self.parameters_debt.list_columns_name.append("Id долга")
            self.parameters_debt.current_len_lcn += 1
        if self.set_debt_win.ui.checkBox_gradebook.isChecked():
            self.parameters_debt.list_checkBoxes.append("student_id")
            self.parameters_debt.list_columns_name.append("Номер зачётки студента")
            self.parameters_debt.current_len_lcn += 1
        if self.set_debt_win.ui.checkBox_id_subject.isChecked():
            self.parameters_debt.list_checkBoxes.append("subject_id")
            self.parameters_debt.list_columns_name.append("Id предмета")
            self.parameters_debt.current_len_lcn += 1
        if self.set_debt_win.ui.checkBox_semester.isChecked():
            self.parameters_debt.list_checkBoxes.append("semester")
            self.parameters_debt.list_columns_name.append("Семестр")
            self.parameters_debt.current_len_lcn += 1
        if self.set_debt_win.ui.checkBox_date.isChecked():
            self.parameters_debt.list_checkBoxes.append("date")
            self.parameters_debt.list_columns_name.append("Дата")
            self.parameters_debt.current_len_lcn += 1

    def hide_settings_debt(self):
        self.get_settings_debt()
        self.set_debt_win.hide()

    def select_debt(self, column=None, value=None):
        try:
            self.debt_connector.create_connection(self.parameters_debt)
            if (column is None) and (value is None):
                if len(self.parameters_debt.list_checkBoxes) == 5:
                    self.parameters_debt.result_select = self.debt_connector.select_data(
                        self.parameters_debt)
                    self.parameters_debt.all_columns = True
                    print("selected all")
                else:
                    self.parameters_debt.result_select = self.debt_connector.select_data(
                        self.parameters_debt,
                        self.parameters_debt.list_checkBoxes)
                    self.parameters_debt.all_columns = False
                    print("selected with parameters")
                self.parameters_debt.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_debt.list_checkBoxes) == 5:
                    self.parameters_debt.result_select = self.debt_connector.select_filtered_data(
                        self.parameters_debt,
                        column, value)
                    self.parameters_debt.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_debt.result_select = self.debt_connector.select_filtered_data(
                        self.parameters_debt,
                        column,
                        value,
                        self.parameters_debt.list_checkBoxes)
                    self.parameters_debt.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_debt.last_display = "filtered"
            self.debt_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))

    def display_table_debts(self):
        self.select_debt()
        if self.parameters_debt.first_show:
            self.get_settings_debt()
            self.parameters_debt.first_show = False

        for i in range(self.ui.tableWidgetDebt.rowCount()):
            self.ui.tableWidgetDebt.removeColumn(i)

        data = self.parameters_debt.result_select

        numrows = len(data)
        numcolumns = len(self.parameters_debt.list_columns_name)
        self.ui.tableWidgetDebt.setColumnCount(numcolumns)
        self.ui.tableWidgetDebt.setHorizontalHeaderLabels(self.parameters_debt.list_columns_name)
        self.ui.tableWidgetDebt.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetDebt.setColumnWidth(0, 150)
            self.ui.tableWidgetDebt.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetDebt.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetDebt.setItem(row, column,
                                                           QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetDebt.setItem(row, column,
                                                           QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_debts(self):
        db_column = self.parameters_debt.dict_combo_box[
            self.ui.comboBoxValueSearchColumnScholarship.currentText()]
        search_text = self.ui.lineEditSearchValueDebt.text().strip()

        self.select_debt(db_column, search_text)

        for i in range(self.ui.tableWidgetDebt.rowCount()):
            self.ui.tableWidgetDebt.removeColumn(i)

        data = self.parameters_debt.result_select
        numrows = len(data)
        numcolumns = len(self.parameters_debt.list_columns_name)
        self.ui.tableWidgetDebt.setColumnCount(numcolumns)
        self.ui.tableWidgetDebt.setHorizontalHeaderLabels(self.parameters_debt.list_columns_name)
        self.ui.tableWidgetDebt.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetDebt.setColumnWidth(0, 150)
            self.ui.tableWidgetDebt.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetDebt.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetDebt.setItem(row, column,
                                                           QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetDebt.setItem(row, column,
                                                           QtWidgets.QTableWidgetItem((data[row][column])))

    def show_add_debt(self):
        self.add_debt_win.show()
        self.add_debt_win.ui.lineEditGradebook.setText("")
        self.add_debt_win.ui.lineEditIdSubject.setText("")
        self.add_debt_win.ui.lineEditSemester.setText("")
        self.add_debt_win.ui.lineEditDate.setText("")

    def insert_debt(self):
        getted_date = self.add_debt_win.ui.lineEditDate.text().replace(" ", "")
        checked_date = self.check_valid_date(getted_date)
        try:
            if len(self.add_debt_win.ui.lineEditGradebook.text().strip()) == 0:
                print("Incorrect gradebook")
                self.show_messagebox("warning", "Warning", "Пустой номер\nзачётной книжки")
                return False
            elif len(self.add_debt_win.ui.lineEditIdSubject.text().strip()) == 0:
                print("Incorrect subject_id")
                self.show_messagebox("warning", "Warning", "Пустой номер\nid предмета")
                return False
            elif checked_date != 0:
                return False
            else:
                self.parameters_debt.error = "default"
                custom_date = getted_date[6:10] + "-" + getted_date[3:5] + "-" + getted_date[0:2]
                try:
                    self.debt_connector.create_connection(self.parameters_debt)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
                self.debt_connector.insert_data(
                    self.parameters_debt,
                    student_id=self.add_debt_win.ui.lineEditGradebook.text().strip(),
                    subject_id=self.add_debt_win.ui.lineEditIdSubject.text().strip(),
                    semester=self.add_debt_win.ui.lineEditSemester.text().strip(),
                    date=custom_date,
                )
                self.debt_connector.close_connection()
                if self.parameters_debt.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
                    return False
                return True
        except Exception as error:
            print("Error: ", error)
            self.debt_connector.close_connection()
            return False

    def hide_insert_debt(self):
        insert_return = self.insert_debt()
        if insert_return:
            self.add_debt_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно добавлена")
            self.get_settings_debt()
            self.display_table_debts()

    def show_edit_debt(self):
        if self.parameters_debt.first_show:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи таблицы")
        elif self.parameters_debt.current_len_lcn != self.parameters_debt.static_len_lcn:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "настроить отображение всех столбцов")
        elif not self.parameters_debt.all_columns:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "вывести записи после настройки столбцов")
        elif self.ui.tableWidgetDebt.currentRow() == -1:
            self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                       "выбрать запись в таблице")
        else:
            self.edit_debt_win.show()
            current_row = self.ui.tableWidgetDebt.currentRow()
            self.parameters_debt.pk["id"] = self.ui.tableWidgetDebt.item(current_row, 0).text()
            self.list_debt_data = [self.ui.tableWidgetDebt.item(current_row, i).text()
                                   for i in range(1, self.parameters_debt.static_len_lcn)]
            self.list_debt_changed_data = [self.edit_debt_win.ui.lineEditGradebook,
                                           self.edit_debt_win.ui.lineEditIdSubject,
                                           self.edit_debt_win.ui.lineEditSemester,
                                           self.edit_debt_win.ui.lineEditDate]

            for i in range(self.parameters_debt.static_len_lcn - 1):
                self.list_debt_changed_data[i].setText(self.list_debt_data[i])

    def comparison_values_debt(self):
        self.parameters_debt.clear_dict()
        for i in range(self.parameters_debt.static_len_lcn - 1):
            if self.list_scholarship_data[i] != self.list_scholarship_changed_data[i].text().strip():
                self.parameters_debt.dict_changed_data[self.parameters_debt.list_checkBoxes[i]] \
                    = self.list_debt_changed_data[i].text()

    def edit_debt(self):
        try:
            if len(self.edit_debt_win.ui.lineEditGradebook.text().strip()) == 0:
                print("Incorrect id debt")
                self.show_messagebox("warning", "Warning", "Пустой номер зачётки")
                return False
            else:
                self.parameters_debt.error = "default"
                self.comparison_values_debt()
                if len(self.parameters_debt.dict_changed_data) == 0:
                    self.show_messagebox("information", "Information", "Изменений не обнаружено")
                    return False
                try:
                    self.debt_connector.create_connection(self.parameters_debt)
                except Exception:
                    self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
                self.debt_connector.update_data(self.parameters_debt,
                                                self.parameters_debt.pk,
                                                self.parameters_debt.dict_changed_data)
                self.debt_connector.close_connection()
                if self.parameters_debt.error != "default":
                    self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
                    return False
            return True
        except Exception as error:
            print("Error: ", error)
            self.debt_connector.close_connection()
            return False

    def hide_edit_debt(self):
        edit_return = self.edit_debt()
        if edit_return:
            self.edit_debt_win.hide()
            self.show_messagebox("information", "Information", "Запись успешно отредактирована")
            self.get_settings_debt()
            print(self.parameters_debt.last_display)
            if self.parameters_debt.last_display == "all":
                self.display_table_debts()
            elif self.parameters_debt.last_display == "filtered":
                self.display_filtered_table_debts()

    def delete_debt(self):
        try:
            if self.parameters_debt.first_show:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести записи таблицы")
            elif "id" not in set(self.parameters_debt.list_checkBoxes):
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "настроить отображение id предмета")
            elif self.ui.tableWidgetDebt.horizontalHeaderItem(0).text() != "Id долга":
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "вывести номер долга")
            elif self.ui.tableWidgetDebt.currentRow() == -1:
                self.show_messagebox("warning", "Warning", "Для выполнения операции необходимо\n"
                                                           "выбрать запись в таблице")
            else:
                self.parameters_debt.error = "default"
                current_row = self.ui.tableWidgetDebt.currentRow()
                pk_debt_id = self.ui.tableWidgetDebt.item(current_row, 0).text()
                msg_box = QMessageBox.question(self, "Подтверждение удаления",
                                               f"Вы хотите удалить группу с \nномером {pk_debt_id}?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg_box == QMessageBox.Yes:
                    try:
                        self.debt_connector.create_connection(self.parameters_scholarship)
                        self.debt_connector.delete_data(self.parameters_debt, "id", pk_debt_id)
                        self.debt_connector.close_connection()
                        if self.parameters_debt.error != "default":
                            self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
                        else:
                            self.show_messagebox("information", "Information", "Запись успешно удалена")
                            self.get_settings_debt()
                            self.display_table_debts()
                    except Exception:
                        self.show_messagebox("critical", "Critical", str(self.parameters_debt.error))
        except Exception as error:
            print("Error: ", error)
            self.debt_connector.close_connection()
