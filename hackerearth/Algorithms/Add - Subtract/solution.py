"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
op = lambda x: x * 3 if x > 0 else x * -5
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = sorted(map(int, input().strip().split()))
    print(min(sum(sorted(map(op, (i - j for j in a)))[:k]) for i in a))
