from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    
    def sound(self):
        print("Woof!")
    def create_and_call(self):
    
        dog_instance = Dog()
        
        dog_instance.sound() 

dog = Dog()
dog.create_and_call()