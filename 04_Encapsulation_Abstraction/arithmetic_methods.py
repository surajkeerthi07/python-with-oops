# CRT Program 18: Class with arithmetic methods
# Note: This demonstrates methods inside a class; it is not, by itself,
# an example of data encapsulation.

class Calculator:
    def addition(self, a, b):
        print("Addition:", a + b)

    def subtraction(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)


calculator = Calculator()
calculator.addition(10, 20)
calculator.subtraction(30, 20)
calculator.multiply(30, 50)
