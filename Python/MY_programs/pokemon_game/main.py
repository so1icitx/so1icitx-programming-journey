import random
import sys

class Trainer:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.pokedex = []
  
  def add_pokemon(self, pokemon):
    self.pokedex.append(pokemon)




class Pokemon:
  def __init__(self, name, health, damage, level, element):
    self.name = name
    self.level = level
    self.health = health
    self.damage = damage
    self.element = element
    self.isKnocked = False
  
  def __repr__(self):
    return (f"This level {self.level} {self.name} has {self.health} hit points remaining. They are a {self.element} type Pokemon.")
    


Bob = Trainer('Bob', '37')
Leonardo = Pokemon('Pikachu', 500, 40, 11, 'lightning')
Bob.add_pokemon(Leonardo)
Rias = Trainer('Rias', '19')
FireDragon = Pokemon('Charmander', 500, 40, 17, 'fire')
Rias.add_pokemon(FireDragon)


class Fight:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def start(self):
    dice = random.randint(0, 1)
    if dice == 1:
      begins = self.right
      last = self.left
    else:
      begins = self.left
      last = self.right

    begins_num = 0
    last_num = 0
    while True:
      last.pokedex[last_num].health -= begins.pokedex[begins_num].damage
      
      print(f'{begins.pokedex[begins_num].name} damaged {last.pokedex[last_num].name} and {last.pokedex[last_num].name} is now on {last.pokedex[last_num].health} hp')

      if last.pokedex[last_num].health <= 0:
        last_num += 1
        if len(last.pokedex) <= last_num:
          print(f'{begins.name} won the battle with{begins.pokedex[begins_num].name} with {begins.pokedex[begins_num].health} hit points')
          sys.exit()

      begins.pokedex[begins_num].health -= last.pokedex[last_num].damage
      
      print(f'{last.pokedex[last_num].name} damaged {begins.pokedex[begins_num].name} and now {begins.pokedex[begins_num].name} is on {begins.pokedex[begins_num].health} hp')

      if begins.pokedex[begins_num].health <= 0:
        begins_num += 1
        if len(begins.pokedex) <= begins_num:
          print(f'{last.name} won the battle with{last.pokedex[last_num].name} with {last.pokedex[last_num].health} hit points')
          sys.exit()
      
      
          
sigma = Fight(Rias, Bob)
sigma.start()




  
