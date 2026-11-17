# CRT Program 21: Handling multiple exceptions

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter integers only.")
