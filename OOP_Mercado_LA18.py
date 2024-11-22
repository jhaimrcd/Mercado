class CreamyMushroom:
    def __init__(self, chicken, cream, mushroom):
        self.__chicken = chicken
        self.__cream = cream
        self.__mushroom = mushroom

    def __str__(self):
        return f"My Creamy Mushroom has {self.__chicken}kg of chicken, {self.__cream} pack of cream, and {self.__mushroom} can of mushroom."

creamy_mushroom = CreamyMushroom(1, 2, 2)
print(creamy_mushroom)