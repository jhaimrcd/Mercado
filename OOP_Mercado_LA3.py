class character:
    def __init__(self, name):
        self.name = name

    def describe(self, role):
        print(f"{self.name} is a {role} hero.")
    
hero_ml = character("Chang'e")
hero_ml.describe("Mage")