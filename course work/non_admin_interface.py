import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from DBNonAdminInterface import Ui_MainWindow
from pop_up_windows.settings_student import Ui_studentForm
from pop_up_windows.settings_group import Ui_groupForm
from pop_up_windows.settings_subject import Ui_subjectForm
from pop_up_windows.settings_scholarship import Ui_scholarshipForm
from pop_up_windows.settings_debt import Ui_debtForm
from pop_up_windows.settings_lt_scholarship import Ui_ltScholarshipForm
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


class SettingsGroup(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsGroup, self).__init__()
        self.ui = Ui_groupForm()
        self.ui.setupUi(self)


class SettingsSubject(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsSubject, self).__init__()
        self.ui = Ui_subjectForm()
        self.ui.setupUi(self)


class SettingsScholarship(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsScholarship, self).__init__()
        self.ui = Ui_scholarshipForm()
        self.ui.setupUi(self)


class SettingsDebt(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsDebt, self).__init__()
        self.ui = Ui_debtForm()
        self.ui.setupUi(self)


class SettingsLTScholarship(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsLTScholarship, self).__init__()
        self.ui = Ui_ltScholarshipForm()
        self.ui.setupUi(self)


class UserMyWindow(QtWidgets.QMainWindow):
    def __init__(self, ext_student, st_conn, ext_group, gr_conn, ext_subject, sub_conn, ext_scholarship, sch_conn,
                 ext_debt, debt_conn, ext_lt_scholarship, lt_sch_conn):
        super(UserMyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagebox = QMessageBox()
        self.student_connector = st_conn
        self.parameters_student = ext_student
        self.list_student_data = []
        self.list_student_changed_data = []
        self.set_student_win = SettingsStudent()
        self.group_connector = gr_conn
        self.parameters_group = ext_group
        self.list_group_data = []
        self.list_group_changed_data = []
        self.set_group_win = SettingsGroup()
        self.subject_connector = sub_conn
        self.parameters_subject = ext_subject
        self.list_subject_data = []
        self.list_subject_changed_data = []
        self.set_subject_win = SettingsSubject()
        self.scholarship_connector = sch_conn
        self.parameters_scholarship = ext_scholarship
        self.list_scholarship_data = []
        self.list_scholarship_changed_data = []
        self.set_scholarship_win = SettingsScholarship()
        self.debt_connector = debt_conn
        self.parameters_debt = ext_debt
        self.list_debt_data = []
        self.list_debt_changed_data = []
        self.set_debt_win = SettingsDebt()
        self.lt_scholarship_connector = lt_sch_conn
        self.parameters_lt_scholarship = ext_lt_scholarship
        self.list_lt_scholarship_data = []
        self.list_lt_scholarship_changed_data = []
        self.set_lt_scholarship_win = SettingsLTScholarship()
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

        self.set_lt_scholarship_win.ui.checkBox_id_appoitment.setChecked(True)
        self.set_lt_scholarship_win.ui.checkBox_id_scholarship.setChecked(True)
        self.set_lt_scholarship_win.ui.checkBox_id_student.setChecked(True)
        self.ui.comboBoxValueSearchColumnLTScholarship.addItems(self.parameters_lt_scholarship.list_combo_box)

    def connect_buttons(self):
        self.ui.pushButtonSettingsColumnsStudent.clicked.connect(self.show_settings_student)
        self.set_student_win.ui.pushButtonApplySettingsStudent.clicked.connect(self.hide_settings_student)
        self.ui.pushButtonDisplayRecordsStudent.clicked.connect(self.display_table_students)
        self.ui.pushButtonSearchValueStudent.clicked.connect(self.display_filtered_table_students)

        self.ui.pushButtonSettingsColumnsGroup.clicked.connect(self.show_settings_group)
        self.set_group_win.ui.pushButtonApplySettingsGroup.clicked.connect(self.hide_settings_group)
        self.ui.pushButtonDisplayRecordsGroup.clicked.connect(self.display_table_groups)
        self.ui.pushButtonSearchValueGroup.clicked.connect(self.display_filtered_table_groups)

        self.ui.pushButtonSettingsColumnsSubject.clicked.connect(self.show_settings_subject)
        self.set_subject_win.ui.pushButtonApplySettingsSubject.clicked.connect(self.hide_settings_subject)
        self.ui.pushButtonDisplayRecordsSubject.clicked.connect(self.display_table_subjects)
        self.ui.pushButtonSearchValueSubject.clicked.connect(self.display_filtered_table_subjects)

        self.ui.pushButtonSettingsColumnsScholarship.clicked.connect(self.show_settings_scholarship)
        self.set_scholarship_win.ui.pushButtonApplySettingsScholarship.clicked.connect(self.hide_settings_scholarship)
        self.ui.pushButtonDisplayRecordsScholarship.clicked.connect(self.display_table_scholarships)
        self.ui.pushButtonSearchValueScholarship.clicked.connect(self.display_filtered_table_scholarships)

        self.ui.pushButtonSettingsColumnsDebt.clicked.connect(self.show_settings_debt)
        self.set_debt_win.ui.pushButtonApplySettingsDebt.clicked.connect(self.hide_settings_debt)
        self.ui.pushButtonDisplayRecordsDebt.clicked.connect(self.display_table_debts)
        self.ui.pushButtonSearchValueDebt.clicked.connect(self.display_filtered_table_debts)

        self.ui.pushButtonSettingsColumnsLTScholarship.clicked.connect(self.show_settings_lt_scholarship)
        self.set_lt_scholarship_win.ui.pushButtonApplySettingsLTScholarship.clicked.connect(self.hide_settings_lt_scholarship)
        self.ui.pushButtonDisplayRecordsLTScholarship.clicked.connect(self.display_table_lt_scholarships)
        self.ui.pushButtonSearchValueLTScholarship.clicked.connect(self.display_filtered_table_lt_scholarships)

    def show_messagebox(self, level, title, text):
        if level == "critical":
            self.messagebox.setIcon(QMessageBox.Critical)
        elif level == "warning":
            self.messagebox.setIcon(QMessageBox.Warning)
        elif level == "information":
            self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.setWindowTitle(title)
        self.messagebox.setText(text)
        self.messagebox.exec()

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
            self.ui.comboBoxValueSearchColumnDebt.currentText()]
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

    '''------------------------------------------------------------------------------------------------------'''

    def show_settings_lt_scholarship(self):
        self.set_lt_scholarship_win.show()

    def get_settings_lt_scholarship(self):
        self.parameters_lt_scholarship.clear_list()
        self.parameters_lt_scholarship.current_len_lcn = 0
        if self.set_lt_scholarship_win.ui.checkBox_id_appoitment.isChecked():
            self.parameters_lt_scholarship.list_checkBoxes.append("id")
            self.parameters_lt_scholarship.list_columns_name.append("Id назначения")
            self.parameters_lt_scholarship.current_len_lcn += 1
        if self.set_lt_scholarship_win.ui.checkBox_id_student.isChecked():
            self.parameters_lt_scholarship.list_checkBoxes.append("student_id")
            self.parameters_lt_scholarship.list_columns_name.append("Номер зачётки студента")
            self.parameters_lt_scholarship.current_len_lcn += 1
        if self.set_lt_scholarship_win.ui.checkBox_id_scholarship.isChecked():
            self.parameters_lt_scholarship.list_checkBoxes.append("scholarship_id")
            self.parameters_lt_scholarship.list_columns_name.append("Id стипендии")
            self.parameters_lt_scholarship.current_len_lcn += 1

    def hide_settings_lt_scholarship(self):
        self.get_settings_lt_scholarship()
        self.set_lt_scholarship_win.hide()

    def select_lt_scholarship(self, column=None, value=None):
        try:
            self.lt_scholarship_connector.create_connection(self.parameters_lt_scholarship)
            if (column is None) and (value is None):
                if len(self.parameters_lt_scholarship.list_checkBoxes) == 3:
                    self.parameters_lt_scholarship.result_select = self.lt_scholarship_connector.select_data(
                        self.parameters_lt_scholarship)
                    self.parameters_lt_scholarship.all_columns = True
                    print("selected all")
                else:
                    self.parameters_lt_scholarship.result_select = self.lt_scholarship_connector.select_data(
                        self.parameters_lt_scholarship,
                        self.parameters_lt_scholarship.list_checkBoxes)
                    self.parameters_lt_scholarship.all_columns = False
                    print("selected with parameters")
                self.parameters_lt_scholarship.last_display = "all"
            elif not (column is None) and not (value is None):
                if len(self.parameters_lt_scholarship.list_checkBoxes) == 3:
                    self.parameters_lt_scholarship.result_select = self.lt_scholarship_connector.select_filtered_data(
                        self.parameters_lt_scholarship,
                        column, value)
                    self.parameters_lt_scholarship.all_columns = True
                    print("selected all(filtered)")
                else:
                    self.parameters_lt_scholarship.result_select = self.lt_scholarship_connector.select_filtered_data(
                        self.parameters_lt_scholarship,
                        column,
                        value,
                        self.parameters_lt_scholarship.list_checkBoxes)
                    self.parameters_lt_scholarship.all_columns = False
                    print("selected with parameters(filtered)")
                self.parameters_lt_scholarship.last_display = "filtered"
            self.lt_scholarship_connector.close_connection()
        except Exception:
            self.show_messagebox("critical", "Critical", str(self.parameters_lt_scholarship.error))

    def display_table_lt_scholarships(self):
        self.select_lt_scholarship()
        if self.parameters_lt_scholarship.first_show:
            self.get_settings_lt_scholarship()
            self.parameters_lt_scholarship.first_show = False

        for i in range(self.ui.tableWidgetLTScholarship.rowCount()):
            self.ui.tableWidgetLTScholarship.removeColumn(i)

        data = self.parameters_lt_scholarship.result_select

        numrows = len(data)
        numcolumns = len(self.parameters_lt_scholarship.list_columns_name)
        self.ui.tableWidgetLTScholarship.setColumnCount(numcolumns)
        self.ui.tableWidgetLTScholarship.setHorizontalHeaderLabels(self.parameters_lt_scholarship.list_columns_name)
        self.ui.tableWidgetLTScholarship.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetLTScholarship.setColumnWidth(0, 150)
            self.ui.tableWidgetLTScholarship.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetLTScholarship.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetLTScholarship.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetLTScholarship.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((data[row][column])))

    def display_filtered_table_lt_scholarships(self):
        db_column = self.parameters_lt_scholarship.dict_combo_box[
            self.ui.comboBoxValueSearchColumnLTScholarship.currentText()]
        search_text = self.ui.lineEditSearchValueLTScholarship.text().strip()

        self.select_lt_scholarship(db_column, search_text)

        for i in range(self.ui.tableWidgetLTScholarship.rowCount()):
            self.ui.tableWidgetLTScholarship.removeColumn(i)

        data = self.parameters_lt_scholarship.result_select
        numrows = len(data)
        numcolumns = len(self.parameters_lt_scholarship.list_columns_name)
        self.ui.tableWidgetLTScholarship.setColumnCount(numcolumns)
        self.ui.tableWidgetLTScholarship.setHorizontalHeaderLabels(self.parameters_lt_scholarship.list_columns_name)
        self.ui.tableWidgetLTScholarship.setRowCount(numrows)
        if len(data) > 0:
            self.ui.tableWidgetLTScholarship.setColumnWidth(0, 150)
            self.ui.tableWidgetLTScholarship.setColumnWidth(1, 150)

        for row in range(numrows):
            for column in range(numcolumns):
                # Check if value datetime, if True convert to string
                if isinstance(data[row][column], datetime.date):
                    self.ui.tableWidgetLTScholarship.setItem(row, column, QtWidgets.QTableWidgetItem(
                        (data[row][column].strftime('%d.%m.%Y'))))
                elif isinstance(data[row][column], int):
                    self.ui.tableWidgetLTScholarship.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((str(data[row][column]))))
                else:
                    self.ui.tableWidgetLTScholarship.setItem(row, column,
                                                    QtWidgets.QTableWidgetItem((data[row][column])))

    '''------------------------------------------------------------------------------------------------------'''
