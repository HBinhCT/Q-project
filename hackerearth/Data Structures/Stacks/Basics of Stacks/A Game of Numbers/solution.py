from collections import deque

n = int(input())
a = [int(input()) for _ in range(n)]
fx = [-1] * n
gx = [-1] * n
stack = deque([0])
for i in range(1, n):
    while stack and a[stack[-1]] < a[i]:
        fx[stack.pop()] = i
    stack.append(i)
stack = deque([0])
for i in range(1, n):
    while stack and a[stack[-1]] > a[i]:
        gx[stack.pop()] = i
    stack.append(i)
print(*(a[gx[i]] if (i != -1 and gx[i] != -1) else -1 for i in fx))
