#formula (S*P)/(100+S)
#s = int(input("Введите начальную сумму: "))
#p = 0.07
#t = 5
#a = s*(1+p)**t
#print(a)



#m = [-7, 0, 1, 2, 4, 5, 6, 13, 26, 33]
#a = []
#s = set()
#n = 6
#for i in m:
#    t = 6 - i
#    if t in s:
#        a.append((t, i))
#    s.add(i)
#print(a)


#m = [-7, 0, 1, 2, 4, 5, 6, 13, 26, 33]
#a = []
#s = set()
#n = 6
#for i in m:
#    t = 6 - i
#    if t in s:
#        a.append((t, i))
#    s.add(i)
#print(a)


# p = int(input("Кол-во людей: "))
# c_25 = c_50 = 0
# for _ in range(p):
#     m = int(input("Сколько заплотил: "))
#     if m == 25:
#         c_25 += 1
#     elif m == 50:
#         if c_25 > 0:
#             c_25 -= 1
#             c_50 += 1
#         else:
#             print("no")
#             break
#     elif m == 100:
#         if c_50 > 0 and c_25 > 0:
#             c_50 -= 1
#             c_25 -= 1
#         elif c_25 >= 3:
#             c_25 -= 3
#         else:
#             print('no')
#             break
# else:
#     print("yes")



# def bank(s, p, t):
#     if t == 0:
#         return s
#     return bank(s*(1+p/100), p, t-1)

# s = int(input("Введите сумму: "))
# p = float(input("Введите проценты: "))
# t = int(input("Введите время: "))
# print(bank(s, p, t))
    


# def adding(a, b):
#     if b == 0:
#         return a
#     return adding(a + 1, b - 1)

# a = int(input("First: "))
# b = int(input("Second: "))
# print(adding(a, b))