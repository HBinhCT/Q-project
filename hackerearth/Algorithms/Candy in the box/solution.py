t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    if k <= n:
        print(k)
        continue
    k -= n
    x = (k - 1) // (n - 1)
    k -= x * (n - 1)
    print(1 + k if x % 2 else n - k)
