t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split()))
    groups = [0] * (n + 1)
    groups[0] = 1
    for i in range(k, n + 1):
        for j in range(i, n + 1):
            groups[j] += groups[j - i]
    print(groups[-1])
