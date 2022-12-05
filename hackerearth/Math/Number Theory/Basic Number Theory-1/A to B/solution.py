from sys import stdin

n = int(stdin.readline())
mod = 1000000007
mod_2 = 1000000005
a = [0] + list(map(int, stdin.readline().strip().split()))
bi = 1
zero_cnt = 0
for i in range(1, n + 1):
    if a[i]:
        bi = bi * a[i] % mod
    else:
        zero_cnt += 1
q = int(stdin.readline())
for _ in range(q):
    t, *query = map(int, stdin.readline().strip().split())
    if 0 == t:
        idx, v = query
        prev = a[idx]
        a[idx] = v
        if prev and v:
            bi = bi * pow(prev, mod_2, mod) % mod * v % mod
        elif v:
            bi = bi * v % mod
            zero_cnt -= 1
        elif prev:
            bi = bi * pow(prev, mod_2, mod) % mod
            zero_cnt += 1
    elif 1 == t:
        idx = query[0]
        if not zero_cnt:
            print(bi * pow(a[idx], mod_2, mod) % mod)
        elif zero_cnt == 1 and not a[idx]:
            print(bi)
        else:
            print(0)
