# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QAbstractSpinBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 853)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 881, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.configGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.configGrid.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.configGrid.setContentsMargins(0, 0, 0, 0)
        self.configGrid.setObjectName("configGrid")
        self.Size = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.Size.setEnabled(True)
        self.Size.setFrame(True)
        self.Size.setKeyboardTracking(True)
        self.Size.setProperty("showGroupSeparator", False)
        self.Size.setPrefix("")
        self.Size.setMinimum(1)
        self.Size.setMaximum(16)
        self.Size.setObjectName("Size")
        self.configGrid.addWidget(self.Size, 0, 1, 1, 1)
        self.Scaling = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Scaling.setFont(font)
        self.Scaling.setObjectName("Scaling")
        self.configGrid.addWidget(self.Scaling, 0, 2, 1, 1)
        self.numberOfIterations = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.numberOfIterations.setEnabled(True)
        self.numberOfIterations.setFrame(True)
        self.numberOfIterations.setKeyboardTracking(True)
        self.numberOfIterations.setProperty("showGroupSeparator", False)
        self.numberOfIterations.setPrefix("")
        self.numberOfIterations.setMinimum(1)
        self.numberOfIterations.setMaximum(1000)
        self.numberOfIterations.setObjectName("numberOfIterations")
        self.configGrid.addWidget(self.numberOfIterations, 2, 1, 1, 1)
        self.error = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.error.setDecimals(5)
        self.error.setObjectName("error")
        self.configGrid.addWidget(self.error, 2, 3, 1, 1)
        self.methodBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.methodBox.setObjectName("methodBox")
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.configGrid.addWidget(self.methodBox, 1, 1, 1, 1)
        self.formatBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.formatBox.setObjectName("formatBox")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.formatBox.addItem("")
        self.configGrid.addWidget(self.formatBox, 1, 3, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.sizeLabel.setAutoFillBackground(False)
        self.sizeLabel.setObjectName("sizeLabel")
        self.configGrid.addWidget(self.sizeLabel, 0, 0, 1, 1)
        self.methodLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.methodLabel.setFont(font)
        self.methodLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.methodLabel.setObjectName("methodLabel")
        self.configGrid.addWidget(self.methodLabel, 1, 0, 1, 1)
        self.formatLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.formatLabel.setFont(font)
        self.formatLabel.setObjectName("formatLabel")
        self.configGrid.addWidget(self.formatLabel, 1, 2, 1, 1)
        self.numberOfIterationsLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.numberOfIterationsLabel.setFont(font)
        self.numberOfIterationsLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.numberOfIterationsLabel.setObjectName("numberOfIterationsLabel")
        self.configGrid.addWidget(self.numberOfIterationsLabel, 2, 0, 1, 1)
        self.errorLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.errorLabel.setFont(font)
        self.errorLabel.setObjectName("errorLabel")
        self.configGrid.addWidget(self.errorLabel, 2, 2, 1, 1)
        self.significantFig = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.significantFig.setObjectName("SpinBox")
        self.configGrid.addWidget(self.significantFig, 0, 3, 1, 1)
        self.Sbmit = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.Sbmit.setObjectName("Sbmit")
        self.configGrid.addWidget(self.Sbmit, 0, 4, 1, 1)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(70, 270, 761, 531))
        self.widget.setObjectName("widget")
        self.numberOfIterationsLabel_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.numberOfIterationsLabel_2.setFont(font)
        self.numberOfIterationsLabel_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.numberOfIterationsLabel_2.setObjectName("numberOfIterationsLabel_2")
        self.configGrid.addWidget(self.numberOfIterationsLabel_2, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.configGrid.addWidget(self.comboBox, 3, 1, 1, 1)
        self.comboBox.setItemText(0, "Partial Pivoting")
        self.comboBox.setItemText(1,  "Scaling")
        self.numberOfIterationsLabel_2.setText("Scaling/Pivoting")


        self.matrixScroll = QtWidgets.QScrollArea(Form)
        self.matrixScroll.setGeometry(QtCore.QRect(10, 370, 1200, 550))
        self.matrixScroll.setWidgetResizable(True)
        self.matrixWidget = QtWidgets.QWidget()
        self.matrixScroll.setObjectName("matrixScroll")
        self.matrixScroll.setWidgetResizable(True)
        self.matrixScroll.setWidget(self.matrixWidget)
        self.matrixScroll.scroll(300, 300)
        self.matrixBox = []
        for i in range(16):
            row = []
            for j in range(17):
              input = QtWidgets.QDoubleSpinBox(self.matrixWidget)
              input.setDecimals(5)
              input.setRange(-9999999.0, 9999999.0)
              input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
              input.move(70 * (j % 21), i * 34)
              input.setFixedWidth(70)
              row.append(input)
            self.matrixBox.append(row)


        # self.charWidget = QtWidgets.QWidget(self.matrixScroll)
        # self.charBox = []
        # for i in range(16):
        #     row = []
        #     for j in range(17):
        #       input = QtWidgets.QLineEdit(self.charWidget)
        #       input.setMaxLength(1)
        #
        #       input.move(70 * (j % 21), i * 34)
        #       input.setFixedWidth(50)
        #       row.append(input)
        #     self.charBox.append(row)


        self.matrixScroll.setWidget(self.matrixWidget)
        self.matrixWidget.setObjectName("matrixWidget")
        self.initials = QtWidgets.QWidget(parent=Form)
        self.initials.setGeometry(QtCore.QRect(30, 240, 1500, 100))
        self.initials.setObjectName("initials")
        self.initialsList = []
        for i in range(16):
           l = QtWidgets.QLabel(self.initials)
           l.setObjectName('X'+str(i))

           l.move(5+94*(i%15), 5+(int(i/15)*35))
           l.setText("X"+str(i)+':')
           input = QtWidgets.QDoubleSpinBox(self.initials)
           input.setDecimals(5)
           input.setRange(-9999999.0, 9999999.0)
           input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
           input.move(94*(i % 15)+25, int(i/15)*35)
           input.setFixedWidth(70)
           self.initialsList.append([l, input])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Scaling.setText(_translate("Form", "significant figures"))
        self.methodBox.setItemText(0, _translate("Form", "LU Decompisition"))
        self.methodBox.setItemText(1, _translate("Form", "Gauss Elimination"))
        self.methodBox.setItemText(2, _translate("Form", "Gauss Jordan"))
        self.methodBox.setItemText(3, _translate("Form", "Gauss seidel"))
        self.methodBox.setItemText(4, _translate("Form", "Jacobi Method"))
        self.formatBox.setItemText(0, _translate("Form", "Doolittle form"))
        self.formatBox.setItemText(1, _translate("Form", "Crout form"))
        self.formatBox.setItemText(2, _translate("Form", "Cholesky form"))
        self.sizeLabel.setText(_translate("Form", "Size"))
        self.methodLabel.setText(_translate("Form", "Method: "))
        self.formatLabel.setText(_translate("Form", "L & U format"))
        self.numberOfIterationsLabel.setText(_translate("Form", "Number of iterations:"))
        self.errorLabel.setText(_translate("Form", "max Relative error:"))
        self.Sbmit.setText(_translate("Form", "Submit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec())
