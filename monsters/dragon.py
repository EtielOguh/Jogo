from mob import Enemy
from random import randint

class Dragon(Enemy):
    def __init__(self, player):
        name = "Dragon"
        level = 90
        attack = randint(0, 6)
        max_health = randint(player.max_health // 2, player.max_health)
        health = max_health  
        

        super().__init__(name, level, attack, health, max_health)

        print(f"{self.name} is gonna kill you! {self.health}/{self.max_health}")
    
        