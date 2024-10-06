class Appliances:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating: ")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliances):
    def operate(self):
        print("Washing CLothes!")

class Refrigerator(Appliances):
    def operate(self):
        print("Keeping the food cold!")

class Microwave(Appliances):
    def operate(self):
        print("Heating food!")

washing_machine = WashingMachine("LG", "TWINWash")
refrigerator = Refrigerator("Samsung", "FamilyHub")
microwave = Microwave("Panasonic", "NN-SN966S")

appliances = [washing_machine, refrigerator, microwave]

for appliances in appliances:
    appliances.info()
    appliances.operate()
    print()