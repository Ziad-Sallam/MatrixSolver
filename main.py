import time

import subprocess

from gui import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets
from gaussSeidel import GaussSeidelSolver
from Jacobi import JacobiSolver
from GaussFinal import GaussianElimination
from answers import Ui_ans
from gaussJodonFinal import GaussJordanElimination
#from LUdecompsition import LUDecomposition

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
    print(ui.doubleSpinBox.value())
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


def segnificantFiguresChange():
    x = ui.doubleSpinBox.value()
    ui.error.setDecimals(x)
    for i in range(16):
        ui.initialsList[i][1].setDecimals(x)

    for i in range(16):
        for j in range(17):
            ui.matrixBox[i][j].setDecimals(x)


def evaluate():
    ans.hide()
    method = ui.methodBox.currentText()
    size = ui.Size.value()
    A = []
    b = []
    finals =[]
    ex_time =0
    iterations =None
    steps = ""
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ui.matrixBox[i][j].value())
        A.append(row)
        b.append(ui.matrixBox[i][size].value())

    if method == "Gauss seidel" or method == "Jacobi Method":
        iterations = ui.numberOfIterations.value()
        maxError = ui.error.value()
        initials = []
        for i in range(size):
            initials.append(ui.initialsList[i][1].value())
        print(initials)
        if method == "Gauss seidel":
            print(initials)
            solver = GaussSeidelSolver(A, b, max_iter=iterations, tol=maxError,precision=ui.doubleSpinBox.value())
            solution, iteration, time = solver.gauss_seidel_iteration(single_step=True)
            finals = solution
            print(iterations)
            print(time)
            ex_time = time
            iterations = iteration
            steps = solver.ans_str
        elif method == "Jacobi Method":
            solver = JacobiSolver(A, b, max_iter=iterations,tol=maxError,precision=ui.doubleSpinBox.value())
            solution, iteration, time = solver.jacobi_iteration(single_step=True)
            print(solution)
            finals = solution
            print(iteration)
            print(time)
            ex_time = time
            iterations = iteration
            steps = solver.ans_str
    elif method == "Gauss Elimination":
        solver = GaussianElimination(A, b, scaling=True, steps=True, significant_digits=ui.doubleSpinBox.value())
        if not solver.solve():
            ex_time = "infinity"
            finals = []
            steps = solver.ans_str
            if solver.noSolution:
                setAnsWindowError("The system has no solution")
                return
            elif solver.infiniteFlag:
                setAnsWindowError("The system has infinite solutions")
                return
        else:
            print(solver.finals)
            finals = solver.finals
            ex_time = solver.execution_time
            steps = solver.ans_str
    elif method == "Gauss Jordan":
        solver = GaussJordanElimination(A,b,scaling=True, steps=True, significant_digits=ui.doubleSpinBox.value())
        if not solver.solve():
            ex_time = "infinity"
            finals = []
            steps = solver.ans_str
            if solver.noSolution:
                setAnsWindowError("The system has no solution")
                return
            elif solver.infiniteFlag:
                setAnsWindowError("The system has infinite solutions")
                return
    elif method == "LU Decompisition":
        if ui.formatBox.currentText() == "Doolittle form":
            pass
        elif ui.formatBox.currentText() == "Crout form":
            pass
        elif ui.formatBox.currentText() == "Cholesky form":
            pass

    createTextFile(steps)
    setAnsWindow(finals, ex_time, iterations)
    ans.show()


def handleDetailedSol():
    command = "notepad ans.txt"
    subprocess.run(command, shell=True, check=True, text=True, capture_output=True)


def setAnsWindow(finals,time,iterations):
    ui1.iterations.setText(str(iterations))
    ui1.error.setText(str(ui.error.value()))
    ui1.Method.setText(str(ui.methodBox.currentText()))
    ui1.size.setText(str(ui.Size.value()))
    ui1.time.setText(str(time))
    ui1.errorsWidget.hide()
    for i in range(len(finals)):
        ui1.answers[i][1].setText(str(finals[i]))

def setAnsWindowError(msg):
    setAnsWindow([], "infinity","can't be determined")
    ui1.solutionWidget.hide()
    ui1.errorMessage.setText(msg)
    ui1.errorsWidget.show()
    ui1.errorMessage.show()
    ans.show()





def createTextFile(str):
    file = open("ans.txt", "w")
    file.write(str)
    file.close()


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
    ui.Sbmit.clicked.connect(evaluate)
    ui.doubleSpinBox.valueChanged.connect(segnificantFiguresChange)

    ans = QtWidgets.QWidget()
    ui1 = Ui_ans()
    ui1.setupUi(ans)
    ui1.solutionButton.clicked.connect(handleDetailedSol)

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