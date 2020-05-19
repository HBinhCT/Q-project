from collections import deque

d = deque()
for _ in range(int(input())):
    methods = input().rstrip().split()
    getattr(d, methods[0])(*methods[1] if len(methods) > 1 else '')
print(*[item for item in d])
