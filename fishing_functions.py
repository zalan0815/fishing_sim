from lake_functions import *
from fishes_functions import row_in_fishes, fishes
import time
import random
import math


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


def get_float(row: str, data_number: int):
    return float(row.split(';')[data_number].replace(',', '.'))

def get_string(row: str, data_number: int):
    return row.split(';')[data_number]






def manage_fish():


    row_number = random.randint(0, len(fishes)-1)
    # print(row_number)
    # print(row_in_fishes(row_number))

    fish_name = get_string(row_in_fishes(row_number), 0)

    fish_mass = round(random.uniform(get_float(row_in_fishes(row_number), 1), get_float(row_in_fishes(row_number), 2)), 2)

    fish_length = round(random.uniform(get_float(row_in_fishes(row_number), 3), get_float(row_in_fishes(row_number), 4)), 2)

    fish_endangered = False

    if get_string(row_in_fishes(row_number), 5) == 'N':
        fish_endangered = False
    else:
        fish_endangered = True


    print(f'{fish_name}!')
    print()
    print(f'Tömeg: {fish_mass} kg')
    print(f'Hossz: {fish_length} m')
    endangered_status_converted = ''
    if fish_endangered == False:
        endangered_status_converted = 'Nem fenyegetett'
    else:
        endangered_status_converted = 'Védett'
    print(f'Védettségi státusz: {endangered_status_converted}')
    print()



    print('Mit fogsz csinálni a hallal?')
    fish_fate = input('Visszaengeded[V] / Elrakod[E]').lower()
    while fish_fate != 'v' and fish_fate != 'e':
        fish_fate = input('Visszaengeded[V] / Elrakod[E]').lower()
    

    converted_row_to_bucket = f'{fish_name};{fish_mass};{fish_length}'

    if fish_fate == 'e':
        if fish_endangered == True:
            print('Nem rakhatsz el védett halat! Megbüntetett a halőr!')
            print('Halőr: Ejnye-bejnye! Többet ilyet meg ne lássak!')
        else:
            bucket.append(converted_row_to_bucket)

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
        manage_fish()
        
        

for i in range (1 , 6):
    input('ENTER a következő bedobáshoz...')
    print(i)
    throw_in()
    print('Vödör tartalma:')
    for fish in bucket:
        print(f'\tFaj: {get_string(fish, 0)} | Tömeg: {get_float(fish, 1)} | Hossz: {get_float(fish, 2)}')
    print()


#dfasf



    # current_catch = catch()


    # print(current_catch)

