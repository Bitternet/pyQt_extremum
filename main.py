import random, sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QDoubleSpinBox,
                               QGridLayout, QVBoxLayout, QWidget)
from PySide2.QtGui import QPainter

from scipy.integrate import odeint
import numpy, pylab

class main(QWidget):
    def __init__(self):

        QWidget.__init__(self)

        self.button = QPushButton("Найти минимальное значение f(x)")
        self.button.setStyleSheet("background-color: steelblue; font: bold; color: white; font-size: 14px");
        self.button.setMinimumHeight(40)
        self.text = QLabel("Погрешность:")
        self.text.setStyleSheet("font-size: 14px");
        self.spin1 = QDoubleSpinBox();
        self.spin1.setValue(0.05);

        self.text2 = QLabel("Начальная точка отрезка:")
        self.text2.setStyleSheet("font-size: 14px");
        self.spin2 = QDoubleSpinBox();
        self.spin2.setValue(1.5);

        self.text3 = QLabel("Конечная точка отрезка:")
        self.text3.setStyleSheet("font-size: 14px");
        self.spin3 = QDoubleSpinBox();
        self.spin3.setValue(2);

        self.layout = QVBoxLayout()
        self.gridlayout = QGridLayout()
        self.gridlayout.addWidget(self.text, 0, 0)
        self.gridlayout.addWidget(self.spin1, 0, 1)

        self.gridlayout.addWidget(self.text2, 1, 0)
        self.gridlayout.addWidget(self.spin2, 1, 1)

        self.gridlayout.addWidget(self.text3, 2, 0)
        self.gridlayout.addWidget(self.spin3, 2, 1)

        self.gridlayout.addWidget(self.button, 3, 0, 1, 2)

        self.layout.addLayout(self.gridlayout)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.fn)


    @staticmethod
    def f(x):
       return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

    @staticmethod
    def biselect(f, a, b, eps):
         while((b - a) / 2 > eps):
            c = (a + b) / 2
            if ((f(a) * f(c)) > 0):
             a = (a + b) / 2
            else:
             b =  (a + b) / 2
            return c

    def fn(self):
         a = self.spin2.value()
         b = self.spin3.value()
         eps = self.spin1.value()
         x = self.biselect(self.f, a, b, eps)
         X = numpy.arange(a, b, eps)
         pylab.title("Минимальное значение функции f(x) и точка минимума x \n Ответ: F(x) = " + str(self.f(x)) + " x = " + str(x) + "\n")
         pylab.plot([x for x in X], [self.f(x) for x in X])
         pylab.grid(True)
         pylab.show()

if __name__ == "__main__":
         app = QApplication(sys.argv)

         widget = main()
         widget.resize(300, 100)
         widget.show()
         sys.exit(app.exec_())



