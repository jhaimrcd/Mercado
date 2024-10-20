class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage.")
        print(f"{target.name} has {target.health} health remaining.")

    def special_move(self):
        pass 

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        print(f"{self.name} defends against {attacker.name}'s attack!")
        print(f"{self.name} takes {reduced_damage} damage and has {self.health} health remaining.")

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.is_power_doubled = False  

    def special_move(self):
        print(f"{self.name} uses Shield Bash! Attack power is doubled for the next attack.")
        self.is_power_doubled = True

    def attack(self, target):
        if self.is_power_doubled:
            attack_power = self.power * 2
            self.is_power_doubled = False  
        else:
            attack_power = self.power

        target.health -= attack_power
        print(f"{self.name} attacks {target.name} for {attack_power} damage.")
        print(f"{target.name} has {target.health} health remaining.")
class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball! The target's health is reduced by 100.")
        return 100  

    def attack(self, target):
        target.health -= self.special_move()
        print(f"{target.name} has {target.health} health remaining.")

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! It ignores the target's defense.")
        return self.power  

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50
        print(f"{self.name} now has {self.health} health.")


warrior = Warrior(name="Warrior", health=150, power=30)
mage = Mage(name="Mage", health=100, power=20)
archer = Archer(name="Archer", health=120, power=25)
monster = Monster(name="Monster", health=200, power=40)

print("\n- Battle Begins")
warrior.attack(monster)
monster.special_move()
mage.attack(monster)
archer.attack(monster)

print("\n- Monster Retaliates")
monster.attack(warrior)
monster.attack(mage)
monster.attack(archer)

print("\n- Special Moves")
characters = [warrior, mage, archer, monster]
for character in characters:
    character.special_move()

print("\n- Defend Moves")
warrior.defend(monster)
mage.defend(monster)
archer.defend(monster)

print("\n- Battle Ends")