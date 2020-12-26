import os
import invincible_game
import time

rules = f"""
Welcome {os.getlogin()}, to The Invincible Game

Rules:
 1. You can play with either cpu or your friend
 2. Both players will chose a number between 1 to 10 one by one
 3. Each of your choices will be added and the player who reaches the total 100 first wins the invincible game

While playing with CPU you require a lot of good luck to win the invincible game.

Try your luck!
"""
print(rules)

time.sleep(2)
print('In which mode do you want to play?\n1. Single player\n2. Two player')
mode = int(input('Enter your choice [1|2]: '))
while not 1 <= mode <= 2:
    mode = int(input('Choose either 1 or 2 only: '))

if mode == 1:
    print(f'\nWho should go first?\n1. CPU\n2. {os.getlogin()}')

    choice = int(input('Enter your choice [1|2]: '))
    while not 1 <= choice <= 2:
        choice = int(input('Choose either 1 or 2 only: '))

    invincible_game.player_starts() if choice == 2 else invincible_game.cpu_starts()
else:
    print('\nWho should go first?\n1. Player 1\n2. Player 2')

    choice = int(input('Enter your choice [1|2]: '))
    while not 1 <= choice <= 2:
        choice = int(input('Choose either 1 or 2 only: '))

    invincible_game.two_player_mode(True if choice == 1 else False)
