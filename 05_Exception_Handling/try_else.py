# CRT Program 25: try-except-else block

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter integers only.")

else:
    # The else block runs only when the try block has no exception.
    print("Result:", result)
