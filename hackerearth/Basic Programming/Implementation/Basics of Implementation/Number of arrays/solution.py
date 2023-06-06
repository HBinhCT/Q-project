t = int(input())
for _ in range(t):
    n, k, q = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    s = max(a) if k == 1 else min(a)
    print(s if s < q else 'NO')
