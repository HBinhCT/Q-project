t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        print(0)
    else:
        m = 1 << n.bit_length() - 1
        print(((m - 1) * (m - 2) + 3 * (n - m + 1) * (n - m)) // 2)
