from collections import defaultdict


def solve(a):
    # Write your code here
    b = defaultdict(int)
    b[0] = 0
    for i in a:
        tmp = b.copy()
        for j in tmp:
            k = i ^ j
            b[k] = max(b[k], tmp[j] + 1)
    ans = 0
    for i in range(0, max(a) + 1):
        ans += b[i] * pow(31, i)
        ans %= 1000000007
    return ans


n = int(input())
a = list(map(int, input().split()))

out_ = solve(a)
print(out_)
