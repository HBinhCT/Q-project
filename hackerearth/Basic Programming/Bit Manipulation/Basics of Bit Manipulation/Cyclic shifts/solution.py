t = int(input())
for _ in range(t):
    n, m, c = input().strip().split()
    n = int(n)
    m = int(m)
    x = bin(n)[2:].zfill(16)
    if "L" == c:
        ans = x[m:] + x[:m]
        print(int(ans, 2))
    elif "R" == c:
        ans = x[-m:] + x[:-m]
        print(int(ans, 2))
