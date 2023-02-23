from collections import deque


def change(src, dist):
    res = 0
    for idx in range(len(src)):
        x = ord(src[idx])
        y = ord(dist[idx])
        z = (y - x + 26) % 26
        res += min(z, 26 - z)
    return res


n = int(input())
s = input().strip()
m = int(input())
strings = [s]
for _ in range(m):
    strings.append(input().strip())
m += 1
counter = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(m):
        counter[i][j] = change(strings[i], strings[j])
q = 2 ** m
dp = [[-1] * m for i in range(q)]
dp[1][0] = 0
stack = deque([(1, 0)])
while stack:
    u, v = stack.popleft()
    for i in range(m):
        if not 1 << i & u:
            j = 1 << i ^ u
            if dp[j][i] == -1:
                stack.append((j, i))
                dp[j][i] = 1000000
            dp[j][i] = min(dp[j][i], counter[v][i] + dp[u][v])
ans = 1000000
q -= 1
for i in range(m):
    if dp[q][i] != -1:
        ans = min(ans, dp[q][i])
print(ans)
