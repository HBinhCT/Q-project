"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
ans = ''
for i in range(len(s)):
    ans += s[i].upper() if not i or s[i - 1] == ' ' else s[i]
print(ans)
