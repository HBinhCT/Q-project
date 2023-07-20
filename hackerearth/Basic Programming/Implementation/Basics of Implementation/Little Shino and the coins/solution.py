k = int(input())
s = input().strip()
n = len(s)
m = n + 1
dp = [m] * 26
x = cnt = ans = 0
for i in range(n):
    j = ord(s[i]) - 97  # ord('a') = 97
    if dp[j] == m:
        if cnt < k:
            cnt += 1
        else:
            y = min(dp)
            z = dp.index(y)
            dp[z] = m
            x = y + 1
    dp[j] = i
    if cnt == k:
        y = min(dp)
        ans += y - x + 1
print(ans)
