mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    print(pow(pow(2, n - 1, mod), mod - 2, mod))
