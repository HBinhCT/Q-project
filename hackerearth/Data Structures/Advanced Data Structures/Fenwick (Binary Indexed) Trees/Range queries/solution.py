t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    a = list(map(int, input().strip().split()))
    subs = [0] * (n + 2)
    for i in range(1, n + 1):
        subs[i] = subs[i - 2] ^ i
    indexes = {}
    for i, v in enumerate(a, start=1):
        indexes[v] = i
    lefts = [n + 2] * (n + 1)
    rights = [-1] * (n + 1)
    for i in range(1, n + 1):
        lefts[i] = min(lefts[i - 1], indexes[i])
        rights[i] = max(rights[i - 1], indexes[i])
    res = []
    for i in range(q):
        l, r = map(int, input().strip().split())
        start = 1
        end = n
        idx = 0
        while start <= end:
            mid = (start + end) // 2
            if lefts[mid] < l or rights[mid] > r:
                end = mid - 1
            else:
                idx = mid
                start = mid + 1
        res.append(subs[idx])
    print(*res)
