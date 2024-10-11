def shifr_deshirf(num, start, end):
    dec_val = int(num, end)
    if end == 10:
        return str(dec_val)
    result = ''
    while dec_val > 0:
        result = (dec_val % end) + result
        dec_val //= end
    return result if result != '' else '0'
 
num = int("Введите число: ")
start = int("Система счисления числа: ")
end = int("Итоговая система счисления: ")
shifr_deshirf = shifr_deshirf(num, start, end)
print(f"{num} из {start} системы в {end} систему: {shifr_deshirf}")


