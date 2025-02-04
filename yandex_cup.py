#н кол-во дисков
#w/h
#ящики бесконечные
#размер ящиков и дисков произвольные

def len_kapes_bee(w, h, d):
    f_rows = h//d
    if f_rows > 1:
        columns = w//d
    else:
        columns = w//d
    count = 0
    for i in range(f_rows):
        if i % 2 == 0:
            count += columns
        else:
            count += max(0, columns - 1)
    return count 

def len_kapes_vert(w, h, d):
    return (w//d)*(h//d)

def len_kapes_horizont(w, h, d):
    return (w//d)*(h//d)

def razmeshenie_len_kapes(w, h, d):
    vert = len_kapes_vert
    horizont = len_kapes_horizont
    bee = len_kapes_bee
    disks = max(vert, horizont, bee)
    if disks == vert:
        return "Vertical", disks
    elif disks == horizont:
        return "Horizontal", disks
    else:
        return "Bee", disks
    
n = int(input("Кол-во дсков: "))
d = float(input("Диаметр дисков: "))
w = float(input("Ширина ящиков: "))
h = float(input("Высота ящиков: "))
result, counts = razmeshenie_len_kapes(w, h, d)
print(f"Optimal razmeshenie: {result}, count of disks{counts}")