from calculator.controller import Controller
import sys

controller = Controller()
try:
    operator = input("Choose the action on the complex numbers you want to perform: [* / + -]: ")
    real1 = input("Real part of the first complex number: ")
    imag1 = input("Imaginary part of the first complex number: ")
    real2 = input("Real part of the second complex number: ")
    imag2 = input("Imaginary part of the second complex number: ")
    result = controller.action(int(real1), int(imag1), int(real2), int(imag2), operator)
    print(f"{real1}{'+' if int(imag1) > 0 else ''}{imag1}j {operator} {real2}{'+' if int(imag2) > 0 else ''}{imag2}j = {result}")
except ValueError:
    print("Wrong input", sys.exc_info())

