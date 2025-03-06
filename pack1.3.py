# Class 1 definition
class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Class1! My name is {self.name}")

# Class 2 definition
class Class2:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Class2! My name is {self.name}")

# Simulate importing these classes (just like using a package)
def import_classes():
    globals()['Class1'] = Class1
    globals()['Class2'] = Class2

# Simulate package initialization
import_classes()

# Main program logic
if __name__ == "__main__":
    obj1 = Class1("Alice")
    obj2 = Class2("Bob")

    obj1.greet()  # Output: Hello from Class1! My name is Alice
    obj2.greet()  # Output: Hello from Class2! My name is Bob
