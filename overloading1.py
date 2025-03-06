class MyClass:
    
    def my_method(self, a):
        print(f"Method with 1 parameter: {a}")
    
    def my_method(self, a, b=None):
        if b is not None:
            print(f"Method with 2 parameters: {a}, {b}")
        else:
            print(f"Method with 1 parameter: {a}")

obj = MyClass()
obj.my_method(10)

obj.my_method(10, 20)