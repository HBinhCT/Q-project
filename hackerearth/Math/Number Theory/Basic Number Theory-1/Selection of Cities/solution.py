mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    print(pow(2, n, mod) - 1)
