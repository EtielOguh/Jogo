from rules import spawn_monster, try_drop_item, show_menu, clear
from player.player_base import Player
from animation import battle_animation
import sys


def Battle(player):
    print(f"Here is where your story begin! {player.name}!\n")

    while player.player_is_alive():
        monster = spawn_monster(player.zone)

        while monster.enemy_is_alive() and player.player_is_alive():
            player.stats()
            print(monster.battle_cry())
            action = show_menu()
            
            if action == 'a':
                battle_animation()
                
                while monster.enemy_is_alive() and player.player_is_alive():
                    player.attack_enemy(monster)

                    if monster.enemy_is_alive():
                        monster.attack_player(player)
                    if player.health <= 20 or monster.attack > player.health:
                        if player.potion > 0:
                            player.potion_use()

                if not monster.enemy_is_alive():
                    clear()
                    print(f"\n{monster.name} Defeated!")
                    player.exp_wins(monster)
                    monster.drop_money(player)
                    player.potion_drops()
                    try_drop_item(player)
                    Player.save_player(player)

            elif action == 'b':
                clear()
                player.potion_use()
                
            elif action == 'z':
                change = False  # Inicializa a variável para evitar erro
                if player.money >= 50:
                    player.money -= 50
                    change = player.change_zone()
                if change:
                    clear()
                    monster = spawn_monster(player.zone)
                    print(monster.battle_cry())
                else:
                    print("You don't have enough money!")

            elif action == 'x':
                change = False  # Mesma correção aqui
                if player.money >= 50:
                    player.money -= 50
                    change = player.back_zone()
                if change:
                    clear()
                    monster = spawn_monster(player.zone)
                    print(monster.battle_cry())
                else:
                    print("You don't have enough money!")
            
            elif action == 'f':
                clear()
                print('LOSER! Try another one!')
                monster = spawn_monster(player.zone)
                
            elif action == 'i':
                clear()
                Player.equip_itens(player)
                  
            elif action == 's':
                Player.save_player(player)
                sys.exit()
            
            elif action == 'e':
                clear()
                player.show_bag_itens()
            
            else:
                print("Invalid action!")                
                