class MyClass:
    
    static_variable = 0

    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Instance value: {self.value}")
        print(f"Static variable: {MyClass.static_variable}")

    def modify_static_variable(self, new_value):
        MyClass.static_variable = new_value  


obj1 = MyClass(10)
obj2 = MyClass(20)


obj1.display()
obj2.display()


obj1.modify_static_variable(100)


obj1.display()
obj2.display()


    