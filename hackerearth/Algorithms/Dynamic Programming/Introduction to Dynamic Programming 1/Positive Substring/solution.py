t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    counter = [0] * (2 * n + 2)
    i = n + 1
    tot = 0
    res = 0
    for c in s:
        counter[i] += 1
        if '0' == c:
            tot -= counter[i + 1]
            i += 1
        else:
            tot += counter[i]
            i -= 1
        res += tot
    print(res)
