from data import *

fishes = []

f = open('halallomany.csv', 'r', encoding='UTF-8')
f.readline()
for row in f:
    d = data(row.strip())
    fishes.append(d)
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
        min_mass = input('Hal minimum sulya: ')
    max_mass = input('Hal maximum sulya: ')
    while check(max_mass) == False:
        max_mass = input('Hal maximum sulya: ')
    min_length = input('Hal minimum hossza: ')
    while check(min_length) == False:
        max_mass = input('Hal minimum hossza: ')
    max_length = input('Hal maximum hossza: ')
    while check(max_length) == False:
        max_mass = input('Hal maximum hossza: ')
    endangered = input('Hal védettsége: ')
    
    
    
    row = f'{name};{min_mass};{max_mass};{min_length};{max_length};{endangered}\n'
    f = open('halallomany.csv', 'a', encoding='UTF-8')
    f.write(row)
    f.close()

    fishes.append(data(row))



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
