import random

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, target):
        if self.health <= 0 or target.health <= 0:
            return
        else:

            counte = self.inventory.count('sword')
            print(f'{self.name} attacked the {target.name} dealing {self.strength + 5 * counte} dmg')
            target.take_damage(self.strength + 5 * counte, self)

    def take_damage(self, amount):
        if self.health - amount > 0:
            self.health -= amount
            print(f'{self.name} is still standing with {self.health}')
        else:
            print(f'{self.name} died')
            self.health -= amount
            



class Hero(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
        self.inventory = []
        self.xp = 0
        self.level = 1
        

    def heal(self):
        if 'health potion' in self.inventory:
            self.health += 30
            self.inventory.remove('health potion')
            print(f'{self.name} healed now is at {self.health} hp')

class Enemy(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
        self.loot = []
    def attack(self, target):
        if self.health <= 0 or target.health <= 0:
            return
        else:

            special_att = random.randint(1, 10)
            if special_att == 7:
                print(f'{self.name} attacked the {target.name} with a special attaack dealing {self.strength + 7} dmg')
                target.take_damage(self.strength + 7)
            else:
                print(f'{self.name} attacked the {target.name} dealing {self.strength} dmg')
                target.take_damage(self.strength)

      

    def take_damage(self, amount, hero):
        loote = random.randint(1, 9)
        if self.health - amount > 0:
            self.health -= amount
            print(f'{self.name} is still standing with {self.health}')
        else:
            print(f'{self.name} died')
            self.health -= amount
            if loote <= 3:
                hero.inventory.append('health potion')
            elif loote >= 7:
                hero.inventory.append('sword')



 

Hero = Hero('Lancelott', 100, 25)
Zombie = Enemy('Zombie', 40, 10)
Goblin = Enemy('Goblin', 35, 10)
Ether = Enemy('Ether', 20, 7)

Hero.attack(Zombie)
Zombie.attack(Hero)
Hero.attack(Zombie)
Goblin.attack(Hero)
Hero.attack(Goblin)
Goblin.attack(Hero)
Hero.attack(Goblin)
print(Hero.inventory)
Ether.attack(Hero)
Hero.attack(Ether)
print(Hero.inventory)
