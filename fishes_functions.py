from data import *
import time


fishes = []

felirat = (f"""\033[91m
 _________________________________________________________________________________________________
|   _____ ______   __   __  __  ____ _______    __ _____      _   __   _        ____  ______   _   |
|  / ____|___  /  /_/  |  \/  |/ __ \__   __|  /_/|  __ \    | | /_/  | |      |  _ \|  ____| | |  |
| | (___    / /   / \  | \  / | |  | | | |    |_ _| |__) |   | | / \  | |      | |_) | |__    | |  |
|  \___ \  / /   / _ \ | |\/| | |  | | | |     | ||  _  /_   | |/ _ \ | |      |  _ <|  __|   | |  |
|  ____) |/ /__ / ___ \| |  | | |__| | | |     | || | \ \ |__| / ___ \| |____  | |_) | |____  |_|  |
| |_____//_____/_/   \_\_|  |_|\____/  |_|    |___|_|  \_\____/_/   \_\______| |____/|______| (_)  |
|__________________________________________________________________________________________________|

\033[0m""")

f = open('halallomany.csv', 'r', encoding='UTF-8')
f.readline()
for row in f:
    d = data(row.strip())
    fishes.append(d)
f.close()

def write_file():
    f = open('halallomany.csv', 'w', encoding='UTF-8')
    f.write('Name;MinMass;MaxMass;MinLength;MaxLength;IsEndangered\n')
    for d in fishes:
        row = f'{d.name};{d.min_mass};{d.max_mass};{d.min_length};{d.max_length};{d.endangered};\n'
        f.write(row)
    f.close()

def check(word):
    try:
        word = float(word) or int(word)
        return (float(word))
    except ValueError:
        return False

def new_fish():
    name = input('Hal neve: ')
    min_mass = input('Hal minimum sulya: ')
    while check(min_mass) == False:
        print(felirat)
        time.sleep(2)
        min_mass = input('Hal minimum sulya: ')
    max_mass = input('Hal maximum sulya: ')
    while check(max_mass) == False:
        print(felirat)
        time.sleep(2)
        max_mass = input('Hal maximum sulya: ')
    min_length = input('Hal minimum hossza: ')
    while check(min_length) == False:
        print(felirat)
        time.sleep(2)
        min_length = input('Hal minimum hossza: ')
    max_length = input('Hal maximum hossza: ')
    while check(max_length) == False:
        print(felirat)
        time.sleep(2)
        max_length = input('Hal maximum hossza: ')
    endangered = input('Hal védettsége (I/N): ').upper()
    if endangered == 'I':
        endangered = 'Y'
    
    
    
    row = f'{name};{min_mass};{max_mass};{min_length};{max_length};{endangered}\n'
    f = open('halallomany.csv', 'a', encoding='UTF-8')
    f.write(row)
    f.close()

    fishes.append(data(row))

def modify_fish():
    name = input('Név: ')
    for d in fishes:
        if d.name.lower() == name.lower():
            d.min_mass = input('Minimum súly: ')
            while check(d.min_mass) == False:
                print(felirat)
                time.sleep(2)
                d.min_mass = input('Minimum súly: ')
            d.max_mass = input('Maximum súly: ')
            while check(d.max_mass) == False:
                print(felirat)
                time.sleep(2)
                d.max_mass = input('Maximum súly: ')
            d.min_length = input('Minimum hossz: ')
            while check(d.min_length) == False:
                print(felirat)
                time.sleep(2)
                d.min_length = input('Minimum hossz: ')
            d.max_length = input('Maximum hossz: ')
            while check(d.max_length) == False:
                print(felirat)
                time.sleep(2)
                d.max_length = input('Maximum hossz: ')
            d.endangered = input('Védettségi státusz (I/N): ').upper()
            if d.endangered == 'I':
                d.endangered = 'Y'
            write_file()
            return

    print('Ilyen hal nincsen')

def delete_fish():
    count = 1
    for d in fishes:
        print(f'{count}. {d.name}')
        count += 1
    name = input('Hal neve: ')
    for d in fishes:
        if d.name.lower() == name.lower():
            fishes.remove(d)
            write_file()
            return
    print('Ilyen hal nincs')


def row_in_fishes(number):
    return f'{fishes[number].name};{fishes[number].min_mass};{fishes[number].max_mass};{fishes[number].min_length};{fishes[number].max_length};{fishes[number].endangered}'

def list_fishes():
    endangered = ''
    for d in fishes:
        if d.endangered == 'N':
            endangered = 'nem védett'
        elif d.endangered == 'Y':
            endangered = 'védett'
        print(f'{d.name} ({d.min_mass}kg - {d.max_mass}kg, {d.min_length}m - {d.max_length}m, {endangered})')

delete_fish()