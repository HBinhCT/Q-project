"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m, g = map(int, input().strip().split())
t = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
max_diff = -float('inf')
for i in range(1, n):
    max_diff = max(t[i] - t[i - 1], max_diff)
count = sum(list(map(lambda x: x <= max_diff, a)))
print(count)
