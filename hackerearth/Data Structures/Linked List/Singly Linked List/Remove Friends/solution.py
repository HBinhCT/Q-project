from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    popularity_friends = map(int, input().strip().split())
    stack = deque([])
    for popularity in popularity_friends:
        while k and stack and stack[-1] < popularity:
            stack.pop()
            k -= 1
        stack.append(popularity)
    print(' '.join(map(str, stack)))
