from collections import deque

n = int(input())
a = deque(input().strip().split())
b = deque(input().strip().split())
ans = 0
while a:
    i = a.index(b[0])
    ans += i + 1
    a.rotate(-i)
    a.popleft()
    b.popleft()
print(ans)
