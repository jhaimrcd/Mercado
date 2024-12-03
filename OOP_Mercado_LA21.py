class food:
    def __init__(self, mushroom, chicken, cream):
        self.mushroom = mushroom
        self.chicken = chicken
        self.__cream = cream 

    def __str__(self):
        return f"Ang niluto kong ulam ay may {self.mushroom}, {self.chicken}, {self.__cream}."

    def getter(self):
        return self.__cream 

    def setter(self, new_cream):
        self.__cream = new_cream

chicken_creamy_mushroom = food("mushroom", "chicken", "cream")
print(chicken_creamy_mushroom.getter())

chicken_creamy_mushroom.setter("extra cream")
print(chicken_creamy_mushroom.getter())