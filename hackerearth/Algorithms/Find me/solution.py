"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().strip().split())
numbers = sorted(map(int, input().strip().split()))
for _ in range(q):
    k = int(input())
    print(numbers.pop(k - 1))
