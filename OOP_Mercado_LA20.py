class food:
    def __init__(self, mushroom, chicken, cream):
        self.mushroom = mushroom
        self.chicken = chicken
        self.__cream = cream 
    def __str__(self):
        return f"AAng niluto kong ulam ay may {self.mushroom}, {self.chicken}, {self.__cream}."
    def getter(self):
        return self.__cream 
    
chicken_creamy_mushroom = food("mushroom", "chicken", "cream")

#print(f"{chicken_creamy_mushroom}")
#print(chicken_creamy_mushroom.__itlog)
print(chicken_creamy_mushroom.getter())