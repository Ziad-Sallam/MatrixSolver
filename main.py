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
    elif ui.methodBox.currentText() == "Gauss seidel" or ui.methodBox.currentText() == "Jacobi Method":
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.show()
        ui.errorLabel.show()
        ui.numberOfIterations.show()
        ui.numberOfIterationsLabel.show()

    else:
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.hide()
        ui.errorLabel.hide()
        ui.numberOfIterations.hide()
        ui.numberOfIterationsLabel.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()

    ui.setupUi(Form)
    handleMethodChange()



    ui.methodBox.currentIndexChanged.connect(handleMethodChange)
    Form.show()
    sys.exit(app.exec())
