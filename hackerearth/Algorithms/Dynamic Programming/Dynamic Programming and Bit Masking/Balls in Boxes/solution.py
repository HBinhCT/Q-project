from collections import defaultdict

size = 2 ** 10
n = int(input())
boxes = []
colored_balls = []
for _ in range(n):
    c, s = input().strip().split()
    boxes.append(int(c))
    colored_balls.append(s)
costs = defaultdict(lambda: float('inf'))
dp = [float('inf')] * size
dp[0] = 0
for i in range(n):
    j = int(colored_balls[i], 2)
    costs[j] = min(costs[j], boxes[i])
x = 0
min_amount = float('inf')
for i in range(size):
    for j in costs:
        k = i | j
        v = dp[k]
        dp[k] = min(dp[k], dp[i] + costs[j])
        if dp[k] != v and k >= x:
            min_amount = dp[k]
            x = k
print(min_amount)
