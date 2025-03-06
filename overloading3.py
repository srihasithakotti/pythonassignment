class MyClass:
    
    def my_method(self, a, b=None):
        if b is not None:
            print(f"Method called with two parameters: {a}, {b}")
        else:
            print(f"Method called with one parameter: {a}")

obj = MyClass()
obj.my_method(10)
obj.my_method(10, 20)
