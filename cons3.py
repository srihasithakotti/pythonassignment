class MyClass:
    def __init__(self):
        print("Public constructor called!")
    
    # Public Constructor
    def public_constructor(self):
        print("This is a public constructor!")
    
    # Protected Constructor (by convention)
    def _protected_constructor(self):
        print("This is a protected constructor!")

    # Private Constructor (by convention, using name mangling)
    def __private_constructor(self):
        print("This is a private constructor!")


class SubClass(MyClass):
    def __init__(self):
        super().__init__()
        print("Calling protected constructor from SubClass:")
        self._protected_constructor()  # Can be accessed within the subclass
        
        print("Calling private constructor from SubClass (will raise an error if done):")
        # self.__private_constructor()  # Uncommenting this line would raise an error because it's private

    def access_private_constructor(self):
        try:
            self.__private_constructor()  # Private method can still be accessed via name mangling
        except AttributeError:
            print("Unable to access private constructor directly!")

        # Accessing private method using name mangling
        print("Accessing private constructor via name mangling:")
        self._MyClass__private_constructor()  # Correct way to access private constructor


# Creating objects to demonstrate different constructor calls
if __name__ == "__main__":
    print("Creating an object of MyClass (using public constructor):")
    obj1 = MyClass()
    obj1.public_constructor()  # This is a public method
    
    print("\nCreating an object of SubClass to demonstrate constructor calls:")
    sub_obj = SubClass()
    
    # Accessing private constructor through name mangling
    print("\nTrying to access the private constructor (using name mangling):")
    sub_obj.access_private_constructor()  # This would access the private constructor
