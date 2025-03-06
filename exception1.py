# Program with exception handling to avoid Arithmetic Exception (ZeroDivisionError)

num = 10
den = 0

try:
    result = num / den  # Attempting division by zero
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
