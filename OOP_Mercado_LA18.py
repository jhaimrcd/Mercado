class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} is made with the following ingredients: {', '.join(self.ingredients)}."

sisig = FavoriteFood("Sisig", ["pig snout", "onion", "soy sauce"])
sipo_egg = FavoriteFood("Sipo Egg", ["quail eggs", "mixed veggies", "cream"])
creamy_mushroom = FavoriteFood("Creamy Chicken Mushroom", ["chicken", "cream", "mushroom"])

print(sisig)
print(sipo_egg)
print(creamy_mushroom)