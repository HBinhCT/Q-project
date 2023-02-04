def Memory(N, A, B, C):
    # Write your code here
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in (A, B, C):
            k = i - j
            if k >= 0 and dp[k] != -1:
                dp[i] = max(dp[i], dp[k] + 1)
    return dp[N]


N = int(input())
A = int(input())
B = int(input())
C = int(input())

out_ = Memory(N, A, B, C)
print(out_)
