def divide_numbers(num, den):
    try:
        # Attempting to divide numbers
        result = num / den
        print("Result:", result)
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block will always be executed
        print("Execution of finally block.")

# Main program to test the function
def main():
    # Test Case 1: Valid division
    print("Test Case 1: Valid division")
    divide_numbers(10, 2)
    print()

    # Test Case 2: Division by zero
    print("Test Case 2: Division by zero")
    divide_numbers(10, 0)
    print()

    # Test Case 3: Invalid input (e.g., passing a string)
    print("Test Case 3: Invalid input")
    divide_numbers(10, "a")

# Run the main program
main()