# CRT Program 23: Basic try-except block

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)

except (ZeroDivisionError, ValueError):
    print("Invalid input: enter integers and make sure b is not zero.")
