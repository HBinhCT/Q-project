"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import bisect

n = int(input())
a = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    if line[0] == 1:
        bisect.insort_left(a, line[1])
    else:
        ln = len(a)
        if ln < 3:
            print('Not enough enemies')
        else:
            print(a[-(ln // 3)])
