class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"{self.brand}, {self.model}, {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass 

kotse1 = Car("Toyota", "Hilux", "Diesel")
kotse1.describeVehicle()

motor1 = Motorcycle("Yamaha", "Mio FI", "Unleaded")
motor1.describeVehicle()