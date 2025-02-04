def success(abiziany):
    for lol, empty in abiziany:
        itog = lol * empty
        if itog <= 5:
            return False
    return True

abiziany = []

for i in range(1, 6):
    while True:
        try:
            lol = float(input(f'Abiziana {i} - Loyalty: '))
            empty = float(input(f'Abiziana {i} - Empathy: '))
            if 0 <= lol <= 10 and 0 <= empty <= 10:
                abiziany.append((lol, empty))
                break
            else:
                print("REPEAT BLIN")
        except ValueError:
            print("ERROR! NO NUMBER")

if success(abiziany):
    print("WELL DONE, ХОРОШИЙ САНТА ЕПТА")
else:
    print("HUINYA")