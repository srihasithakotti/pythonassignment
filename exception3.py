# Method that raises an exception
def raise_exception():
    # Raise a custom exception or a built-in exception
    raise Exception("This is a custom exception thrown from raise_exception method.")

# Main program with try-except block
def main():
    print("Calling the method that raises an exception...")
    try:
        raise_exception()  # This will raise the exception
    except Exception as e:
        print(f"Exception caught: {e}")

# Calling the main method
main()