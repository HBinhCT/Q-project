from collections import defaultdict, deque

n = int(input())
arr = list(map(int, input().strip().split()))
pairs = defaultdict(int)
stack = deque([])
for i, v in enumerate(arr):
    while stack and v > arr[stack[-1]]:
        j = stack.pop()
        diff = i - j
        cnt = j - (stack[-1] if stack else -1)
        pairs[diff] = max(pairs[diff], cnt)
    stack.append(i)
print(sum(pairs.values()))
