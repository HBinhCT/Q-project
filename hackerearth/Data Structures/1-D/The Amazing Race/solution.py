t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().strip().split()))
    right = [0] * n
    left = [0] * n
    stack = []
    for i in range(n):
        while stack and h[stack[-1]] < h[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and h[stack[-1]] < h[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    winner = -1
    max_sight = -float('inf')
    for i in range(n):
        sight = ((right[i] - left[i] - 1) * (i + 1)) % 1000000007
        if max_sight < sight:
            winner = i + 1
            max_sight = sight
    print(winner)
