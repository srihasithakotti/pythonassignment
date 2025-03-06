class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_car_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

person = Person("John", 30)
person.display_info()  

car = Car("Toyota", "Corolla")
car.display_car_info()
