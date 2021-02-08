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
    p = input()
    f = input()
    ans = ''
    counter = Counter(list(f))
    for i in p:
        if i in counter.keys():
            ans += i * counter[i]
    print(ans)
