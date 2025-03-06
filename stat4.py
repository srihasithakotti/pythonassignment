class MyClass:
    static_var = 100  # Static (class) variable

    @classmethod
    def update_static_var(cls, new_value):
        cls.static_var = new_value  # Modifying static variable

# Accessing static variable before modification
print("Before update:", MyClass.static_var)

# Modifying static variable using class method
MyClass.update_static_var(200)

# Accessing static variable after modification
print("After update:", MyClass.static_var)