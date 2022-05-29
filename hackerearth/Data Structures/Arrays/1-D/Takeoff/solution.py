t = int(input())
for _ in range(t):
    n, p, q, r = map(int, input().strip().split())
    count = 0
    for i in range(p, n + 1, p):
        if i % q and i % r:
            count += 1
    for i in range(q, n + 1, q):
        if i % p and i % r:
            count += 1
    for i in range(r, n + 1, r):
        if i % q and i % p:
            count += 1
    print(count)
