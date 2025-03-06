# Class A (superclass)
class A:
    def methodA(self):
        print("Method A from Class A")

# Class B (subclass of A)
class B(A):
    def methodB(self):
        print("Method B from Class B")

# Class C (subclass of B)
class C(B):
    def methodC(self):
        print("Method C from Class C")

# Main method
def main():
    # Create objects for each class
    objA = A()
    objB = B()
    objC = C()

    # Calling methods using objects
    objA.methodA()  # Calling method from class A
    
    objB.methodA()  
