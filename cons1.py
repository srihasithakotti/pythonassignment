class MyClass:
    
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor called: No arguments")
        elif b is None:
            print(f"One argument constructor called: {a}")
        else:
            print(f"Two arguments constructor called: {a}, {b}")


if __name__ == "__main__":
    
    obj1 = MyClass()  
    

    obj2 = MyClass(10)  
    
    obj3 = MyClass(10, 20)
