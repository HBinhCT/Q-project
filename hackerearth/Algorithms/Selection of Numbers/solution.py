def solve(k, arr):
    # //Write code here
    dp = [0] * (k + 1)
    dp[0] = sum(arr[-k:])
    for i in range(1, k + 1):
        dp[i] = dp[i - 1] - arr[-k + i - 1] + arr[i - 1]
    return max(dp)


k, n = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

out_ = solve(k, arr)
print(out_)
