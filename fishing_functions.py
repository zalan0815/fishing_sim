from lake_functions import *
import time
import random


def animation(amount: int):
    time_since_throw = 0
    dot_amount = 0

    # print(f'amount: {amount}')
    # print(f'time_since_throw: {time_since_throw}')

    while time_since_throw < amount:
        time.sleep(1)
        if dot_amount == 0:
            print('Horgászás folyamatban')
            dot_amount += 1
        elif dot_amount == 1:
            print('Horgászás folyamatban.')
            dot_amount += 1
        elif dot_amount == 2:
            print('Horgászás folyamatban..')
            dot_amount += 1
        elif dot_amount == 3:
            print('Horgászás folyamatban...')
            dot_amount = 0
        time_since_throw += 1

bucket = []

mass = 0
length = 0
endangered = False

def manage_fish_fate(mass: float, length: float, endangered: bool):
    pass

def throw_in():
    print('Bedobtad a csalit.\nVárj a kapásra!')
    time_to_catch = random.randint(5, 15)
    animation(time_to_catch)

    print()
    print('KAPÁSOD VAN!!!')
    print()
    print('Ezt fogtad:')
    current_catch = catch()
    if current_catch == 'semmi':
        print(random.choice(['Hínár!', 'Nem fogtál semmit!', 'Gumicsizma!', 'Biciklikerék!', 'AK-47-es gépkarabély! (Hívd a rendőrséget!)']))
    elif current_catch == 'aranyhal':
        print('Aranyhal!')
    else:
        print(f'{catch()}!')
        print()
        print(f'Tömeg: {15} kg')
        print(f'Hossz: {1} m')
        print(f'Védettségi státusz: {0}')
        print()
        print('Mit fogsz csinálni a hallal?')
        fish_fate = input('Visszaengeded[V] / Elrakod[E]').lower()
        while fish_fate != 'v' and fish_fate != 'e':
            fish_fate = input('Visszaengeded[V] / Elrakod[E]').lower()

throw_in()

    

    # current_catch = catch()


    # print(current_catch)

