# CRT Program 2: Create a class with multiple methods

class Calculator:
    def addition(self, a, b):
        print("Addition:", a + b)

    def subtraction(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)


calculator = Calculator()
calculator.addition(10, 20)
calculator.subtraction(40, 20)
calculator.multiply(10, 5)
