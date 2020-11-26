"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    min_1 = a[0]
    min_2 = a[1]
    max_1 = a[-1]
    max_2 = a[-2]
    ans = (max_1 - min_2 + max_2 - min_1) * 2 + math.ceil((min_2 - min_1 + max_1 - max_2) * math.sqrt(2))
    print(ans * m)
