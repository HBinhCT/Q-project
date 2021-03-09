"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

t = int(input())
caching = []
max_num = 1001
for i in range(max_num):
    kit = set()
    for j in range(max_num):
        if (i | j) - (i & j) == i - j:
            kit.add(j)
    caching.append(kit)
for _ in range(t):
    n = int(input())
    a = map(int, input().strip().split())
    cnt = Counter(a)
    ans = 0
    for k, x in cnt.items():
        ans += sum(x * cnt[y] for y in caching[k])
    print(ans)
