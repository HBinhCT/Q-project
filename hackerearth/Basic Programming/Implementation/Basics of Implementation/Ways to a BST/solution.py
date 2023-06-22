mod = 1000000007
size = 1024
dp = [[0] * size for _ in range(size)]
for i in range(size):
    dp[i][0] = dp[i][i] = 1
    for j in range(1, i):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod


def permutation(a):
    if len(a) > 1:
        left = []
        right = []
        for x in range(1, len(a)):
            if a[x] < a[0]:
                left.append(a[x])
            else:
                right.append(a[x])
        return dp[len(a) - 1][len(left)] * permutation(left) * permutation(right) % mod
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(permutation(arr))
