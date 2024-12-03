import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # Add labels to the content widget
        for i in range(1, 21):
            content_layout.addWidget(QLabel(f"Label {i}"))

        # Set the content widget to the scroll area
        scroll_area.setWidget(content_widget)

        # Create a main layout and add the scroll area to it
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)
        self.setWindowTitle("Simpler Scrollable Area in PyQt")
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# self.matrixScroll = QtWidgets.QScrollArea(Form)
# self.matrixScroll.setGeometry(QtCore.QRect(10, 370, 1200, 550))
# self.matrixScroll.setWidgetResizable(True)
# self.matrixWidget = QtWidgets.QWidget()
# self.matrixScroll.setObjectName("matrixScroll")
# self.matrixScroll.setWidgetResizable(True)
# self.matrixScroll.setWidget(self.matrixWidget)
# self.matrixScroll.scroll(300, 300)
# self.matrixBox = []
# for i in range(16):
#     row = []
#     for j in range(17):
#         input = QtWidgets.QDoubleSpinBox(self.matrixWidget)
#         input.setDecimals(5)
#         input.setRange(-9999999.0, 9999999.0)
#         input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
#         input.move(70 * (j % 21), i * 34)
#         input.setFixedWidth(70)
#         row.append(input)
#     self.matrixBox.append(row)
#
# # self.charWidget = QtWidgets.QWidget(self.matrixScroll)
# # self.charBox = []
# # for i in range(16):
# #     row = []
# #     for j in range(17):
# #       input = QtWidgets.QLineEdit(self.charWidget)
# #       input.setMaxLength(1)
# #
# #       input.move(70 * (j % 21), i * 34)
# #       input.setFixedWidth(50)
# #       row.append(input)
# #     self.charBox.append(row)
#
#
# self.matrixScroll.setWidget(self.matrixWidget)
# self.matrixWidget.setObjectName("matrixWidget")
# self.initials = QtWidgets.QWidget(parent=Form)
# self.initials.setGeometry(QtCore.QRect(30, 240, 1500, 100))
# self.initials.setObjectName("initials")
# self.initialsList = []
# for i in range(16):
#     l = QtWidgets.QLabel(self.initials)
#     l.setObjectName('X' + str(i))
#
#     l.move(5 + 94 * (i % 15), 5 + (int(i / 15) * 35))
#     l.setText("X" + str(i) + ':')
#     input = QtWidgets.QDoubleSpinBox(self.initials)
#     input.setDecimals(5)
#     input.setRange(-9999999.0, 9999999.0)
#     input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
#     input.move(94 * (i % 15) + 25, int(i / 15) * 35)
#     input.setFixedWidth(70)
#     self.initialsList.append([l, input])