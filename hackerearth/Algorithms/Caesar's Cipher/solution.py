"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
k = int(input())
for _ in range(k):
    s = input().strip()
    t = input().strip()
    k = (ord(t[0]) - ord(s[0]) + 26) % 26
    for i in range(1, len(s)):
        if (ord(t[i]) - ord(s[i]) + 26) % 26 != k:
            print(-1)
            break
    else:
        print(k)
