"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
s = input()
t = input()
ans = 0
last = 0
for i in range(n):
    x = s[i] != t[i]
    ans += last == 0 and x
    last = x
print(ans)
