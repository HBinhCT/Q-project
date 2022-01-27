"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
left = a[::]
right = a[::-1]
for i in range(1, n):
    left[i] += left[i - 1] // 2
    right[i] += right[i - 1] // 2
right.reverse()
print(max(left[i] + right[i] - a[i] for i in range(n)))
