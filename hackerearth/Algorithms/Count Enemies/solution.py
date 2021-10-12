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
    groups = s.split('*')
    ans = 0
    for group in groups:
        count = group.count('O')
        if count == len(group):
            ans += count
    print(ans)
