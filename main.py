import math
import time as tm
import subprocess
from gui1 import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets
from gaussSeidel import GaussSeidelSolver
from Jacobi import JacobiSolver
from GaussFinal import GaussianElimination
from answers import Ui_ans
from gaussJodonFinal import GaussJordanElimination
from LUDecomposition import LUDecomposition
from crout import LU_Decomposition as CroutDecomposition
from Chelosky import Cholesky_Decomposition
from gaussSymbols import GaussianElimination2
from sympy import Matrix
import sympy as sp
from CroutSYMBOL import LU_Decomposition_Symbolic as CroutDecomposition_Symbolic
from DolittleSYMBOLS import LUDecomposition as DolittleDecomposition_Symbolic
from CheloskySYMBOLS import Cholesky_Decomposition as CholeskyDecomposition_Symbolic
from JordonSYMBOLS import GaussJordanElimination as JordanElimination_Symbolic

def handleMethodChange():

    if ui.methodBox.currentText() == "LU Decompisition":
        ui.formatBox.show()
        ui.formatLabel.show()
        ui.error.hide()
        ui.errorLabel.hide()
        ui.numberOfIterations.hide()
        ui.numberOfIterationsLabel.hide()
        ui.initials.hide()
        ui.numberOfIterationsLabel_2.hide()
        ui.comboBox.hide()

    elif ui.methodBox.currentText() == "Gauss seidel" or ui.methodBox.currentText() == "Jacobi Method":
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.show()
        ui.errorLabel.show()
        ui.numberOfIterations.show()
        ui.numberOfIterationsLabel.show()
        ui.initials.show()
        ui.numberOfIterationsLabel_2.hide()
        ui.comboBox.hide()
    else:
        ui.numberOfIterationsLabel_2.show()
        ui.comboBox.show()
        ui.formatBox.hide()
        ui.formatLabel.hide()
        ui.error.hide()
        ui.errorLabel.hide()
        ui.numberOfIterations.hide()
        ui.numberOfIterationsLabel.hide()
        ui.initials.hide()

def handleSizeChange():
    print(ui.Size.value())
    print(ui.significantFig.value())
    try:
        for i in range(len(ui.matrixBox)):
            ui.initialsList[i][0].hide()
            ui.initialsList[i][1].hide()
            for j in range(len(ui.matrixBox)+1):
                ui.matrixBox[i][j].hide()
                ui.charBox[i][j].hide()

        for i in range(ui.Size.value()):
            ui.initialsList[i][0].show()
            ui.initialsList[i][1].show()
            for j in range(ui.Size.value()+1):
                ui.matrixBox[i][j].show()
                ui.charBox[i][j].show()

    except Exception as e:
        pass


def handleInputChange():
    if ui.inputBox.currentText() == "Numeric":
        ui.charWidget.hide()
        ui.matrixWidget.show()
        ui.initials.show()
    elif ui.inputBox.currentText() == "Characters":
        ui.charWidget.show()
        ui.initials.hide()
        ui.matrixWidget.hide()


def segnificantFiguresChange():
    x = ui.significantFig.value()

    for i in range(16):
        ui.initialsList[i][1].setDecimals(x)

    for i in range(16):
        for j in range(17):
            ui.matrixBox[i][j].setDecimals(x)


def evaluateChar():
    ans.hide()
    size = ui.Size.value()
    A = []
    b = []
    ex_time = 0
    iterations = None
    steps = ""
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ui.charBox[i][j].text())
        A.append(row)
        b.append(ui.charBox[i][size].text())
    print("hereeeeeee")
    if ui.methodBox.currentText() == "Gauss Elimination":
        solver = GaussianElimination2(A,b)
        solver.show_steps = True
        solver.solve()
        createTextFile(str(solver.ans))
    elif ui.methodBox.currentText() == "LU Decompisition":
        if ui.formatBox.currentText() == "Crout form":
            solver = CroutDecomposition_Symbolic(A,b,True)
            solver.solve()
            print(A)
            print(b)
            print(solver.ans_str)
            createTextFile(str(solver.ans_str))
        elif ui.formatBox.currentText() == "Doolittle form":
            solver = DolittleDecomposition_Symbolic(A, b, True,significant_digits=6)
            print(solver.solve())
            print(A)
            print(b)
            print(solver.ans_str)
            createTextFile(solver.ans_str)
        elif ui.formatBox.currentText() == "Cholesky form":
            solver = CholeskyDecomposition_Symbolic(A, b, precision=6, steps=True)
            try:
                print(solver.solve())
                print(A)
                print(b)
                print(solver.ans_str)
                createTextFile(solver.ans_str)
            except Exception as e:
                createTextFile("Not Symmetric")
    elif ui.methodBox.currentText() == "Gauss Jordan":
        solver = JordanElimination_Symbolic(A, b)
        solver.show_steps = True
        solver.solve()
        createTextFile(str(solver.ans))

    handleDetailedSol()


