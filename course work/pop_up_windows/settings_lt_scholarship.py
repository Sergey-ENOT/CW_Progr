# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\settings_lt_scholarship.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ltScholarshipForm(object):
    def setupUi(self, ltScholarshipForm):
        ltScholarshipForm.setObjectName("ltScholarshipForm")
        ltScholarshipForm.resize(281, 101)
        self.layoutWidget = QtWidgets.QWidget(ltScholarshipForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_id_appoitment = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_id_appoitment.sizePolicy().hasHeightForWidth())
        self.checkBox_id_appoitment.setSizePolicy(sizePolicy)
        self.checkBox_id_appoitment.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_id_appoitment.setObjectName("checkBox_id_appoitment")
        self.verticalLayout_2.addWidget(self.checkBox_id_appoitment)
        self.checkBox_id_student = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_id_student.sizePolicy().hasHeightForWidth())
        self.checkBox_id_student.setSizePolicy(sizePolicy)
        self.checkBox_id_student.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_id_student.setObjectName("checkBox_id_student")
        self.verticalLayout_2.addWidget(self.checkBox_id_student)
        self.checkBox_id_scholarship = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_id_scholarship.sizePolicy().hasHeightForWidth())
        self.checkBox_id_scholarship.setSizePolicy(sizePolicy)
        self.checkBox_id_scholarship.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_id_scholarship.setObjectName("checkBox_id_scholarship")
        self.verticalLayout_2.addWidget(self.checkBox_id_scholarship)
        self.pushButtonApplySettingsLTScholarship = QtWidgets.QPushButton(ltScholarshipForm)
        self.pushButtonApplySettingsLTScholarship.setGeometry(QtCore.QRect(170, 30, 101, 31))
        self.pushButtonApplySettingsLTScholarship.setObjectName("pushButtonApplySettingsLTScholarship")

        self.retranslateUi(ltScholarshipForm)
        QtCore.QMetaObject.connectSlotsByName(ltScholarshipForm)

    def retranslateUi(self, ltScholarshipForm):
        _translate = QtCore.QCoreApplication.translate
        ltScholarshipForm.setWindowTitle(_translate("ltScholarshipForm", "?????????????????? ????????????????"))
        self.checkBox_id_appoitment.setText(_translate("ltScholarshipForm", "Id ????????????????????"))
        self.checkBox_id_student.setText(_translate("ltScholarshipForm", "??? ???????????????? ????????????"))
        self.checkBox_id_scholarship.setText(_translate("ltScholarshipForm", "Id ??????????????????"))
        self.pushButtonApplySettingsLTScholarship.setText(_translate("ltScholarshipForm", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ltScholarshipForm = QtWidgets.QWidget()
    ui = Ui_ltScholarshipForm()
    ui.setupUi(ltScholarshipForm)
    ltScholarshipForm.show()
    sys.exit(app.exec_())
