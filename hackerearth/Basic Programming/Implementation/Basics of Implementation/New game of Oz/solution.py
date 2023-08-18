from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    arr = deque(sorted(map(int, input().strip().split())))
    turns = i = 0
    while arr:
        x = arr.popleft() + 1
        turns += 1
        if arr and x == arr[0]:
            arr.popleft()
    print(turns)
