from collections import defaultdict

x = input().strip()
m = int(input())
queries = defaultdict(list)
for i in range(m):
    k, l = map(int, input().strip().split())
    queries[k - 1].append((l, i))
n = len(x)
left = []
right = list(range(n - 1, -1, -1))
ans = [''] * m
for k in range(n - 1, -1, -1):
    for l, i in queries[k]:
        ans[i] = x[left[l - 1]] if len(left) >= l else x[right[-l + len(left)]]
    while not left or right and x[left[-1]] >= x[right[-1]]:
        left.append(right.pop())
    left.pop()
print(''.join(ans))
