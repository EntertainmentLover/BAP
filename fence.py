def find_p(n, k, h):
    c_sum = sum(h[:k])
    m_sum = c_sum
    m_indx = 0
    for i in range(1, n-k+1):
        c_sum = c_sum - h[i - 1]+h[i + k - 1]
        if c_sum < m_sum:
            m_sum = c_sum
            m_indx = i
    return m_indx + 1

n, k = input().split()
n, k = int(n), int(k)
h = [int(x) for x in input().split()]

result = find_p(n, k, h)

print(result)
