def generate_arithmetic_exception():
    # Attempt to divide by zero, which will raise a ZeroDivisionError
    result = 10 / 0
    print("This will not be printed due to exception.")

# Main program to test the exception
def main():
    try:
        generate_arithmetic_exception()  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        # Catching the ZeroDivisionError and printing the error message
        print(f"Arithmetic Exception: {e}")

# Run the main program
main()