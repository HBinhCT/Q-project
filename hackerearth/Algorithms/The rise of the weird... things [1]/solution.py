"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
powers = map(int, input().strip().split())
even = []
odd = []
for i in powers:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
even.sort()
odd.sort()
print(*even, sum(even), *odd, sum(odd))
