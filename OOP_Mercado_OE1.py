class heroML():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type

hero = heroML("Hilda", "Tank", "Physical")
print(f"{hero.name} is a {hero.role} that deals {hero.dmg_type} damage.")

hero = heroML("Nana", "Mage", "Magic")
print(f"{hero.name} is a {hero.role} that deals {hero.dmg_type} damage.")

hero_ = heroML("Gusion", "Assassin", "Magic")
print(f"{hero.name} is a {hero.role} that deals {hero.dmg_type} damage.")

hero = heroML("Natan", "Marksman", "Magic")
print(f"{hero.name} is a {hero.role} that deals {hero.dmg_type} damage.")

hero = heroML("Badang", "Fighter", "Physical")
print(f"{hero.name} is a {hero.role} that deals {hero.dmg_type} damage.")