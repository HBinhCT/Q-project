t = int(input())
for _ in range(t):
    x, k = map(int, input().strip().split())
    while x:
        r = x % k
        if r > 1:
            print('NO')
            break
        x //= k
    else:
        print('YES')
