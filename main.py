from fishing_functions import *

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
if menu_user_choice == '2':
    pass    


