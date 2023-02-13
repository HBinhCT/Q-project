from sys import stdin

mx = 1000000000


def get_min_val(x, size, d1, d2, d3, d4):
    m1 = m2 = 0
    for j in range(size - 1):
        u = v = mx
        if d1[j] <= x:
            u = m1
        if d2[j] <= x:
            u = min(u, m2)
        m1 += 1
        m2 += 1
        if d3[j] <= x:
            v = m1
        if d4[j] <= x:
            v = min(v, m2)
        m1 = u
        m2 = v
    return min(m1, m2)


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().strip().split()))
    b = list(map(int, stdin.readline().strip().split()))
    diff_a = []
    diff_ab = []
    diff_b = []
    diff_ba = []
    for i in range(1, n):
        diff_a.append(abs(a[i] - a[i - 1]))
        diff_ab.append(abs(a[i] - b[i - 1]))
        diff_b.append(abs(b[i] - b[i - 1]))
        diff_ba.append(abs(b[i] - a[i - 1]))
    diff = sorted(set(diff_a) | set(diff_ab) | set(diff_ba) | set(diff_b))
    left = 0
    right = len(diff)
    while left < right:
        mid = (left + right) // 2
        if get_min_val(diff[mid], n, diff_a, diff_ab, diff_ba, diff_b) <= k:
            right = mid
        else:
            left = mid + 1
    print(diff[left])
