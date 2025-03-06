class MyClass:
    def _init_(self):
        self.existing_field = "This is an existing field."

def generate_no_such_field_exception():
    try:
    
        obj = MyClass()
        print(obj.non_existent_field)  
    except AttributeError as e:
    
        print(f"AttributeError: {e}")

def main():
    print("Attempting to generate NoSuchFieldException...")
    generate_no_such_field_exception()

main()