"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s1, s2 = input().strip().split()
    ity = iter(s2)
    if all(c in ity for c in s1):
        print('Love you too')
    else:
        print('We are only friends')
