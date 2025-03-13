from mob import Enemy, spawn_monster
from random import choice
from knight import Player
from time import sleep

def Battle():
    player = Player()
    print(f"Wellcome to the jungle! {player.name}!")
    player.show_bag_itens()

    while player.player_is_alive():
        monster = spawn_monster(player)
        
        while Enemy.enemy_is_alive(monster) and player.player_is_alive():
            action = input("A for Attack and B for potion: ")
            if action in 'aA':
                while Enemy.enemy_is_alive(monster) and player.player_is_alive():
                    player.attack_enemy(monster)
                    sleep(1)
                    if Enemy.enemy_is_alive(monster):
                        monster.attack_player(player)
                    if not Enemy.enemy_is_alive(monster):
                        print(f'{monster.name} Defeated!')
                        player.potion_drops()
                        break
            elif action in "bB":
                player.potion_use()
                        
                    