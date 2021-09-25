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
    ans = 1
    c = Counter(s).values()
    for i in c:
        ans *= i
    print(ans % 1000000007)
