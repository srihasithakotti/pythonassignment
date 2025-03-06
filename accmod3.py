class MyClass:
    def __init__(self):
        self.public_field = "This is a public field"
    
    def public_method(self):
        print("This is a public method")  
        
class AccessPublicFromDifferentPackage:
    def access_public(self):
        
        obj = MyClass()
        

        print(obj.public_field)  
        obj.public_method()

access_obj = AccessPublicFromDifferentPackage()
access_obj.access_public()
