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
    s = input()
    counter = Counter(s)
    counter = sorted(counter.items(), key=lambda x: (x[-1], x[0]))
    ans = ''
    for k, v in counter:
        ans += k * v
    print(ans)
