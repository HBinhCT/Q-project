"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    trees = defaultdict(list)
    n = int(input())
    for _ in range(n - 1):
        a, b, c = map(int, input().strip().split())
        trees[a].append((b, c))
    queue = deque([(1, 0)])
    count = 0
    while queue:
        cur_node, xor_value = queue.popleft()
        if not len(trees[cur_node]) and xor_value % 2:
            count += 1
        for node, weight in trees[cur_node]:
            queue.append((node, weight ^ xor_value))
    print(count)
