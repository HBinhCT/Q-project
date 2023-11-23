t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = sorted(map(int, input().strip().split()), reverse=True)
    print(2 * sum(a[:k]))
