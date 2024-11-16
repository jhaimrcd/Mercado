class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} cannot attack because they are out of health!")
            return
        damage = self.attack_power
        target.health -= damage
        print(f"{self.name} attacked {target.name} for {damage} damage.")
        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{target.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} points. Current health: {self.health}")

player1 = Player("Warrior", 100, 15)
player2 = Player("Mage", 80, 20)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player1.name} wins!")
        break
    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player2.name} wins!")
        break

print("\nBonus demonstration:")
player1.heal(20)
player2.heal(10)
