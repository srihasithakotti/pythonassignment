# Custom function to raise an exception with a custom message
def check_positive_number(number):
    if number < 0:
        # Raising an exception with a custom message
        raise ValueError("Custom Error: The number cannot be negative!")
    else:
        print(f"The number {number} is positive.")

# Main function to test the exception
def main():
    try:
        # Test with a negative number
        check_positive_number(-5)
    except ValueError as e:
        # Catching the custom exception and printing the message
        print(f"Exception caught: {e}")

    try:
        # Test with a positive number
        check_positive_number(10)
    except ValueError as e:
        # This block will not execute as no exception is raised
        print(f"Exception caught: {e}")

# Run the main function
main()