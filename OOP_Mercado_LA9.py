class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"

car = Car("Audi")
print(car)
del car
print(car)