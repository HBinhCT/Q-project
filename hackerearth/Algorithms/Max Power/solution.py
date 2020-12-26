"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    low = min(a)
    high = max(a)
    if n > 2 and high == a[0] and low == a[-1]:
        print(max(high - min(a[1:-1]), max(a[1:-1]) - low))
    else:
        print(high - low)
