from fishing_functions import *
from my_fishes_functions import *
import os

def menu():
    print('Üdvözlünk a \033[1;33;40mHorgászok Ligája\033[0m \033[1;37;40m1.0.0\033[0m - ban!')
    print('Válasszon menüpontot!')
    print('1. Játék')
    print('2. Halállomány beállítása')
    print('3. Kapásaim')
    print()
    print('0. Kilépés')
    menu_user_choice = input('Választás: ')

    if menu_user_choice == '1':
        start_game()
    elif menu_user_choice == '2':
        pass   
    elif menu_user_choice == '3':
        print('Válasszon menüpontot!')
        print('1. Keresés (név alapján)')
        print('2. Halaim kilistázása')
        print('3. Legnagyobb hal (tömeg)')
        print('4. Legnagyobb hal (hossz)')
        print('5. Hal elfogyasztása')
        submenu_2_user_choice = input('Választás: ')

        if submenu_2_user_choice == '1':
            search_by_name()
        elif submenu_2_user_choice == '2':
            all_of_my_fishes()
        elif submenu_2_user_choice == '3':
            biggest_fish('súly')
        elif submenu_2_user_choice == '4':
            biggest_fish('hossz')
        elif submenu_2_user_choice == '5':
            eat_fish()   
    input()
    os.system('cls')     
    menu()
menu()
    



