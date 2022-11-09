import os 

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
    for u in users:
        print(f'{count} - {u}')
        count += 1
    print(f'\n{count} - Új felhasználó regisztrálása')
    print(f'\n0 - Kilépés')

def new_user():
    user_name = input('Felhasználó név: ')
    f = open(f'{user_name}.csv', 'w', encoding='UTF-8')
    f.write('Name;Mass;Length\n')
    f.close()

def user():
    list_users()
    choice = int(input('Választás: '))
    if choice > 0 and choice <= len(users):
        return f'{users[choice - 1]}.csv'
    elif choice > len(users):
        new_user()
