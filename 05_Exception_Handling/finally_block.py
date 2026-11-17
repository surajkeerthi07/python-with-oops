# CRT Program 26: try-except-else-finally block

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter integers only.")

else:
    print("Result:", result)

finally:
    # The finally block runs whether an exception occurred or not.
    print("Code execution is over.")
