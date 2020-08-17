"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input()
    max_len = res = 0
    counter = Counter()
    for i in range(n):
        counter[s[i]] += 1
        max_len = max(max_len, counter[s[i]])
        if res - max_len < k:
            res += 1
        else:
            counter[s[i - res]] -= 1
    print(res)
