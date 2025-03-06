# Superclass A
class A:
    def method_override(self):
        print("Method Override: This is the method from class A")

# Subclass B (inheriting from A)
class B(A):
    def method_override(self):
        print("Method Override: This is the overridden method in class B")

# Subclass C (inheriting from B)
class C(B):
    def method_override(self):
        print("Method Override: This is the overridden method in class C")

# Test the call using superclass reference
# Create objects of B and C
b = B()
c = C()

# Call the overridden method with superclass reference to B and C
print("Calling overridden method with superclass reference to B:")
a_ref_to_b = A()  # A reference to B object
a_ref_to_b.method_override = b.method_override  # Binding B's method to A's reference
a_ref_to_b.method_override()  # Output: Method Override: This is the overridden method in class B

print("\nCalling overridden method with superclass reference to C:")
a_ref_to_c = A()  # A reference to C object
a_ref_to_c.method_override = c.method_override  # Binding C's method to A's reference
a_ref_to_c.method_override()  # Output: Method Override: This is the overridden method in class C
