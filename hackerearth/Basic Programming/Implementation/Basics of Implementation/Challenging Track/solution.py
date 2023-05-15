t = int(input())
for _ in range(t):
    n, p = map(int, input().strip().split())
    h = list(map(int, input().strip().split()))
    p -= max(0, h[0])
    if p < 0:
        print('No')
        continue
    i = 1
    while p > 0 and i < n:
        p -= max(0, h[i] - i + h[i] % 2)
        i += 1
    if i == n:
        print('Yes', p)
    else:
        print('No')
