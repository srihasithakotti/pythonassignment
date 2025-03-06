# Class with protected fields and methods
class ParentClass:
    def __init__(self):
        self._protected_field = "This is a protected field"

    def _protected_method(self):
        print("This is a protected method")

# Another class in the same package
class ChildClass(ParentClass):
    def access_protected(self):
        # Accessing the protected field and method from the ParentClass
        print(self._protected_field)  # Access protected field
        self._protected_method()  # Call protected method

# Testing
child = ChildClass()
child.access_protected()
