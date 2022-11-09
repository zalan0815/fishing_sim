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

new_fish()






