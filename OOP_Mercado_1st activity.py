class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
        
    def describe(self):
        return f"{self.name} is a/an {self.role} with a/an {self.dmg_type} power"
        
hero_roam1 = hero("akai", "tank", "sustain", 3269, 115)
hero_mage1 = hero("zhask", "mage", "magic damage", 2401, 107)
hero_jungler1 = hero("fanny", "assassin", "attack damage", 2426, 126)
hero_mm1 = hero("claude", "marksman", "attack damage", 2370, 97)
hero_fighter1 = hero("cici", "fighter", "attack damage", 2609, 129)

print(f'''
{hero_roam1.name}
{hero_roam1.role}
{hero_roam1.health} HP 
{hero_roam1.auto_atk_dmg} basic attack damage
{hero_roam1.dmg_type}
{hero_roam1.describe()}

{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.health} HP 
{hero_mage1.auto_atk_dmg} basic attack damage
{hero_mage1.dmg_type}
{hero_mage1.describe()}

{hero_jungler1.name}
{hero_jungler1.role}
{hero_jungler1.health} HP 
{hero_jungler1.auto_atk_dmg} basic attack damage
{hero_jungler1.dmg_type}
{hero_jungler1.describe()}

{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP 
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} HP 
{hero_fighter1.auto_atk_dmg} basic attack damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}
''')