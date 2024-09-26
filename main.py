# n = int(input("Groups: "))
# count1 = count2 = count3 = count4 = 0
# for i in range(n):
#     Si = int(input("How many people in group: "))
#     if Si == 1:
#         count1 += 1
#     elif Si == 2:
#         count2 += 1
#     elif Si == 3:
#         count3 += 1
#     elif Si == 4:
#         count4 += 1
# t = 0
# t += count4
# t += count3
# count1 -= count3
# if count1 < 0:
#     count1 = 0
# t += count2 // 2
# if count2 % 2 == 1:
#     t += 1
#     count1 -= 2
# if count1 < 0:
#     count1 = 0
# t += (count1 +3) // 4
# print(t)


# p = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
# n = int(input("Number of cola: "))
# l = len(p)
# round = 1
# while n > l * round:
#     n -= l * round
#     round += 1
# index = (n - 1) // round
# print(p[index])







































