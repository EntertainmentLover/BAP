def magic_num(n):
    count = 0
    while n > 0:
        max_num = max(map(int, str(n)))
        n -= max_num
        count += 1
    return count
n = int(input("Введите: "))
print(magic_num(n))