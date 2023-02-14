t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().strip().split()))
    answer = [0] * n
    position = [0] * (n + 1)
    for i in range(n):
        position[p[i]] = i
    minimum = maximum = position[0]
    for i in range(1, n):
        if position[i] < minimum:
            count = (minimum - position[i]) * (n - maximum)
        elif maximum < position[i]:
            count = (minimum + 1) * (position[i] - maximum)
        else:
            count = 0
        answer[i - 1] = count
        minimum = min(minimum, position[i])
        maximum = max(maximum, position[i])
    answer[n - 1] = 1
    print(*answer)
