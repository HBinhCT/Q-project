t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    print("NO" if k % 2 or k > n * n / 2 else "YES")
