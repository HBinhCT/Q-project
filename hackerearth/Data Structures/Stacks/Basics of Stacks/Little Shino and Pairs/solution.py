from collections import deque

n = int(input())
a = list(map(int, input().strip().split()))
count = 0
stack = deque([])
for i in a:
    while stack and stack[-1] < i:
        stack.pop()
        count += 1
    if stack:
        count += 1
    stack.append(i)
print(count)
