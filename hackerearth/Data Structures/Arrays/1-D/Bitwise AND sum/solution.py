from sys import stdin

mx = 2 ** 25 - 1
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    counter = {d: n for d in range(25)}
    x = mx
    i = 1
    for j in reversed(a[1:]):
        y = x & j
        if y != x:
            diff = bin(x - y)
            for k, v in enumerate(str(diff)[:1:-1]):
                if v == '1':
                    counter[k] = i
            x = y
            if x == 0:
                break
        i += 1
    total = sum(v * 1 << k for k, v in counter.items())
    values = set(counter.values())
    values.update([0, n - 1])
    ans = total - mx
    x = mx
    i = n - 1
    z = 0
    for j in a:
        y = x & j
        if y != x:
            diff = bin(x - y)
            for k, v in enumerate(str(diff)[:1:-1]):
                if v == '1':
                    total -= counter[k] * 1 << k
                    counter[k] = 0
            x = y
            if x == 0:
                break
        if i in values:
            z = 0
            for k, v in counter.items():
                if i < v:
                    z += 1 << k
        total -= z
        ans += total
        i -= 1
    print(ans)
