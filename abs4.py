from abc import ABC, abstractmethod

class Animal(ABC):
    
    def speak(self):
        print("This animal makes a sound.")
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    
    def sound(self):
        print("Woof!")
    
    def create_and_call_non_abstract(self):

        dog_instance = Dog()
        
    
        dog_instance.speak()  

dog = Dog()
dog.create_and_call_non_abstract()