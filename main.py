from fishing_functions import *
from my_fishes_functions import *
from fishes_functions import *
import os

def sub_menu_1():
    os.system('cls')    
    print('Válasszon menüpontot!')
    print('1. Halak kilistázása')
    print('2. Új hal hozzáadása')
    print('3. Hal módosítása')
    print('4. Hal törlése')
    print()
    print('0. Vissza')
    submenu_1_user_choice = input('Választás: ')
    if submenu_1_user_choice == '1':
        list_fishes()
    elif submenu_1_user_choice == '2':
        new_fish()
    elif submenu_1_user_choice == '3':
        modify_fish()
    elif submenu_1_user_choice == '4':
        delete_fish()
    elif submenu_1_user_choice == '0':
        menu()
    else:
        sub_menu_1()
    # while submenu_1_user_choice != '1' and submenu_1_user_choice != '2' and submenu_1_user_choice != '3' and submenu_1_user_choice != '4':
        
    

def sub_menu_2():
    os.system('cls')    
    print('Válasszon menüpontot!')
    print('1. Keresés (név alapján)')
    print('2. Halaim kilistázása')
    print('3. Legnagyobb hal (tömeg)')
    print('4. Legnagyobb hal (hossz)')
    print('5. Hal elfogyasztása')
    print()
    print('0. Vissza')
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
    elif submenu_2_user_choice == '0':
        menu()
    else:
        sub_menu_2()

def menu():
    os.system('cls')    
    print('Üdvözlünk a \033[1;33;40mHorgászok Ligája\033[0m \033[1;37;40m1.1.3\033[0m - ban!')
    print('Válasszon menüpontot!')
    print('1. Játék')
    print('2. Halállomány beállítása')
    print('3. Kapásaim')
    menu_user_choice = input('Választás: ')

    if menu_user_choice == '1':
        start_game()
    elif menu_user_choice == '2':
       
        sub_menu_1()

    elif menu_user_choice == '3':
        
        sub_menu_2()
    else:
        menu()
    
    print()
    input('\033[1;37;40mENTER a menübe való visszatéréshez...\033[0m')
     
    menu()
menu()
    

 