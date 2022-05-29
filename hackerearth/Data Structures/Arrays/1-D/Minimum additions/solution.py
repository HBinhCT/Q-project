t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = map(int, input().strip().split())
    print(max(0, sum(a) // (k + 1) - n + 1))
