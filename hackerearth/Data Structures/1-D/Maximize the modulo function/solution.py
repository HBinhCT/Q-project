t = int(input())
for _ in range(t):
    m, k = map(int, input().strip().split())
    s = input().strip()
    a = list(map(int, s))
    a.reverse()
    mod = 1
    x = []
    y = []
    z = []
    for i in range(m):
        x.append(mod)
        y.append(a[i] * mod)
        mod = (mod * 10) % k
    total = sum(y) % k
    z.append(total)
    new_number = (total - y[-1]) % k
    z.append(new_number)
    for i in range(m - 2, -1, -1):
        new_number -= x[i] * (a[i] - a[i + 1])
        new_number %= k
        z.append(new_number)
    print(max(z))
