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
    s = sorted(map(int, input().split()))
    k = int(input())
    result = sum(s[:k])
    result += s[k - 1] * (n - k)
    print(result)
