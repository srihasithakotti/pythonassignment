# Superclass A
class A:
    def method_A1(self):
        print("Method A1: Specific to class A")

    def method_A2(self):
        print("Method A2: Specific to class A")

    def method_override(self):
        print("Method Override: This is the method from class A")

# Subclass B (inheriting from A)
class B(A):
    def method_B1(self):
        print("Method B1: Specific to class B")

    def method_B2(self):
        print("Method B2: Specific to class B")

    # Override method from class A
    def method_override(self):
        print("Method Override: This is the overridden method in class B")

# Subclass C (inheriting from B)
class C(B):
    def method_C1(self):
        print("Method C1: Specific to class C")

    def method_C2(self):
        print("Method C2: Specific to class C")

    # Override method from class B
    def method_override(self):
        print("Method Override: This is the overridden method in class C")

# Test the classes
a = A()
b = B()
c = C()

# Call specific methods from each class
print("Calling methods from class A:")
a.method_A1()
a.method_A2()

print("\nCalling methods from class B:")
b.method_A1()  # Inherited from A
b.method_A2()  # Inherited from A
b.method_B1()
b.method_B2()

print("\nCalling methods from class C:")
c.method_A1()  # Inherited from A
c.method_A2()  # Inherited from A
c.method_B1()  # Inherited from B
c.method_B2()  # Inherited from B
c.method_C1()
c.method_C2()

# Call overridden methods
print("\nCalling overridden methods:")
a.method_override()  # Method from A
b.method_override()  # Overridden in B
c.method_override()  # Overridden in C
