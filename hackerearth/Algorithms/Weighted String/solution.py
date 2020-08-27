"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque

t = int(input())
for _ in range(t):
    k = int(input())
    s = input()
    cache = deque()
    ans = 0
    cur = 0
    for i in s:
        cache.append(i)
        cur += (ord(i) - 97) + 1  # 97 = ord('a')
        if cur == k:
            ans += 1
            continue
        elif cur < k:
            continue
        else:
            while cur > k:
                c = cache.popleft()
                cur -= (ord(c) - 97) + 1
                if cur == k:
                    ans += 1
    print(ans)
