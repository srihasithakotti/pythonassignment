# Define a custom exception by subclassing the built-in Exception class
class MyCustomException(Exception):
    def _init_(self, message):
        # Initialize the base class with the message
        super()._init_(message)

# Function that raises the custom exception if a condition is met
def check_number(number):
    if number < 0:
        # Raise the custom exception with a specific message
        raise MyCustomException("Custom Error: Negative numbers are not allowed.")
    else:
        print(f"Number {number} is valid.")

# Main function to demonstrate custom exception handling
def main():
    try:
        # Test with a negative number to raise the custom exception
        check_number(-5)
    except MyCustomException as e:
        # Catch the custom exception and print the error message
        print(f"Exception caught: {e}")
    
    try:
        # Test with a positive number (this will not raise an exception)
        check_number(10)
    except MyCustomException as e:
        # This block will not execute
        print(f"Exception caught: {e}")

# Run the program
main()