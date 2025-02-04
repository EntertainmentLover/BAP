# def lt(n, f):
#     f = [x - 1 for x in f]
#     for i in range(n):
#         a = f[i] - 1
#         b = f[a] - 1
#         c = f[b] - 1
#         if c == i:
#             return "YES"
#     return "NO"

# n = int(input())
# f = [int(x) for x in input().split()]
# print(lt(n, f))


# def metro(n, s, a, b):
#     if a[0] == 1 and a[s-1] == 1:
#         return "Yes"
#     for i in range(s - 1, n): 
#         if a[0] == 1 and a[i] == 1 and b[i] == 1 and b[s - 1] == 1:
#             return "Yes"
#     return "No"

# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(metro(n, s, a, b))


# n = int(input('Длина: '))
# a = list(map(int, input("Первый массив: ").split()))
# b = list(map(int, input("Второй массив: ").split()))
# c = [a[i] - b[i] for i in range(n)]
# max_c = max(c)
# result = [i+1 for i in range(n) if c[i] == max(c)]
# result.sort()
# print(len(result))
# print(' '.join(map(str, result)))



# 1857D
# def solve():
#     t = int(input("Кол-во наборов: "))
#     for _ in range(t):
#         n = int(input("Длина массивов: "))
#         a = list(map(int, input("Первый массив: ").split()))
#         b = list(map(int, input("Второй массив: ").split()))
#         X = [a[i] - b[i] for i in range(n)]
#         maxX = max(X)
#         strong_vertices = [str(i + 1) for i in range(n) if X[i] == maxX]
#         print(len(strong_vertices))
#         print(" ".join(strong_vertices))

# if __name__ == '__main__':
#     solve()

# 1327В
# def solve():
#     t = int(input("Количество тестов: "))
#     for _ in range(t):
#         n = int(input("Количество дочерей и королевств: "))
#         married_princes = set()
#         unmarried_daughter = -1 
        
#         preferences = [] 
        
#         for i in range(1, n + 1):
#             data = list(map(int, input("Массив: ").split()))
#             k = data[0] 
#             choices = data[1:] 
#             preferences.append(choices)
#             married = False 
#             for prince in choices:
#                 if prince not in married_princes:
#                     married_princes.add(prince)
#                     married = True
#                     break
#             if not married and unmarried_daughter == -1:
#                 unmarried_daughter = i 
#         if unmarried_daughter == -1:
#             print("OPTIMAL")
#         else:
#             for prince in range(1, n + 1):
#                 if prince not in married_princes:
#                     print("IMPROVE")
#                     print(unmarried_daughter, prince)
#                     break

# if __name__ == "__main__":
#     solve()

# 707В
# def main():
#     from heapq import heappush, heappop
#     n, m, k = map(int, input("Города, дороги и склады: ").split())
#     g = [[] for _ in range(n+1)]
#     for _ in range(m):
#         u, v, l = map(int, input("Нумеровка и длина двунаправленной дороги: ").split())
#         g[u].append((v, l))
#         g[v].append((u, l))
#     ware = set(map(int, input("Номера городов, в которых склады с мукой:").split())) if k else set()
#     if k == 0 or k == n:
#         print(-1)
#         return
#     INF = 10**18
#     d = [INF]*(n+1)
#     h = []
#     for l in ware:
#         d[l] = 0
#         heappush(h, (0, l))
#     while h:
#         dd, u = heappop(h)
#         if dd != d[u]:
#             continue
#         for v, l in g[u]:
#             nd = dd + l
#             if nd < d[v]:
#                 d[v] = nd
#                 heappush(h, (nd, v))
#     ans = min((d[i] for i in range(1, n+1) if i not in ware), default=INF)
#     print(ans if ans != INF else -1)

# main()
