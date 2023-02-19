def group(arr, size):
    dp = [1] * size
    for i in range(1, size):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


t = int(input())
for _ in range(t):
    n = int(input())
    terminators = []
    for _ in range(n):
        p1, p2 = map(int, input().strip().split())
        terminators.append((p1, p2))
    terminators.sort()
    print(max(group(terminators, n)))
