from lake_functions import *
from fishes_functions import row_in_fishes, fishes
from my_fishes_functions import store_fishes
import time
import random
import os




def animation(amount: int): #kiírja egymás után hogy horgászás folyamatban amount-szor
    time_since_throw = 0
    dot_amount = 0

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

bucket = [] #Eltárolja a vödör tartalmát


def get_float(row: str, data_number: int): #Egy sorból kiszed egy float-ot
    return float(row.split(';')[data_number].replace(',', '.'))

def get_string(row: str, data_number: int): #Egy sorból kiszed egy stringet
    return row.split(';')[data_number]






def manage_fish():


    row_number = random.randint(0, len(fishes)-1) # Kisorsol egy számot

    fish_name = get_string(row_in_fishes(row_number), 0) # A fishes(class) listából a kisorsolt számú hal nevét visszaadja

    fish_mass = round(random.uniform(get_float(row_in_fishes(row_number), 1), get_float(row_in_fishes(row_number), 2)), 2) # A fishes(class) listából a kisorsolt számú hal tömegét kisorsolja

    fish_length = round(random.uniform(get_float(row_in_fishes(row_number), 3), get_float(row_in_fishes(row_number), 4)), 2) # A fishes(class) listából a kisorsolt számú hal hosszát kisorsolja

    fish_endangered = False

    if get_string(row_in_fishes(row_number), 5) == 'N': # # A fishes(class) listából a kisorsolt számú hal védettségi státuszát visszaadja
        fish_endangered = False
    else:
        fish_endangered = True


    print(f'{fish_name}!')
    print()
    print(f'Tömeg: {fish_mass} kg')
    print(f'Hossz: {fish_length} m')
    endangered_status_converted = ''                                #Kiírja a hal adatait
    if fish_endangered == False:
        endangered_status_converted = 'Nem fenyegetett'
    else:
        endangered_status_converted = 'Védett'
    print(f'Védettségi státusz: {endangered_status_converted}')
    print()



    print('Mit fogsz csinálni a hallal?')
    fish_fate = input('Visszaengeded[V] / Elrakod[E] | Választás: ').lower()     # Felhaszáló döntése a hal sorsáról
    while fish_fate != 'v' and fish_fate != 'e':
        fish_fate = input('Visszaengeded[V] / Elrakod[E] | Választás: ').lower()
    

    converted_row_to_bucket = f'{fish_name};{fish_mass};{fish_length}' # A hal adatait átalakítja kettőspontokkal elválasztott sorrá

    if fish_fate == 'e':
        if fish_endangered == True:  
            print()                                       # Ha a felhasználó elrakja (ha visszaengedi nem történik seemmi)
            print('Nem rakhatsz el védett halat! Megbüntetett a halőr!')    
            print('Halőr: Ejnye-bejnye! Többet ilyet meg ne lássak!')
            print()
        else:
            bucket.append(converted_row_to_bucket)

def throw_in():
    print()
    print('Bedobtad a csalit.\nVárj a kapásra!')
    print()
    time_to_catch = random.randint(5, 15)           # Csali bedobása, idő sorsolása
    animation(time_to_catch)
    

    
    
    print()
    print('\033[93mKAPÁSOD VAN!!! \033[0m')
    print()                                         #Kapás kiírása
    print('Ezt fogtad:')
    current_catch = catch()
    if current_catch == 'semmi':
        print(random.choice(['Hínár!', 'Nem fogtál semmit!', 'Gumicsizma!', 'Biciklikerék!', 'AK-47-es gépkarabély! (Hívd a rendőrséget!)'])) # Ha nem fogott a felhasználó halat
    elif current_catch == 'aranyhal':
        print('\033[33mAranyhal!  \033[0m')
        print()
        golden_fish()
        golden_fish_choice = input('Visszaengeded a halat? [I] / [N]: ').lower()
        while golden_fish_choice != 'i' and golden_fish_choice != 'n':
            golden_fish_choice = input('Visszaengeded a halat? [I] / [N]: ').lower()
        if golden_fish_choice == 'i':
            golden_fish2()
        else:
            print('Az aranyhalat nem engeddet vissza.')
            print('Az aranyhal felrobbant és magával vitte a jobb kezedet.')
            print('Ez meg fogja nehezíteni a horgászatot a számodra.')
    else:
        manage_fish() # Ha fogott a felhasználó halat
        
        

for i in range (1 , 6):
    input('ENTER a bedobáshoz...')
    os.system('cls')
    print(f'{i}. Bedobás')
    throw_in()
    print('Vödör tartalma:')
    print()
    for fish in bucket:
        print(f'\tFaj: {get_string(fish, 0)} | Tömeg: {get_float(fish, 1)} kg | Hossz: {get_float(fish, 2)} m')
        print()



store_fishes(bucket) # vödör fájlba írása3
