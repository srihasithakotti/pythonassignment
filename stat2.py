class MyClass:
    static_var = 100  # Static (class) variable

    def _init_(self, value):
        self.instance_var = value  # Instance variable

# Creating an instance
obj = MyClass(50)

# Accessing the static variable through the instance
print("Static Variable:", obj.static_var)

# Accessing the static variable through the class (preferred way)
print("Static Variable (via class):", MyClass.static_var)

# Accessing the instance variable
print("Instance Variable:", obj.instance_var)