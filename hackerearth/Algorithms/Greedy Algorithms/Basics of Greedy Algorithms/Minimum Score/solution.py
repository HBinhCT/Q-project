n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
x = a[0]
subs = []
for i in range(n):
    if a[i] != x:
        x = a[i]
        subs.append(i)
m = len(subs)
h = k - 1
if m >= k:
    print(1)
    for i in range(1, k):
        print(i, i)
    print(k, n)
else:
    if m < h:
        for i in range(n - 1):
            j = i + 1
            if a[i] == a[j]:
                subs.append(j)
                if len(subs) == h:
                    break
        subs.sort()
    print(0)
    subs.insert(0, 0)
    subs.append(n)
    for i in range(k):
        print(subs[i] + 1, subs[i + 1])
