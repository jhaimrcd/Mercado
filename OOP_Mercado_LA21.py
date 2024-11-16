class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self._ingredients = ingredients 
        self.__secret_ingredient = "Onion" 

    def __str__(self):
        return f"{self.name} is made with the following ingredients: {', '.join(self._ingredients)}."

    def get_secret_ingredient(self):
        return self.__secret_ingredient

    def set_secret_ingredient(self, new_ingredient):
        self.__secret_ingredient = new_ingredient

sisig = FavoriteFood("Sisig", ["pig snout", "soy sauce"])
sipo_egg = FavoriteFood("Sipo Egg", ["quail eggs", "mixed veggies", "cream"])
creamy_mushroom = FavoriteFood("Creamy Chicken Mushroom", ["chicken", "cream", "mushroom"])

print(sisig)
print(sipo_egg)
print(creamy_mushroom)
print(f"The secret ingredient in {sisig.name} is: {sisig.get_secret_ingredient()}")

sisig.set_secret_ingredient("Garlic")
print(f"The updated secret ingredient in {sisig.name} is: {sisig.get_secret_ingredient()}")