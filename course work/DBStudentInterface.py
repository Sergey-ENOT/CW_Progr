# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\DBStudentInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 865)
        MainWindow.setStyleSheet("background-color: rgb(255, 247, 7);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1001, 801))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_student = QtWidgets.QWidget()
        self.tab_student.setObjectName("tab_student")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_student)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 971, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.layoutWidget = QtWidgets.QWidget(self.tab_student)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 971, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSettingsColumnsStudent = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSettingsColumnsStudent.sizePolicy().hasHeightForWidth())
        self.pushButtonSettingsColumnsStudent.setSizePolicy(sizePolicy)
        self.pushButtonSettingsColumnsStudent.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButtonSettingsColumnsStudent.setObjectName("pushButtonSettingsColumnsStudent")
        self.horizontalLayout.addWidget(self.pushButtonSettingsColumnsStudent)
        self.pushButtonDisplayRecordsStudent = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDisplayRecordsStudent.sizePolicy().hasHeightForWidth())
        self.pushButtonDisplayRecordsStudent.setSizePolicy(sizePolicy)
        self.pushButtonDisplayRecordsStudent.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButtonDisplayRecordsStudent.setObjectName("pushButtonDisplayRecordsStudent")
        self.horizontalLayout.addWidget(self.pushButtonDisplayRecordsStudent)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_student)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 570, 971, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelAviableFuncStudent = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAviableFuncStudent.sizePolicy().hasHeightForWidth())
        self.labelAviableFuncStudent.setSizePolicy(sizePolicy)
        self.labelAviableFuncStudent.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.labelAviableFuncStudent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAviableFuncStudent.setObjectName("labelAviableFuncStudent")
        self.verticalLayout.addWidget(self.labelAviableFuncStudent)
        self.pushButtonAddRecordStudent = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddRecordStudent.sizePolicy().hasHeightForWidth())
        self.pushButtonAddRecordStudent.setSizePolicy(sizePolicy)
        self.pushButtonAddRecordStudent.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButtonAddRecordStudent.setObjectName("pushButtonAddRecordStudent")
        self.verticalLayout.addWidget(self.pushButtonAddRecordStudent)
        self.pushButtonEditRecordStudent = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEditRecordStudent.sizePolicy().hasHeightForWidth())
        self.pushButtonEditRecordStudent.setSizePolicy(sizePolicy)
        self.pushButtonEditRecordStudent.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButtonEditRecordStudent.setObjectName("pushButtonEditRecordStudent")
        self.verticalLayout.addWidget(self.pushButtonEditRecordStudent)
        self.pushButtonDeleteRecordStudent = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteRecordStudent.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteRecordStudent.setSizePolicy(sizePolicy)
        self.pushButtonDeleteRecordStudent.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButtonDeleteRecordStudent.setObjectName("pushButtonDeleteRecordStudent")
        self.verticalLayout.addWidget(self.pushButtonDeleteRecordStudent)
        self.pushButtonSearchValueStudent = QtWidgets.QPushButton(self.tab_student)
        self.pushButtonSearchValueStudent.setGeometry(QtCore.QRect(14, 100, 971, 23))
        self.pushButtonSearchValueStudent.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButtonSearchValueStudent.setObjectName("pushButtonSearchValueStudent")
        self.widget = QtWidgets.QWidget(self.tab_student)
        self.widget.setGeometry(QtCore.QRect(20, 130, 161, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSearchColumnStudent = QtWidgets.QLabel(self.widget)
        self.labelSearchColumnStudent.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.labelSearchColumnStudent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSearchColumnStudent.setObjectName("labelSearchColumnStudent")
        self.verticalLayout_2.addWidget(self.labelSearchColumnStudent)
        self.comboBoxValueSearchColumnStudent = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxValueSearchColumnStudent.sizePolicy().hasHeightForWidth())
        self.comboBoxValueSearchColumnStudent.setSizePolicy(sizePolicy)
        self.comboBoxValueSearchColumnStudent.setObjectName("comboBoxValueSearchColumnStudent")
        self.verticalLayout_2.addWidget(self.comboBoxValueSearchColumnStudent)
        self.widget1 = QtWidgets.QWidget(self.tab_student)
        self.widget1.setGeometry(QtCore.QRect(189, 131, 791, 61))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelSearchValueStudent = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSearchValueStudent.sizePolicy().hasHeightForWidth())
        self.labelSearchValueStudent.setSizePolicy(sizePolicy)
        self.labelSearchValueStudent.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.labelSearchValueStudent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSearchValueStudent.setObjectName("labelSearchValueStudent")
        self.verticalLayout_3.addWidget(self.labelSearchValueStudent)
        self.lineEditSearchValueStudent = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearchValueStudent.sizePolicy().hasHeightForWidth())
        self.lineEditSearchValueStudent.setSizePolicy(sizePolicy)
        self.lineEditSearchValueStudent.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(255, 0, 0);")
        self.lineEditSearchValueStudent.setObjectName("lineEditSearchValueStudent")
        self.verticalLayout_3.addWidget(self.lineEditSearchValueStudent)
        self.tabWidget.addTab(self.tab_student, "")
        self.tab_group = QtWidgets.QWidget()
        self.tab_group.setObjectName("tab_group")
        self.tabWidget.addTab(self.tab_group, "")
        self.tab_subject = QtWidgets.QWidget()
        self.tab_subject.setObjectName("tab_subject")
        self.tabWidget.addTab(self.tab_subject, "")
        self.tab_scholarship = QtWidgets.QWidget()
        self.tab_scholarship.setObjectName("tab_scholarship")
        self.tabWidget.addTab(self.tab_scholarship, "")
        self.tab_grades = QtWidgets.QWidget()
        self.tab_grades.setObjectName("tab_grades")
        self.tabWidget.addTab(self.tab_grades, "")
        self.tab_linking_scholarship = QtWidgets.QWidget()
        self.tab_linking_scholarship.setObjectName("tab_linking_scholarship")
        self.tabWidget.addTab(self.tab_linking_scholarship, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "База данных \"Студент\""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        self.pushButtonSettingsColumnsStudent.setText(_translate("MainWindow", "Настройка столбцов"))
        self.pushButtonDisplayRecordsStudent.setText(_translate("MainWindow", "Вывести все записи таблицы"))
        self.labelAviableFuncStudent.setText(_translate("MainWindow", "Доступные функции"))
        self.pushButtonAddRecordStudent.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButtonEditRecordStudent.setText(_translate("MainWindow", "Редактировать запись"))
        self.pushButtonDeleteRecordStudent.setText(_translate("MainWindow", "Удалить запись"))
        self.pushButtonSearchValueStudent.setText(_translate("MainWindow", "Поиск по значению в столбце"))
        self.labelSearchColumnStudent.setText(_translate("MainWindow", "Столбец"))
        self.labelSearchValueStudent.setText(_translate("MainWindow", "Значение:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_student), _translate("MainWindow", "Таблица \"Студент\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_group), _translate("MainWindow", "Таблица \"Группа\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_subject), _translate("MainWindow", "Таблица \"Предмет\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scholarship), _translate("MainWindow", "Таблица \"Стипендия\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_grades), _translate("MainWindow", "Таблица \"Оценки\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linking_scholarship), _translate("MainWindow", "Таблица \"Назначенные стипендии\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())