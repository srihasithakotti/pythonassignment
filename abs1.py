from abc import ABC, abstractmethod

# Abstract class definition
class MyAbstractClass(ABC):
    
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def abstract_method(self):
        pass
    
    # Non-abstract method (can be inherited or overridden)
    def non_abstract_method(self):
        print("This is a non-abstract method that is implemented in the abstract class.")
        
# Subclass that implements the abstract method
class MyConcreteClass(MyAbstractClass):
    
    # Implement the abstract method
    def abstract_method(self):
        print("This is the implementation of the abstract method.")
        
# Main program to test the functionality
if __name__ == "__main__":
    # Create an object of the concrete subclass
    obj = MyConcreteClass()
    
    # Call the non-abstract method
    obj.non_abstract_method()
    
    # Call the abstract method (now implemented in the subclass)
    obj.abstract_method()
