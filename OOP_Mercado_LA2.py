class heroML():
    def __init__(self, hero, role):
        self.hero = hero
        self.role = role
ml_hero = heroML("Estes", "Support")
print(ml_hero.hero, ml_hero.role)