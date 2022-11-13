from config import host, root_user, guest_user, password, db_name
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_connector import ConnectorDB
from LoginInterface import Ui_LoginWindow
from extensions.extension_student import ParametersStudent
from extensions.extension_group import ParametersGroup
from extensions.extension_subject import ParametersSubject
from extensions.extension_scholarship import ParametersScholarship
from extensions.extension_debt import ParametersDebt
from extensions.extension_lt_scholarship import ParametersLTScholarship
from main_interface import MyWindow
import sys


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.login = ""
        self.password = ""
        self.application = None
        self.messagebox = QMessageBox()
        self.test = ParametersStudent()
        self.update_ui()

    def update_ui(self):
        self.ui.pushButtonLogin.clicked.connect(self.run_database)

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

    def check_login(self):
        input_login = self.ui.lineEditLogin.text().strip()
        input_password = self.ui.lineEditPassword.text().strip()
        if (len(input_login) == 0) or (len(input_password) == 0):
            self.show_messagebox("warning", "Warning", "Пустое поле 'логин' или 'пароль'\n"
                                                       "либо содержатся только пробелы")
            return False
        else:
            self.login = input_login
            self.password = input_password
            return True

    def run_database(self):
        if self.check_login():
            try:
                ConnectorDB(host, self.login, self.password, db_name, "student").create_connection(self.test)
                self.hide()
                student_connector = ConnectorDB(host, self.login, self.password, db_name, "student")
                group_connector = ConnectorDB(host, self.login, self.password, db_name, "study_group")
                subject_connector = ConnectorDB(host, self.login, self.password, db_name, "subject")
                scholarship_connector = ConnectorDB(host, self.login, self.password, db_name, "scholarship")
                debt_connector = ConnectorDB(host, self.login, self.password, db_name, "debt")
                lt_scholarship_connector = ConnectorDB(host, self.login, self.password, db_name, "student_scholarship")

                self.application = MyWindow(ParametersStudent(),
                                            student_connector,
                                            ParametersGroup(),
                                            group_connector,
                                            ParametersSubject(),
                                            subject_connector,
                                            ParametersScholarship(),
                                            scholarship_connector,
                                            ParametersDebt(),
                                            debt_connector,
                                            ParametersLTScholarship(),
                                            lt_scholarship_connector)
                self.application.show()
            except Exception:
                self.show_messagebox("critical", "Critical", "Access denied for this user")


app = QtWidgets.QApplication([])
login_w = LoginWindow()
login_w.show()
sys.exit(app.exec())
