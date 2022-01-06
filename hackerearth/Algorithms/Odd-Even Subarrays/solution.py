"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
odd_even = [1 if i & 1 else -1 for i in a]
diff = defaultdict(int)
diff[0] = 1
curr = 0
for i in odd_even:
    curr += i
    diff[curr] += 1
total = 0
for i in diff.values():
    total += i * (i - 1) // 2
print(total)
