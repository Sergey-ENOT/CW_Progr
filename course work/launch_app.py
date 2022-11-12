from config import host, root_user, guest_user, password, db_name
from PyQt5 import QtWidgets
from db_connector import ConnectorDB
from extensions.extension_student import ParametersStudent
from extensions.extension_group import ParametersGroup
from extensions.extension_subject import ParametersSubject
from extensions.extension_scholarship import ParametersScholarship
from extensions.extension_debt import ParametersDebt
from main_interface import MyWindow
import sys

app = QtWidgets.QApplication([])
student_connector = ConnectorDB(host, root_user, password, db_name, "student")
group_connector = ConnectorDB(host, root_user, password, db_name, "study_group")
subject_connector = ConnectorDB(host, root_user, password, db_name, "subject")
scholarship_connector = ConnectorDB(host, root_user, password, db_name, "scholarship")
debt_connector = ConnectorDB(host, root_user, password, db_name, "debt")

application = MyWindow(ParametersStudent(),
                       student_connector,
                       ParametersGroup(),
                       group_connector,
                       ParametersSubject(),
                       subject_connector,
                       ParametersScholarship(),
                       scholarship_connector,
                       ParametersDebt(),
                       debt_connector)
application.show()

sys.exit(app.exec())
