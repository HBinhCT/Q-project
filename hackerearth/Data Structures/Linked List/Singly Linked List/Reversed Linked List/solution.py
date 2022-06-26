from collections import deque

n = int(input())
reverse_list = list(map(int, input().strip().split()))
original_list = []
stack = deque([])
for element in reverse_list:
    if element % 2:
        while stack:
            original_list.append(stack.pop())
        original_list.append(element)
    else:
        stack.append(element)
while stack:
    original_list.append(stack.pop())
print(*original_list)
