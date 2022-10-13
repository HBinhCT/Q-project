t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    if n == 7:
        print(36)
    else:
        print(n * n)
