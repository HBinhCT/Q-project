from collections import Counter

mod = 1000000007
n, k = map(int, input().strip().split())
p = list(map(int, input().strip().split()))
if k == 0:
    print(1)
else:
    counts = [1] + list(Counter(p).values())
    ln = len(counts)
    if k > ln:
        print(0)
    else:
        ways = counts.copy() + [0]
        if k == ln:
            ans = 1
            for j in ways:
                if j:
                    ans *= j
                    ans %= mod
                else:
                    ans = 0
                    break
            print(ans)
        else:
            for i in range(k - 1):
                total = 0
                for j in range(ln - i - 1, -1, -1):
                    val = ways[j]
                    ways[j] = counts[j] * total
                    total += val
            print(sum(ways) % mod)
