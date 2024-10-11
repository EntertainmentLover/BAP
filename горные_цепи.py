def chains(h, k):
    a = 1
    for i in range(len(h) - 1):
        if abs(h[i] - h[i + 1]) > k:
            a += 1
    return a

def find_k(m, h):
    low = 0
    high = 1000000
    result = -1

    while low <= high:
        mid = (low + high) // 2
        с = chains(h, mid)

        if с == m:
            result = mid
            high = mid - 1
        elif с < m:
            high = mid - 1
        else:
            low = mid + 1

    return result

n, m = input().split()
n, m = int(n), int(m)
h = [int(x) for x in input().split()]

result = find_k(m, h)

print(result)
