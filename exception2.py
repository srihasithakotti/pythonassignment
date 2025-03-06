# Program with exception handling to handle arithmetic exceptions like division by zero

num = 10
den = 0

try:
    # Attempting division by zero, which will raise a ZeroDivisionError
    result = num / den
    print("Result:", result)
except ZeroDivisionError:
    # Handling the division by zero exception
    print("Error: Division by zero is not allowed.")