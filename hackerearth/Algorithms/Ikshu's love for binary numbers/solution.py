from fractions import Fraction


def find_probability(i, j, h, w, dp=None):
    if dp is None:
        dp = [[-1] * (w + 1) for _ in range(h + 1)]
    if j >= w:
        return 2 ** (h - i)
    if i >= h:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = find_probability(i + 1, j + 1, h, w, dp) + find_probability(i + 1, 0, h, w, dp)
    return dp[i][j]


n, k = map(int, input().strip().split())
print(Fraction(find_probability(0, 0, n, k), 2 ** n))
