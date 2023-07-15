q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().strip().split()))
    x, a, b, t = map(int, input().strip().split())
    counter = [0] * n
    for i in range(1, t + 1):
        counter[x] += 1
        x = (a * x + b) % n
    ans = 0
    for i in range(n):
        ans += counter[i] // p[i]
    print(ans)
