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
    n = len(s)
    if s == 'R':
        print(0)
    elif s.count('K') == n:
        print(n)
    elif s.count('R') == n:
        print(n - 1)
    else:
        prev = res = 0
        cnt = s.count('R')
        for i in range(n):
            if s[i] == 'K':
                prev += 1
            else:
                if prev > 0:
                    prev -= 1
            res = max(res, prev)
        print(cnt + res)
