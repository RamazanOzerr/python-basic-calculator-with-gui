from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import time
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.UI()
        self.r_add.setChecked(True)

    def UI(self):
        form = QFormLayout()
        h_box = QHBoxLayout()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete)
        qFont = QFont("Calibri",14,QFont.Bold)
        qIcon = QIcon("Logo_Haf.png")

        self.result = QLabel()
        self.result.setFont(qFont)

        self.s1_label = QLabel("Number1 : ")
        self.s2_label = QLabel("Number2 : ")

        self.s1_edit = QLineEdit()
        self.s2_edit = QLineEdit()

        self.r_add = QRadioButton("Sum")
        self.r_add.clicked.connect(self.calculate)
        self.r_sub = QRadioButton("Substract")
        self.r_sub.clicked.connect(self.calculate)
        self.r_multiple = QRadioButton("Multiple")
        self.r_multiple.clicked.connect(self.calculate)
        self.r_devide = QRadioButton("Divide")
        self.r_devide.clicked.connect(self.calculate)

        h_box.addWidget(self.r_add)
        h_box.addWidget(self.r_sub)
        h_box.addWidget(self.r_multiple)
        h_box.addWidget(self.r_devide)

        form.addRow(self.s1_label,self.s1_edit)
        form.addRow(self.s2_label,self.s2_edit)
        form.addRow(QLabel("Calculation : "),h_box)
        form.addRow(self.calculate_button)
        form.addRow(QLabel("Calculation result : "),self.result)
        form.addRow(self.delete_button)

        self.setLayout(form)
        self.setGeometry(1000,400,400,180)
        self.setWindowTitle("BASIC CALCULATOR")
        self.setWindowIcon(qIcon)
        self.show()

    def calculate(self):
        try:
            if self.r_add.isChecked():
                self.result.setText(str(float(self.s1_edit.text()) + float(self.s2_edit.text())))
            elif self.r_sub.isChecked():
                self.result.setText(str(float(self.s1_edit.text()) - float(self.s2_edit.text())))
            elif self.r_devide.isChecked():
                self.result.setText(str(float(self.s1_edit.text()) / float(self.s2_edit.text())))
            elif self.r_multiple.isChecked():
                self.result.setText(str(float(self.s1_edit.text()) * float(self.s2_edit.text())))
            else:
                self.result.setText("Not chosen the calculation type...")


        except:
            self.result.setText("ERROR ! Please try again !")

    def delete(self):
        self.result.setText("")
        self.s1_edit.setText("")
        self.s2_edit.setText("")
        self.s1_edit.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())