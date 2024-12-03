class food:
    def __init__(self, mushroom, chicken, cream):
        self.mushroom = mushroom
        self.chicken = chicken
        self.cream = cream
    def __str__(self):
        return f"Ang niluto kong ulam ay may {self.mushroom}, {self.chicken}, {self.cream}."
    
chicken_creamy_mushroom = food("mushroom", "chicken", "cream")

print(f"{chicken_creamy_mushroom}")