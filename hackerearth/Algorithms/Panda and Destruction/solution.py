"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
destroying = {}
energy = 0
for _ in range(m):
    a, b = map(int, input().split())
    if a not in destroying:
        destroying[a] = None
        energy += 1
print(energy)
