"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input().strip()
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) not in (1, 25):
            print('NO')
            break
    else:
        print('YES')
