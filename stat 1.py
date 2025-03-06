class MyClass:
    
    static_variable = 0

    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Instance value: {self.value}")
        print(f"Static variable: {MyClass.static_variable}")

    @classmethod
    def increment_static_variable(cls):
        cls.static_variable += 1
print(MyClass.static_variable)  
MyClass.increment_static_variable()
print(MyClass.static_variable)  


obj = MyClass(10)
obj.display()