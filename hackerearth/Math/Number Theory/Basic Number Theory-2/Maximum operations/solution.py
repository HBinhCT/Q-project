def xnor(x, y):
    if x == 0:
        return 1 ^ y
    z = x
    z |= z >> 1
    z |= z >> 2
    z |= z >> 4
    z |= z >> 8
    z |= z >> 16
    z |= z >> 32
    z |= z >> 64
    return z ^ x ^ y


t = int(input())
for _ in range(t):
    a, b, n = map(int, input().strip().split())
    n -= 1
    tmp = n % 3
    if 0 == tmp:
        print(a)
    elif 1 == tmp:
        print(b)
    else:
        c = a ^ b
        d = xnor(max(a, b), min(a, b))
        print(max(c, d))
