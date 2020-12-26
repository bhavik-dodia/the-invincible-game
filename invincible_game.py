import random
import time

SEQ = [12, 23, 34, 45, 56, 67, 78, 89]

def cpu_starts():
    cpu = 1
    total = 0
    while True:
        time.sleep(1)
        print(f'\nCPU chooses: {cpu}')
        total += cpu
        print(f'Total: {total}')

        if total >= 100:
            print('\nCPU wins!!!\nBetter luck next time!!')
            break

        num = int(input('\nChoose a number [1-10]: '))
        while not 1 <= num <= 10:
            num = int(input('Choose a number between 1 to 10 only: '))
        total += num
        print(f'Total: {total}')
        cpu = 11 - num

        if total >= 100:
            print('\nCongratulations, You just won The Invincible Game!!!')
            break


def player_starts():
    total = 0
    while True:
        num = int(input('\nChoose a number [1-10]: '))
        while not 1 <= num <= 10:
            num = int(input('Choose a number between 1 to 10 only: '))
        total += num
        print(f'Total: {total}')

        if total >= 100:
            print('\nCongratulations, You just won The Invincible Game!!!')
            break

        cpu = min([abs(i - total) for i in SEQ]) % 11
        if cpu == 0:
            cpu = random.randint(1, 10)
        elif total + cpu in SEQ:
            ...
        else:
            cpu = 11 - num

        time.sleep(1)
        print(f'\nCPU chooses: {cpu}')
        total += cpu
        print(f'Total: {total}')

        if total >= 100:
            print('\nCPU wins!!!\nBetter luck next time!!')
            break


def two_player_mode(turn_p1):
    total = 0
    while True:
        if turn_p1:
            num = int(input('\nPlayer 1: Choose a number [1-10]: '))
            while not 1 <= num <= 10:
                num = int(
                    input('Player 1: Choose a number between 1 to 10 only: '))
            total += num
            print(f'Total: {total}')
            if total >= 100:
                print('\nPlayer 1 wins!!!')
                break
        else:
            num = int(input('\nPlayer 2: Choose a number [1-10]: '))
            while not 1 <= num <= 10:
                num = int(
                    input('Player 2: Choose a number between 1 to 10 only: '))
            total += num
            print(f'Total: {total}')
            if total >= 100:
                print('\nPlayer 2 wins!!!')
                break

        turn_p1 = not turn_p1