def evaluate():
    ui1.error.setText("None")
    ui1.LU.setText("None")
    if ui.inputBox.currentText() == "Characters":
        evaluateChar()
        return

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
            solver = GaussSeidelSolver(A, b, max_iter=iterations, tol=maxError,precision=ui.significantFig.value())
            solver.initial_guess = initials
            solution, iteration, time = solver.gauss_seidel_iteration(single_step=True)
            finals = solution
            print(iterations)
            print(time)
            ui1.error.setText(str(solver.relativeError))
            ex_time = time
            iterations = iteration
            steps = solver.ans_str

        elif method == "Jacobi Method":
            solver = JacobiSolver(A, b, max_iter=iterations,tol=maxError,precision=ui.significantFig.value())
            solver.initial_guess = initials
            solution, iteration, time = solver.jacobi_iteration(single_step=True)
            print(solution)
            finals = solution
            print(iteration)
            print(time)
            ex_time = time
            iterations = iteration
            ui1.error.setText(str(solver.relativeError))
            steps = solver.ans_str

    elif method == "Gauss Elimination":
        scale = False
        if ui.comboBox.currentText() == "Scaling":
            scale = True
        print(scale)
        solver = GaussianElimination(A, b, scaling=scale, steps=True, significant_digits=ui.significantFig.value())
        if not solver.solve():
            ex_time = ""
            finals = []
            steps = solver.ans_str
            if solver.noSolution:
                setAnsWindowError("The system has no solution")
                return
            elif solver.infiniteFlag:
                setAnsWindowError("The system has infinite solutions")
                return
        else:
            print("teessssstt")
            print(solver.finals)
            finals = solver.finals
            ex_time = solver.execution_time
            steps = solver.ans_str
    elif method == "Gauss Jordan":
        scale = False
        if ui.comboBox.currentText() == "Scaling":
            scale = True
        print(scale)

        solver = GaussJordanElimination(A, b, scaling=scale, steps=True, significant_digits=ui.significantFig.value())
        st = tm.time()
        if not solver.solve():
            ex_time = ""
            finals = []
            steps = solver.ans_str
            if solver.noSolution:
                setAnsWindowError("The system has no solution")
                return
            elif solver.infiniteFlag:
                setAnsWindowError("The system has infinite solutions")
                return
        else:
            ex_time = tm.time() - st
            print(solver.finals)
            finals = solver.finals
            steps = solver.ans_str
    elif method == "LU Decompisition":
        if ui.formatBox.currentText() == "Doolittle form":
            ui1.LU.setText("Doolittle form")
            solver = LUDecomposition(A, b, significant_digits=ui.significantFig.value(), steps=True)
            st = tm.time()
            finals = solver.solve().tolist()
            ex_time = tm.time() - st
            steps = solver.ans_str
            if solver.isSingular:
                setAnsWindowError("the matrix is singular")

        elif ui.formatBox.currentText() == "Crout form":
            ui1.LU.setText("Crout form")
            solver = CroutDecomposition(A, b, precision=ui.significantFig.value(), steps=True)
            st = tm.time()
            finals = solver.solve()
            for i in range(len(finals)):
                finals[i] = round(finals[i], ui.significantFig.value())
            ex_time = tm.time() - st
            steps = solver.ans_str
            print(finals)

        elif ui.formatBox.currentText() == "Cholesky form":
            ui1.LU.setText("Cholesky form")
            try:
                solver = Cholesky_Decomposition(A, b, precision=ui.significantFig.value(), steps=True)
                st = tm.time()
                finals = solver.solve().tolist()
                ex_time = tm.time() - st
                steps = solver.ans_str
            except Exception as e:
                setAnsWindowError("error")
                ans.show()
                return

    print("hello")
    print(finals)
    for i in range(len(finals)):
        finals[i] = round(float(finals[i]), ui.significantFig.value())
    print("hello again!!")

    createTextFile(steps)
    setAnsWindow(finals, ex_time, iterations)
    ans.show()


def handleDetailedSol():
    command = "notepad ans.txt"
    subprocess.run(command, shell=True, check=True, text=True, capture_output=True)


def setAnsWindow(finals, time, iterations):
    ui1.iterations.setText(str(iterations))
    #ui1.error.setText(str(ui.error.value()))
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
    from sympy import Matrix

    # Example augmented matrix
    augmented_matrix = Matrix([['1', 2, 3], [4, 5, 6], [7, 8, 9]])

    # Pretty-print to a string
    pretty_string = sp.pretty(Matrix(augmented_matrix))
    print(pretty_string)



    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.error.setDecimals(7)
    ui.significantFig.setValue(6)
    handleMethodChange()
    handleSizeChange()
    segnificantFiguresChange()
    ui.methodBox.currentIndexChanged.connect(handleMethodChange)
    ui.Size.valueChanged.connect(handleSizeChange)
    ui.Sbmit.clicked.connect(evaluate)
    ui.significantFig.valueChanged.connect(segnificantFiguresChange)
    ans = QtWidgets.QWidget()
    ui.charWidget.hide()
    ui1 = Ui_ans()
    ui1.setupUi(ans)
    ui1.solutionButton.clicked.connect(handleDetailedSol)
    ui.inputBox.currentIndexChanged.connect(handleInputChange)

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