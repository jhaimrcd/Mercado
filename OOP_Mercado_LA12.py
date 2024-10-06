class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        print(f"Name: {self.name}, Price: {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
    
laruan = Car("Petron Supercars", "700")
print(laruan.name)
laruan.__str__()