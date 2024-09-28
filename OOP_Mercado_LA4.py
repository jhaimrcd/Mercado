class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{hero_ml.name} is a {hero_ml.role} hero."
    
hero_ml = character("Alpha", "Fighter")
print(hero_ml)