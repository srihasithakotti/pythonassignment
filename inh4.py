# Superclass A
class A:
    def __init__(self):
        self.value = "This is class A's data member"
        
    def display_value(self):
        print(self.value)

# Subclass B (inheriting from A)
class B(A):
    def __init__(self):
        super().__init__()
        self.value = "This is class B's data member"  # Overriding data member

# Subclass C (inheriting from B)
class C(B):
    def __init__(self):
        super().__init__()
        self.value = "This is class C's data member"  # Overriding data member

# Test the call using superclass reference to B and C

# Create objects of B and C
b = B()
c = C()

# Call the data member using superclass reference
print("Accessing data member using superclass reference to B:")
a_ref_to_b = A()  # A reference to B object
a_ref_to_b.value = b.value  # Manually binding B's data member to A's reference
print(a_ref_to_b.value)  # Output: This is class B's data member

print("\nAccessing data member using superclass reference to C:")
a_ref_to_c = A()  # A reference to C object
a_ref_to_c.value = c.value  # Manually binding C's data member to A's reference
print(a_ref_to_c.value)  # Output: This is class C's data member
