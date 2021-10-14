"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
s = input().strip()
ans = max(s)
idx = s.index(ans)
for i in range(ord(ans) - 1, ord('a') - 1, -1):
    try:
        idx = s.index(chr(i), idx + 1)
        ans += chr(i)
    except ValueError:
        pass
print(ans)
