"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    frequency_tasks = defaultdict(int)
    for i in range(n):
        task = input()
        frequency_tasks[task] += 1
    res = sorted(zip(frequency_tasks.values(), frequency_tasks.keys()))
    for i, j in res:
        print(i, j)
