def hanoi_pyramid(n, r, ss, es):
    if n == 1:
        print(1, r, es)
    else:
        hanoi_pyramid(n - 1, r, es, ss)
        print(n, r, es)
        hanoi_pyramid(n - 1, ss, r, es)

n = int(input('Disks: '))
hanoi_pyramid(n, 1, 2, 3)