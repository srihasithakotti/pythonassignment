class Calculator:
    def add(self, a, b=0, c=0):
        # Method with different number of parameters
        result = a + b + c
        print(f"Result of addition: {result}")

# Creating an instance of Calculator class
calc = Calculator()

# Calling method with two arguments (simulates one version of overloading)
print("Calling add with two arguments:")
calc.add(5, 10)

# Calling method with one argument (simulates another version of overloading)
print("\nCalling add with one argument:")
calc.add(5)

# Calling method with three arguments
print("\nCalling add with three arguments:")
calc.add(5, 10, 15)