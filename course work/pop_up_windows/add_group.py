# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\add_group.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addGroupForm(object):
    def setupUi(self, addGroupForm):
        addGroupForm.setObjectName("addGroupForm")
        addGroupForm.resize(352, 102)
        self.layoutWidget = QtWidgets.QWidget(addGroupForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_number_group = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_number_group.sizePolicy().hasHeightForWidth())
        self.label_number_group.setSizePolicy(sizePolicy)
        self.label_number_group.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number_group.setObjectName("label_number_group")
        self.verticalLayout.addWidget(self.label_number_group)
        self.label_level_training = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_level_training.sizePolicy().hasHeightForWidth())
        self.label_level_training.setSizePolicy(sizePolicy)
        self.label_level_training.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level_training.setObjectName("label_level_training")
        self.verticalLayout.addWidget(self.label_level_training)
        self.label_course = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_course.sizePolicy().hasHeightForWidth())
        self.label_course.setSizePolicy(sizePolicy)
        self.label_course.setAlignment(QtCore.Qt.AlignCenter)
        self.label_course.setObjectName("label_course")
        self.verticalLayout.addWidget(self.label_course)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditNumberGroup = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNumberGroup.setObjectName("lineEditNumberGroup")
        self.verticalLayout_2.addWidget(self.lineEditNumberGroup)
        self.lineEditDirectionTraining = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditDirectionTraining.setObjectName("lineEditDirectionTraining")
        self.verticalLayout_2.addWidget(self.lineEditDirectionTraining)
        self.lineEditCourse = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCourse.setObjectName("lineEditCourse")
        self.verticalLayout_2.addWidget(self.lineEditCourse)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButtonAddGroup = QtWidgets.QPushButton(addGroupForm)
        self.pushButtonAddGroup.setGeometry(QtCore.QRect(260, 20, 81, 41))
        self.pushButtonAddGroup.setObjectName("pushButtonAddGroup")

        self.retranslateUi(addGroupForm)
        QtCore.QMetaObject.connectSlotsByName(addGroupForm)

    def retranslateUi(self, addGroupForm):
        _translate = QtCore.QCoreApplication.translate
        addGroupForm.setWindowTitle(_translate("addGroupForm", "???????????????????? ????????????"))
        self.label_number_group.setText(_translate("addGroupForm", "?????????? ????????????"))
        self.label_level_training.setText(_translate("addGroupForm", "?????????????? ????????????????"))
        self.label_course.setText(_translate("addGroupForm", "????????"))
        self.pushButtonAddGroup.setText(_translate("addGroupForm", "????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addGroupForm = QtWidgets.QWidget()
    ui = Ui_addGroupForm()
    ui.setupUi(addGroupForm)
    addGroupForm.show()
    sys.exit(app.exec_())
