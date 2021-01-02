"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
students = defaultdict(list)
for _ in range(n):
    name, scholar, mark = input().strip().split()
    students[int(mark)].append((name, int(scholar)))
for i in sorted(students.keys(), reverse=True):
    for j in sorted(students[i]):
        print(f'{j[0]} {j[1]} {i}')
