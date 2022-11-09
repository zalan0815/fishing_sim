import random
import math

def wich_fish():
    return random.choice(['Ponty', 'Csuka', 'Harcsa'])

def golden_fish():
    print("Gratulálunk!!!")
    print("Kifogtál egy aranyhalat!")
    print("\"Ha visszaengedsz teljesítem 3 kívánságod!\"")

def golden_fish2():
    print("\"Köszönöm, hogy visszaengedtél!\"")
    print("\"Ezért lehet 3 kívánságod!\"")
    for i in range(1, 4):
        input(f"Mi az {i}. kívánságod?: ")
        print("\"Csiribú csiribá! Abraka dabra! A kívánságod teljesűlt!\"")
    print("\"Most pedig vissza megyek a tó mélyére, további szép napot!\"")

def catch():
    percent = random.randint(0, 100)
    if percent <= 50:
        return 'semmi'
    elif percent > 50 and percent <= 99:
        return wich_fish()
    elif percent == 100:
        golden_fish()
        return 'aranyhal'

# asd = random.uniform(6, 7)
# asd = round(asd, 2)
# print(asd)
