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
        studentForm.resize(417, 262)
        self.pushButtonApplySettingsStudent = QtWidgets.QPushButton(studentForm)
        self.pushButtonApplySettingsStudent.setGeometry(QtCore.QRect(300, 80, 101, 31))
        self.pushButtonApplySettingsStudent.setObjectName("pushButtonApplySettingsStudent")
        self.layoutWidget = QtWidgets.QWidget(studentForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_gradebook = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_gradebook.sizePolicy().hasHeightForWidth())
        self.checkBox_gradebook.setSizePolicy(sizePolicy)
        self.checkBox_gradebook.setObjectName("checkBox_gradebook")
        self.verticalLayout_2.addWidget(self.checkBox_gradebook)
        self.checkBox_family = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_family.sizePolicy().hasHeightForWidth())
        self.checkBox_family.setSizePolicy(sizePolicy)
        self.checkBox_family.setObjectName("checkBox_family")
        self.verticalLayout_2.addWidget(self.checkBox_family)
        self.checkBox_name = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_name.sizePolicy().hasHeightForWidth())
        self.checkBox_name.setSizePolicy(sizePolicy)
        self.checkBox_name.setObjectName("checkBox_name")
        self.verticalLayout_2.addWidget(self.checkBox_name)
        self.checkBox_patronymic = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_patronymic.sizePolicy().hasHeightForWidth())
        self.checkBox_patronymic.setSizePolicy(sizePolicy)
        self.checkBox_patronymic.setObjectName("checkBox_patronymic")
        self.verticalLayout_2.addWidget(self.checkBox_patronymic)
        self.checkBox_group = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_group.sizePolicy().hasHeightForWidth())
        self.checkBox_group.setSizePolicy(sizePolicy)
        self.checkBox_group.setObjectName("checkBox_group")
        self.verticalLayout_2.addWidget(self.checkBox_group)
        self.checkBox_date_birthday = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_date_birthday.sizePolicy().hasHeightForWidth())
        self.checkBox_date_birthday.setSizePolicy(sizePolicy)
        self.checkBox_date_birthday.setObjectName("checkBox_date_birthday")
        self.verticalLayout_2.addWidget(self.checkBox_date_birthday)
        self.checkBox_town = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_town.sizePolicy().hasHeightForWidth())
        self.checkBox_town.setSizePolicy(sizePolicy)
        self.checkBox_town.setObjectName("checkBox_town")
        self.verticalLayout_2.addWidget(self.checkBox_town)
        self.checkBox_street = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_street.sizePolicy().hasHeightForWidth())
        self.checkBox_street.setSizePolicy(sizePolicy)
        self.checkBox_street.setObjectName("checkBox_street")
        self.verticalLayout_2.addWidget(self.checkBox_street)
        self.checkBox_hoise_flat = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_hoise_flat.sizePolicy().hasHeightForWidth())
        self.checkBox_hoise_flat.setSizePolicy(sizePolicy)
        self.checkBox_hoise_flat.setObjectName("checkBox_hoise_flat")
        self.verticalLayout_2.addWidget(self.checkBox_hoise_flat)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_gradebook = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gradebook.sizePolicy().hasHeightForWidth())
        self.label_gradebook.setSizePolicy(sizePolicy)
        self.label_gradebook.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gradebook.setObjectName("label_gradebook")
        self.verticalLayout.addWidget(self.label_gradebook)
        self.label_family = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_family.sizePolicy().hasHeightForWidth())
        self.label_family.setSizePolicy(sizePolicy)
        self.label_family.setAlignment(QtCore.Qt.AlignCenter)
        self.label_family.setObjectName("label_family")
        self.verticalLayout.addWidget(self.label_family)
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_patronymic = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_patronymic.sizePolicy().hasHeightForWidth())
        self.label_patronymic.setSizePolicy(sizePolicy)
        self.label_patronymic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_patronymic.setObjectName("label_patronymic")
        self.verticalLayout.addWidget(self.label_patronymic)
        self.label_group = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_group.sizePolicy().hasHeightForWidth())
        self.label_group.setSizePolicy(sizePolicy)
        self.label_group.setAlignment(QtCore.Qt.AlignCenter)
        self.label_group.setObjectName("label_group")
        self.verticalLayout.addWidget(self.label_group)
        self.label_date_birthday = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_birthday.sizePolicy().hasHeightForWidth())
        self.label_date_birthday.setSizePolicy(sizePolicy)
        self.label_date_birthday.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date_birthday.setObjectName("label_date_birthday")
        self.verticalLayout.addWidget(self.label_date_birthday)
        self.label_town = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_town.sizePolicy().hasHeightForWidth())
        self.label_town.setSizePolicy(sizePolicy)
        self.label_town.setAlignment(QtCore.Qt.AlignCenter)
        self.label_town.setObjectName("label_town")
        self.verticalLayout.addWidget(self.label_town)
        self.label_street = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_street.sizePolicy().hasHeightForWidth())
        self.label_street.setSizePolicy(sizePolicy)
        self.label_street.setAlignment(QtCore.Qt.AlignCenter)
        self.label_street.setObjectName("label_street")
        self.verticalLayout.addWidget(self.label_street)
        self.label_house_flat = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_house_flat.sizePolicy().hasHeightForWidth())
        self.label_house_flat.setSizePolicy(sizePolicy)
        self.label_house_flat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_house_flat.setObjectName("label_house_flat")
        self.verticalLayout.addWidget(self.label_house_flat)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(studentForm)
        QtCore.QMetaObject.connectSlotsByName(studentForm)

    def retranslateUi(self, studentForm):
        _translate = QtCore.QCoreApplication.translate
        studentForm.setWindowTitle(_translate("studentForm", "Настройки столбцов \"Студент\""))
        self.pushButtonApplySettingsStudent.setText(_translate("studentForm", "Применить"))
        self.checkBox_gradebook.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_family.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_name.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_patronymic.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_group.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_date_birthday.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_town.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_street.setText(_translate("studentForm", "CheckBox"))
        self.checkBox_hoise_flat.setText(_translate("studentForm", "CheckBox"))
        self.label_gradebook.setText(_translate("studentForm", "№ зачётной книжки"))
        self.label_family.setText(_translate("studentForm", "Фамилия"))
        self.label_name.setText(_translate("studentForm", "Имя"))
        self.label_patronymic.setText(_translate("studentForm", "Отчество"))
        self.label_group.setText(_translate("studentForm", "Группа"))
        self.label_date_birthday.setText(_translate("studentForm", "Дата рождения"))
        self.label_town.setText(_translate("studentForm", "Город"))
        self.label_street.setText(_translate("studentForm", "Улица"))
        self.label_house_flat.setText(_translate("studentForm", "Квартира/дом"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentForm = QtWidgets.QWidget()
    ui = Ui_studentForm()
    ui.setupUi(studentForm)
    studentForm.show()
    sys.exit(app.exec_())