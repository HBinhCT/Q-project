from collections import deque

n = int(input())
heights = list(map(int, input().strip().split()))
stack = deque([])
max_stamina = stamina = 0
for i in reversed(heights):
    while stack and stack[-1] <= i:
        stamina = stamina ^ stack.pop()
    stack.append(i)
    stamina = stamina ^ i
    max_stamina = max(max_stamina, stamina)
print(max_stamina)
