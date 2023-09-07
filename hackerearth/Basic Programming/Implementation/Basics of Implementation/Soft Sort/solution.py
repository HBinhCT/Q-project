mod = 1000000007
t = int(input())
ani = [int(input()) for _ in range(t)]
m = max(ani)
x = 1
f = [x]
for i in range(1, m + 1):
    x = (x * i) % mod
    f.append(x)
for n in ani:
    print((f[n] * 3 + 3) % mod)
