from sys import stdin

n, q = map(int, stdin.readline().strip().split())
a = stdin.readline().strip().split()
b = [sum(map(int, i)) for i in a]
a = list(map(int, a))
for _ in range(q):
    i = int(stdin.readline())
    ans = -1
    for j in range(i, n):
        if a[i - 1] < a[j] and b[i - 1] > b[j]:
            ans = j + 1
            break
    print(ans)
