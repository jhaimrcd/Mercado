class Pagkain:
	def __init__(self, name, procedure, ingredients):
		self.__name = name
		self.procedure = procedure
		self.ingredients = ingredients
	def __str__(self):
		return f"{self.name}, {self.procedure}, {self.ingredients}"
	def pagkain_is_back(self):
		return self.__name
	def privateFoods(self, newfoods):
		self.__name = newfoods

		
sisig_recipe = Pagkain("sisig", "grilled", "pig snout")
sipo_recipe = Pagkain("sipo egg", "cook", "mixed veggies")
msauce_recipe = Pagkain("mushroom sauce", "boil", "mushroom")
sisig_recipe.privateFoods = ("2 sili")
sipo_recipe.privateFoods = ("10 eggs")
msauce_recipe.privateFoods = ("1 mushroom")

print(sisig_recipe.privateFoods, sipo_recipe.privateFoods, msauce_recipe.privateFoods)