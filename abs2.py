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

dog = Dog()


dog.speak()  