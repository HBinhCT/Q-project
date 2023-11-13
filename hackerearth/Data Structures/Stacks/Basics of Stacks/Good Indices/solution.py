t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    res = [0] * n
    lefts = []
    for i in range(n):
        while lefts and a[lefts[-1]] >= a[i]:
            lefts.pop()
        if lefts:
            res[i] += i - lefts[-1] - 1
        else:
            res[i] = -1
        lefts.append(i)
    rights = []
    for i in range(n - 1, -1, -1):
        while rights and a[rights[-1]] >= a[i]:
            rights.pop()
        if rights and res[i] != -1:
            res[i] += rights[-1] - i - 1
        else:
            res[i] = -1
        rights.append(i)
    print(" ".join(map(str, res)))
