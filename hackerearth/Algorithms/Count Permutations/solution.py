mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    prev = 0
    count = 1
    for i, v in enumerate(a):
        if v < prev or v <= i:
            print(0)
            break
        elif v == prev:
            count = count * (prev - i) % mod
        else:
            prev = v
    else:
        print(count)
