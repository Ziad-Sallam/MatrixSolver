# Form implementation generated from reading ui file 'answers.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ans(object):
    def setupUi(self, ans):
        ans.setObjectName("ans")
        ans.resize(810, 659)
        self.solutionButton = QtWidgets.QPushButton(parent=ans)
        self.solutionButton.setGeometry(QtCore.QRect(630, 580, 141, 51))
        self.solutionButton.setObjectName("solutionButton")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=ans)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.MethodLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.MethodLabel.setFont(font)
        self.MethodLabel.setObjectName("MethodLabel")
        self.gridLayout.addWidget(self.MethodLabel, 1, 0, 1, 1)
        self.iterationsLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.iterationsLabel.setFont(font)
        self.iterationsLabel.setObjectName("iterationsLabel")
        self.gridLayout.addWidget(self.iterationsLabel, 2, 0, 1, 1)
        self.iterations = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.iterations.setText("")
        self.iterations.setObjectName("iterations")
        self.gridLayout.addWidget(self.iterations, 2, 1, 1, 1)
        self.Method = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.Method.setText("")
        self.Method.setObjectName("Method")
        self.gridLayout.addWidget(self.Method, 1, 1, 1, 1)
        self.errorLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.errorLabel.setFont(font)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 2, 2, 1, 1)
        self.TimeLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.gridLayout.addWidget(self.TimeLabel, 0, 2, 1, 1)
        self.error = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.error.setText("")
        self.error.setObjectName("error")
        self.gridLayout.addWidget(self.error, 2, 3, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 0, 0, 1, 1)
        self.time = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.time.setText("")
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 0, 3, 1, 1)
        self.LULabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.LULabel.setFont(font)
        self.LULabel.setObjectName("LULabel")
        self.gridLayout.addWidget(self.LULabel, 1, 2, 1, 1)
        self.size = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.size.setText("")
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 0, 1, 1, 1)
        self.LU = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.LU.setText("")
        self.LU.setObjectName("LU")
        self.gridLayout.addWidget(self.LU, 1, 3, 1, 1)
        self.solutionWidget = QtWidgets.QWidget(parent=ans)
        self.solutionWidget.setGeometry(QtCore.QRect(19, 149, 761, 421))
        self.solutionWidget.setObjectName("solutionWidget")
        self.errorsWidget = QtWidgets.QWidget(ans)
        self.errorsWidget.move(250,250)
        self.errorMessage = QtWidgets.QLabel(self.errorsWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.errorsWidget.setFont(font)

        self.answers = []
        for i in range(16):
            label = QtWidgets.QLabel(self.solutionWidget)
            label.setObjectName("answerLabel" + str(i))
            label.setText(f"X{i}:")
            label.move(400 * (i % 2), int(i / 2) * 50)
            ans = QtWidgets.QLabel(self.solutionWidget)
            ans.setText("")
            ans.setObjectName("answer" + str(i))
            ans.move(400 * (i % 2) + 30, int(i / 2) * 50)
            self.answers.append([label,ans])


        self.retranslateUi(ans)
        QtCore.QMetaObject.connectSlotsByName(ans)

    def retranslateUi(self, ans):
        _translate = QtCore.QCoreApplication.translate
        ans.setWindowTitle(_translate("ans", "Form"))
        self.solutionButton.setText(_translate("ans", "export detailed solution"))
        self.MethodLabel.setText(_translate("ans", "Method:"))
        self.iterationsLabel.setText(_translate("ans", "Number of iterations: "))
        self.errorLabel.setText(_translate("ans", "Relative Error:"))
        self.TimeLabel.setText(_translate("ans", "Execution Time:"))
        self.sizeLabel.setText(_translate("ans", "Size:"))
        self.LULabel.setText(_translate("ans", "LU format:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ans = QtWidgets.QWidget()
    ui = Ui_ans()
    ui.setupUi(ans)
    ans.show()
    sys.exit(app.exec())
