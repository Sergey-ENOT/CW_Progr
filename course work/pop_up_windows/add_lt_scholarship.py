# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\add_lt_scholarship.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addLTScholarshipForm(object):
    def setupUi(self, addLTScholarshipForm):
        addLTScholarshipForm.setObjectName("addLTScholarshipForm")
        addLTScholarshipForm.resize(361, 81)
        self.layoutWidget = QtWidgets.QWidget(addLTScholarshipForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 249, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_id_student = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id_student.sizePolicy().hasHeightForWidth())
        self.label_id_student.setSizePolicy(sizePolicy)
        self.label_id_student.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_student.setObjectName("label_id_student")
        self.verticalLayout.addWidget(self.label_id_student)
        self.label_id_scholarship = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id_scholarship.sizePolicy().hasHeightForWidth())
        self.label_id_scholarship.setSizePolicy(sizePolicy)
        self.label_id_scholarship.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_scholarship.setObjectName("label_id_scholarship")
        self.verticalLayout.addWidget(self.label_id_scholarship)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditIdStudent = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditIdStudent.setObjectName("lineEditIdStudent")
        self.verticalLayout_2.addWidget(self.lineEditIdStudent)
        self.lineEditIdScholarship = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditIdScholarship.sizePolicy().hasHeightForWidth())
        self.lineEditIdScholarship.setSizePolicy(sizePolicy)
        self.lineEditIdScholarship.setObjectName("lineEditIdScholarship")
        self.verticalLayout_2.addWidget(self.lineEditIdScholarship)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButtonAddLTScholarship = QtWidgets.QPushButton(addLTScholarshipForm)
        self.pushButtonAddLTScholarship.setGeometry(QtCore.QRect(270, 20, 81, 31))
        self.pushButtonAddLTScholarship.setObjectName("pushButtonAddLTScholarship")

        self.retranslateUi(addLTScholarshipForm)
        QtCore.QMetaObject.connectSlotsByName(addLTScholarshipForm)

    def retranslateUi(self, addLTScholarshipForm):
        _translate = QtCore.QCoreApplication.translate
        addLTScholarshipForm.setWindowTitle(_translate("addLTScholarshipForm", "???????????????????? ??????????????????"))
        self.label_id_student.setText(_translate("addLTScholarshipForm", "??? ???????????????? ????????????"))
        self.label_id_scholarship.setText(_translate("addLTScholarshipForm", "Id ??????????????????"))
        self.pushButtonAddLTScholarship.setText(_translate("addLTScholarshipForm", "????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addLTScholarshipForm = QtWidgets.QWidget()
    ui = Ui_addLTScholarshipForm()
    ui.setupUi(addLTScholarshipForm)
    addLTScholarshipForm.show()
    sys.exit(app.exec_())
