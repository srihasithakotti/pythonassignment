def divide_numbers(num, den):
    try:
        # Attempt division
        result = num / den
        print("Result:", result)
    
    # Handle division by zero error
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    # Handle ValueError in case of invalid input (e.g., passing non-numeric values)
    except ValueError:
        print("Error: Invalid value provided.")
    
    # Handle TypeError in case of type mismatch (e.g., passing a string to arithmetic operations)
    except TypeError:
        print("Error: Invalid type. Please provide numbers.")
    
    # Handle any other exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function with different inputs
print("Test Case 1:")
divide_numbers(10, 2)  # Valid division

print("\nTest Case 2:")
divide_numbers(10, 0)  # Division by zero

print("\nTest Case 3:")
divide_numbers(10, 'a')  # Invalid type (string instead of a number)

print("\nTest Case 4:")
divide_numbers('10', '5')  #