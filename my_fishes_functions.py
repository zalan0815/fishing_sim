from data import data2
from users import user

file = user()

my_fishes = []

def read_file():
#    f.clear()
    f = open(file, 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = data2(row.strip())
        my_fishes.append(r)
    f.close()

def write_file():
    f = open(file, 'w', encoding='UTF-8')
    f.write('Name;Mass;Length\n')
    for m in my_fishes:
        row = f'{m.name};{m.mass};{m.length}\n'
        f.write(row)

def store_fishes(fishes):
    for fish in fishes:
        f = open(file, 'a', encoding='UTF-8')
        f.write(f'{fish}\n')
        f.close()

        d = data2(fish)
        my_fishes.append(d)

def search_by_name():
    name = input('Halfaj(részlet) keresése: ')
    for f in my_fishes:
        if name.lower() in f.name.lower():
            print(f'{f.name} ({f.mass}kg, {f.length}m)')
    input('\n')

def all_of_my_fishes():
    for f in my_fishes:
        print(f'{f.name} ({f.mass}kg, {f.length}m)')
        
def eat_fish():
    count = 1
    for f in my_fishes:
        print(f'{count} - {f.name} ({f.mass}kg, {f.length}m)')
        count += 1
    my_fishes.pop(int(input('Választás: ')) - 1)
    write_file()
    print("Nyam nyam nyam")

def biggest_fish(criterion):
    if criterion == 'súly':
        max_mass = my_fishes[1].mass
        index = 1
        for i in range(1, len(my_fishes)):
            if my_fishes[i].mass > max_mass:
                max_mass = my_fishes[i].mass
                index = i

        max_mass_indexes = []
        for i in range(0, len(my_fishes)):
            if my_fishes[i].mass == max_mass:
                max_mass_indexes.append(i)
        for i in max_mass_indexes:
            print(f'{my_fishes[i].name} - {my_fishes[i].mass}kg')


    if criterion == 'hossz':
        longest = my_fishes[1].length
        index = 1
        for i in range(1, len(my_fishes)):
            if my_fishes[i].length > longest:
                longest = my_fishes[i].length
                index = i

        max_mass_indexes = []
        for i in range(0, len(my_fishes)):
            if my_fishes[i].length == longest:
                max_mass_indexes.append(i)
        for i in max_mass_indexes:
            print(f'{my_fishes[i].name} - {my_fishes[i].length}m')

read_file()
# biggest_fish('súly')
# biggest_fish('hossz')
# #search_by_name()
all_of_my_fishes()
#eat_fish()
