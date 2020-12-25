"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
m = int(input())
b = list(map(int, input().split()))
max_b = max(b) + 1
ans = 0
for i in a:
    if i < max_b:
        ans += max_b - i
print(ans)
