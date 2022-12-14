# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course work\pop_up_windows\settings_scholarship.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scholarshipForm(object):
    def setupUi(self, scholarshipForm):
        scholarshipForm.setObjectName("scholarshipForm")
        scholarshipForm.resize(271, 141)
        self.layoutWidget = QtWidgets.QWidget(scholarshipForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.checkBox_name_scholarship = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_name_scholarship.sizePolicy().hasHeightForWidth())
        self.checkBox_name_scholarship.setSizePolicy(sizePolicy)
        self.checkBox_name_scholarship.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_name_scholarship.setObjectName("checkBox_name_scholarship")
        self.verticalLayout_2.addWidget(self.checkBox_name_scholarship)
        self.checkBox_amount = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_amount.sizePolicy().hasHeightForWidth())
        self.checkBox_amount.setSizePolicy(sizePolicy)
        self.checkBox_amount.setStyleSheet("border: 2px solid;\n"
"border-color: rgb(89, 170, 139);")
        self.checkBox_amount.setObjectName("checkBox_amount")
        self.verticalLayout_2.addWidget(self.checkBox_amount)
        self.pushButtonApplySettingsScholarship = QtWidgets.QPushButton(scholarshipForm)
        self.pushButtonApplySettingsScholarship.setGeometry(QtCore.QRect(160, 50, 101, 31))
        self.pushButtonApplySettingsScholarship.setObjectName("pushButtonApplySettingsScholarship")

        self.retranslateUi(scholarshipForm)
        QtCore.QMetaObject.connectSlotsByName(scholarshipForm)

    def retranslateUi(self, scholarshipForm):
        _translate = QtCore.QCoreApplication.translate
        scholarshipForm.setWindowTitle(_translate("scholarshipForm", "?????????????????? ??????????????????????"))
        self.checkBox_id_scholarship.setText(_translate("scholarshipForm", "Id ??????????????????"))
        self.checkBox_name_scholarship.setText(_translate("scholarshipForm", "???????????????? ??????????????????"))
        self.checkBox_amount.setText(_translate("scholarshipForm", "????????????"))
        self.pushButtonApplySettingsScholarship.setText(_translate("scholarshipForm", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scholarshipForm = QtWidgets.QWidget()
    ui = Ui_scholarshipForm()
    ui.setupUi(scholarshipForm)
    scholarshipForm.show()
    sys.exit(app.exec_())
