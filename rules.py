from random import choice
from monsters import gosma, dragon, demon, goblin, angel

def spawn_monster():
        monster_class = choice([angel.Angel])
        return monster_class()