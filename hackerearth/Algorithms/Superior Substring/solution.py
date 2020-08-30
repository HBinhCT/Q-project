"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import defaultdict

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    if n <= 3:
        print(n)
    else:
        adj = defaultdict(list)
        for i in range(n):
            adj[ord(s[i]) - 97].append(i)  # 97 is ord('a')
        v = 3
        for u in adj.values():
            size = len(u)
            if 2 * size + 1 > v:
                for i in range(size):
                    u[i] -= 2 * i
                for i in range(size):
                    j = (v + 2 * i - 3) // 2 + 1
                    while j < size:
                        diff = u[j] - u[i]
                        if diff <= 2:
                            w = 2 * (j - i + 1) + 1
                            v = max(v, w)
                            j += 1
                        else:
                            j += diff - 2
        print(min(v, n))
