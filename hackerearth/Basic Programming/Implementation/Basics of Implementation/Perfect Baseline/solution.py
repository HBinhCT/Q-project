t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    names = [input().strip() for _ in range(n)]
    ans = []
    for i in range(k):
        take = sorted(names[j][i] for j in range(n))
        ans.append(min(take[n >> 1], take[n - 1 >> 1]))
    print("".join(ans))
