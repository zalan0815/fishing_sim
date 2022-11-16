import os 
import time
from fishes_functions import check

felirat = """
   _____ ______ __                  _     __     _   __  _   _          
  / ____|___  //_/                 | |   /_/    (_) /_/ | | | |         
 | (___    / / __ _ _ __ ___   ___ | |_   _ _ __ _  __ _| | | |__   ___ 
  \___ \  / / / _` | '_ ` _ \ / _ \| __| | | '__| |/ _` | | | '_ \ / _ \
  ____) |/ /_| (_| | | | | | | (_) | |_  | | |  | | (_| | | | |_) |  __/
 |_____//_____\__,_|_| |_| |_|\___/ \__| |_|_|  | |\__,_|_| |_.__/ \___|
                                               _/ |                     
                                              |__/                      
"""

files = os.listdir()
files.pop(0)
files.pop(len(files) - 1)

users = []
def list_users():
    for f in files:
        type = f.split('.')
        if type[1] == 'csv' and type[0] != 'halallomany':
            users.append(type[0])

    count = 1
    os.system("cls")
    print("--------------------------------------------------------------------------------")
    print("Profilok:")
    for u in users:
        print(f'{count} - {u}')
        count += 1
    print(f'\n{count} - Új felhasználó regisztrálása')
    print(f'\n0 - Kilépés')
    print("--------------------------------------------------------------------------------")

def new_user():
    os.system("cls")
    print("--------------------------------------------------------------------------------")
    print("Új felhasználó létrehozása")
    print('0 - Mégse')
    user_name = input('Felhasználó név: ')
    if user_name == '0':
        user()
    print("Sikeresen létrehoztuk az új profilt!")
    print("--------------------------------------------------------------------------------")
    f = open(f'{user_name}.csv', 'w', encoding='UTF-8')
    f.write('Name;Mass;Length\n')
    f.close()

def user():
    os.system("cls")
    list_users()
    choice = input('Választás: ')
    while check(choice) == False:
        os.system("cls")
        print(f"\033[91m{felirat}\033[0m")
        time.sleep(10)
        user()
    if check(choice) > 0 and check(choice) <= len(users):
        return f'{users[int(choice) - 1]}.csv'
    elif check(choice) > len(users):
        new_user()
user()