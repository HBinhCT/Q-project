t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    print(max(0, k - min(a)))
