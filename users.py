import os 
import time
from fishes_functions import check, felirat

wrong_password = (f"""\033[91m
 _______________________________________________________________________________
|  _    _ _____ ____    __    _____        _ ______ _       _____ ______ __  _  |
| | |  | |_   _|  _ \  /_/   / ____|      | |  ____| |     / ____|___  //_/ | | |
| | |__| | | | | |_) | / \  | (___        | | |__  | |    | (___    / // _ \| | |
| |  __  | | | |  _ < / _ \  \___ \   _   | |  __| | |     \___ \  / /| | | | | |
| | |  | |_| |_| |_) / ___ \ ____) | | |__| | |____| |____ ____) |/ /_| |_| |_| |
| |_|  |_|_____|____/_/   \_\_____/   \____/|______|______|_____//_____\___/(_) |
|_______________________________________________________________________________|

\033[0m""")

files = os.listdir()
files.pop(0)
files.pop(len(files) - 1)

users = []
def list_users():
    users.clear()
    os.system("cls")
    for f in files:
        type = f.split('.')
        if (type[1] == 'csv' and type[0] != 'halallomany') and (type[1] == 'csv' and type[0] != 'jelszok'):
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

    for u in users:
        users.remove(u)
        users.append(u.lower())

    user_name = input('Felhasználó név: ')
    while user_name.lower() in users:
        print("Már van ilyen nevű felhasználó!")
        print("Válassz másikat!")
        user_name = input('Felhasználó név: ')
    if user_name == '0':
        user()
    password = str(input("Jelszó: "))
    print("Sikeresen létrehoztuk az új profilt!")
    print("--------------------------------------------------------------------------------")
    f = open(f'{user_name}.csv', 'w', encoding='UTF-8')
    f.write('Name;Mass;Length\n')
    f.close()

    f = open(f'jelszok.csv', 'a', encoding='UTF-8')
    f.write(f'{user_name};{password}\n')
    f.close()
    return f'{user_name}.csv'

def login(user_name, choice):
    f = open(f'jelszok.csv', 'r', encoding='UTF-8')
    for row in f:
        data = row.strip().split(';')
        if user_name == data[0]:
            pw = input('Jelszó: ')
            while pw != data[1]:
                print(wrong_password)
                try_again = input('Újra próbálod? (I/N): ')
                if try_again == 'N':
                    user()
                pw = input('Jelszó: ')
            f.close()
            return f'{users[int(choice) - 1]}.csv'

def user():
    os.system("cls")
    list_users()
    choice = input('Választás: ')
    while check(choice) == False:
        os.system("cls")
        print(felirat)
        time.sleep(2)
        user()
    if check(choice) > 0 and check(choice) <= len(users):
        return login(users[int(choice)-1], choice)
    elif check(choice) > len(users):
        return new_user()

user()