"""class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self._ingredients = ingredients  
        self.__secret_ingredient = "chef's secret recipe"  

    def __str__(self):
        return f"{self.name} is made with the following ingredients: {', '.join(self._ingredients)}."

sisig = FavoriteFood("Sisig", ["pig snout", "onion", "soy sauce"])
sipo_egg = FavoriteFood("Sipo Egg", ["quail eggs", "mixed veggies", "cream"])
creamy_mushroom = FavoriteFood("Creamy Chicken Mushroom", ["chicken", "cream", "mushroom"])

print(sisig)
print(sipo_egg)
print(creamy_mushroom)
print(f"The private ingredient is: {sisig._FavoriteFood__secret_ingredient}")"""


class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self._ingredients = ingredients 
        self.__secret_ingredient = "chef's secret spice"  

    def __str__(self):
        return f"{self.name} is made with the following ingredients: {', '.join(self._ingredients)}."

sisig = FavoriteFood("Sisig", ["pig snout", "onion", "soy sauce"])
sipo_egg = FavoriteFood("Sipo Egg", ["quail eggs", "mixed veggies", "cream"])
creamy_mushroom = FavoriteFood("Creamy Chicken Mushroom", ["chicken", "cream", "mushroom"])

print(sisig)
print(sipo_egg)
print(creamy_mushroom)
print(sisig.__secret_ingredient)