# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\add_subject.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addSubjectForm(object):
    def setupUi(self, addSubjectForm):
        addSubjectForm.setObjectName("addSubjectForm")
        addSubjectForm.resize(351, 81)
        self.layoutWidget = QtWidgets.QWidget(addSubjectForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_number_subject = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_number_subject.sizePolicy().hasHeightForWidth())
        self.label_number_subject.setSizePolicy(sizePolicy)
        self.label_number_subject.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number_subject.setObjectName("label_number_subject")
        self.verticalLayout.addWidget(self.label_number_subject)
        self.label_subject = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_subject.sizePolicy().hasHeightForWidth())
        self.label_subject.setSizePolicy(sizePolicy)
        self.label_subject.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subject.setObjectName("label_subject")
        self.verticalLayout.addWidget(self.label_subject)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditIdSubject = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditIdSubject.setObjectName("lineEditIdSubject")
        self.verticalLayout_2.addWidget(self.lineEditIdSubject)
        self.lineEditNameSubject = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNameSubject.setObjectName("lineEditNameSubject")
        self.verticalLayout_2.addWidget(self.lineEditNameSubject)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButtonAddSubject = QtWidgets.QPushButton(addSubjectForm)
        self.pushButtonAddSubject.setGeometry(QtCore.QRect(260, 20, 81, 41))
        self.pushButtonAddSubject.setObjectName("pushButtonAddSubject")

        self.retranslateUi(addSubjectForm)
        QtCore.QMetaObject.connectSlotsByName(addSubjectForm)

    def retranslateUi(self, addSubjectForm):
        _translate = QtCore.QCoreApplication.translate
        addSubjectForm.setWindowTitle(_translate("addSubjectForm", "???????????????????? ????????????????"))
        self.label_number_subject.setText(_translate("addSubjectForm", "Id ????????????????"))
        self.label_subject.setText(_translate("addSubjectForm", "???????????????? ????????????????"))
        self.pushButtonAddSubject.setText(_translate("addSubjectForm", "????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addSubjectForm = QtWidgets.QWidget()
    ui = Ui_addSubjectForm()
    ui.setupUi(addSubjectForm)
    addSubjectForm.show()
    sys.exit(app.exec_())
