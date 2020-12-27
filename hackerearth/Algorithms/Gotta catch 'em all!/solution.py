"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
k = int(input())
days = sorted(map(int, input().strip().split()), reverse=True)
earliest = -1
for i in range(k):
    base = 1 + i
    evolve = base + days[i]
    earliest = max(earliest, evolve)
print(earliest + 1)
