class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car = Car("Audi", "Black")
print(f"Original Value: {car.brand} {car.color}")

car.color = "Blue"
print(f"Updated Value: {car.brand} {car.color}")

car2 = Car("Mazda", "White")
print(f"Original Value: {car2.brand} {car2.color}")