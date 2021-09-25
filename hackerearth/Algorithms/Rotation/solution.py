"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
s = list(input().strip())
t = list(input().strip())
ans = 0
while s != t:
    s.pop(0)
    t.pop(-1)
    ans += 1
print(ans)
