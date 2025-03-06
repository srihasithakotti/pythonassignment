class Car:
    def __init__(self, make, model, year):
        # Constructor attributes (instance variables)
        self.make = make
        self.model = model
        self.year = year
        
        # A simple attribute initialized to a constant value
        self.is_running = False

    def start_engine(self):
        # Method to start the car engine
        self.is_running = True
        print(f"The engine of {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        # Method to stop the car engine
        self.is_running = False
        print(f"The engine of {self.year} {self.make} {self.model} has stopped.")

    def display_car_info(self):
        # Display car details
        print(f"Car Details: {self.year} {self.make} {self.model}")
        print(f"Engine Running: {self.is_running}")


# Main program to create objects and illustrate constructor attributes
if __name__ == "__main__":  # Corrected the typo here
    # Create a Car object with constructor attributes
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2023)

    # Display car information
    print("Car 1:")
    car1.display_car_info()

    print("\nCar 2:")
    car2.display_car_info()

    # Start the engine of car1 and display info again
    print("\nStarting the engine of Car 1...")
    car1.start_engine()
    car1.display_car_info()

    # Stop the engine of car1 and display info again
    print("\nStopping the engine of Car 1...")
    car1.stop_engine()
    car1.display_car_info()
