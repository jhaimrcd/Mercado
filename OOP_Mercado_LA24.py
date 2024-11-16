from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name} swings a sword!")

class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name} casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name} shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print(f"{self.name} casts a healing spell on an ally!")

warrior = Warrior("Ezra")
mage = Mage("Zeref")
archer = Archer("Lindi")
healer = Healer("Porlyusica") 

characters = [warrior, mage, archer, healer]
for character in characters:
    character.attack()