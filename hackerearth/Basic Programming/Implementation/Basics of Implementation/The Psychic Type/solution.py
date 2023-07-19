n = int(input())
a = list(map(int, input().strip().split()))
s, e = map(int, input().strip().split())
for i in range(1, n + 1):
    x = s - 1
    if s == e or a[x] == e:
        print('Yes')
        break
    if i == n:
        print('No')
        break
    s = a[x]
