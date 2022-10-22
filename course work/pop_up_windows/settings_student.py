# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\settings_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_studentForm(object):
    def setupUi(self, studentForm):
        studentForm.setObjectName("studentForm")
        studentForm.resize(281, 232)
        self.pushButtonApplySettingsStudent = QtWidgets.QPushButton(studentForm)
        self.pushButtonApplySettingsStudent.setGeometry(QtCore.QRect(170, 80, 101, 31))
        self.pushButtonApplySettingsStudent.setObjectName("pushButtonApplySettingsStudent")
        self.layoutWidget = QtWidgets.QWidget(studentForm)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 141, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_gradebook = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_gradebook.sizePolicy().hasHeightForWidth())
        self.checkBox_gradebook.setSizePolicy(sizePolicy)
        self.checkBox_gradebook.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_gradebook.setObjectName("checkBox_gradebook")
        self.verticalLayout_2.addWidget(self.checkBox_gradebook)
        self.checkBox_family = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_family.sizePolicy().hasHeightForWidth())
        self.checkBox_family.setSizePolicy(sizePolicy)
        self.checkBox_family.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_family.setObjectName("checkBox_family")
        self.verticalLayout_2.addWidget(self.checkBox_family)
        self.checkBox_name = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_name.sizePolicy().hasHeightForWidth())
        self.checkBox_name.setSizePolicy(sizePolicy)
        self.checkBox_name.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_name.setObjectName("checkBox_name")
        self.verticalLayout_2.addWidget(self.checkBox_name)
        self.checkBox_patronymic = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_patronymic.sizePolicy().hasHeightForWidth())
        self.checkBox_patronymic.setSizePolicy(sizePolicy)
        self.checkBox_patronymic.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_patronymic.setObjectName("checkBox_patronymic")
        self.verticalLayout_2.addWidget(self.checkBox_patronymic)
        self.checkBox_group = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_group.sizePolicy().hasHeightForWidth())
        self.checkBox_group.setSizePolicy(sizePolicy)
        self.checkBox_group.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_group.setObjectName("checkBox_group")
        self.verticalLayout_2.addWidget(self.checkBox_group)
        self.checkBox_date_birthday = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_date_birthday.sizePolicy().hasHeightForWidth())
        self.checkBox_date_birthday.setSizePolicy(sizePolicy)
        self.checkBox_date_birthday.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_date_birthday.setObjectName("checkBox_date_birthday")
        self.verticalLayout_2.addWidget(self.checkBox_date_birthday)
        self.checkBox_town = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_town.sizePolicy().hasHeightForWidth())
        self.checkBox_town.setSizePolicy(sizePolicy)
        self.checkBox_town.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_town.setObjectName("checkBox_town")
        self.verticalLayout_2.addWidget(self.checkBox_town)
        self.checkBox_street = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_street.sizePolicy().hasHeightForWidth())
        self.checkBox_street.setSizePolicy(sizePolicy)
        self.checkBox_street.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_street.setObjectName("checkBox_street")
        self.verticalLayout_2.addWidget(self.checkBox_street)
        self.checkBox_hoise_flat = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_hoise_flat.sizePolicy().hasHeightForWidth())
        self.checkBox_hoise_flat.setSizePolicy(sizePolicy)
        self.checkBox_hoise_flat.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_hoise_flat.setObjectName("checkBox_hoise_flat")
        self.verticalLayout_2.addWidget(self.checkBox_hoise_flat)

        self.retranslateUi(studentForm)
        QtCore.QMetaObject.connectSlotsByName(studentForm)

    def retranslateUi(self, studentForm):
        _translate = QtCore.QCoreApplication.translate
        studentForm.setWindowTitle(_translate("studentForm", "Настройки столбцов \"Студент\""))
        self.pushButtonApplySettingsStudent.setText(_translate("studentForm", "Применить"))
        self.checkBox_gradebook.setText(_translate("studentForm", "№ зачётной книжки"))
        self.checkBox_family.setText(_translate("studentForm", "Фамилия"))
        self.checkBox_name.setText(_translate("studentForm", "Имя"))
        self.checkBox_patronymic.setText(_translate("studentForm", "Отчество"))
        self.checkBox_group.setText(_translate("studentForm", "Группа"))
        self.checkBox_date_birthday.setText(_translate("studentForm", "Дата рождения"))
        self.checkBox_town.setText(_translate("studentForm", "Город"))
        self.checkBox_street.setText(_translate("studentForm", "Улица"))
        self.checkBox_hoise_flat.setText(_translate("studentForm", "Дом"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentForm = QtWidgets.QWidget()
    ui = Ui_studentForm()
    ui.setupUi(studentForm)
    studentForm.show()
    sys.exit(app.exec_())