t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    max_val = (1 << 32) - 1
    for i in range(n):
        max_val &= a[i]
        max_val &= b[i]
    print(max_val)
