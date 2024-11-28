from gui import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets


def handleMethodChange():
    if ui.methodBox.currentText() == "LU Decompisition":
        ui.formatBox.show()
        ui.formatLabel.show()
        ui.error.hide()
        ui.errorLabel.hide()
        ui.numberOfIterations.hide()
        ui.numberOfIterationsLabel.hide()
        ui.initials.hide()
    elif ui.methodBox.currentText() == "Gauss seidel" or ui.methodBox.currentText() == "Jacobi Method":
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.show()
        ui.errorLabel.show()
        ui.numberOfIterations.show()
        ui.numberOfIterationsLabel.show()
        ui.initials.show()

    else:
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.hide()
        ui.errorLabel.hide()
        ui.numberOfIterations.hide()
        ui.numberOfIterationsLabel.hide()
        ui.initials.hide()

def handleSizeChange():
    print(ui.Size.value())
    for i in range(len(ui.matrixBox)):
        ui.initialsList[i][0].hide()
        ui.initialsList[i][1].hide()
        for j in range(len(ui.matrixBox)+1):
            ui.matrixBox[i][j].hide()

    for i in range(ui.Size.value()):
        ui.initialsList[i][0].show()
        ui.initialsList[i][1].show()
        for j in range(ui.Size.value()+1):
            ui.matrixBox[i][j].show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    handleMethodChange()
    handleSizeChange()
    ui.methodBox.currentIndexChanged.connect(handleMethodChange)
    ui.Size.valueChanged.connect(handleSizeChange)
    Form.show()
    sys.exit(app.exec())




# initialsList = []
# for i in range(27):
#     l = QtWidgets.QLabel(self.initials)
#     l.setObjectName('X' + str(i))
#
#     l.move(5 + 94 * (i % 9), 5 + (int(i / 9) * 35))
#     l.setText("X" + str(i) + ':')
#     input = QtWidgets.QDoubleSpinBox(self.initials)
#     input.setDecimals(5)
#     input.setRange(-9999999.0, 9999999.0)
#     input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
#     input.move(94 * (i % 9) + 25, int(i / 9) * 35)
#     input.setFixedWidth(70)
#     initialsList.append([l, input])