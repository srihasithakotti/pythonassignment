# Superclass A with private fields and private methods
class A:
    def __init__(self):
        # Private fields (instance variables)
        self.__private_field1 = "Private Field 1"
        self.__private_field2 = "Private Field 2"

    # Private method
    def __private_method(self):
        print("This is a private method in class A.")

    # Public method to access private fields and methods (for demonstration)
    def access_private_fields(self):
        print(self.__private_field1)
        print(self.__private_field2)

    def access_private_method(self):
        self.__private_method()

# Subclass B that tries to access private fields and methods from class A
class B(A):
    def __init__(self):
        super().__init__()

    def try_access_private_fields(self):
        try:
            print(self.__private_field1)  # Attempting to access private field
        except AttributeError:
            print("Cannot access private field __private_field1 from subclass B.")

        try:
            print(self.__private_field2)  # Attempting to access private field
        except AttributeError:
            print("Cannot access private field __private_field2 from subclass B.")

    def try_access_private_method(self):
        try:
            self.__private_method()  # Attempting to access private method
        except AttributeError:
            print("Cannot access private method __private_method from subclass B.")

# Main method for testing
def main():
    # Create an object of class A
    a = A()

    # Access private fields using public methods
    print("Accessing private fields from class A:")
    a.access_private_fields()

    # Access private method using public method
    print("\nAccessing private method from class A:")
    a.access_private_method()

    # Create an object of class B (Subclass of A)
    b = B()

    # Try to access private fields and method in subclass B
    print("\nAccessing private fields and method from subclass B:")
    b.try_access_private_fields()
    b.try_access_private_method()

# Call the main method
if __name__ == "__main__":
    main()
