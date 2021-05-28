"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
for _ in range(n - 1):
    input()
statuses = ''.join(input().strip().split())
roads = list(map(len, statuses.split('1')))
ans = max(roads)
ans -= ans in (roads[0], roads[-1])
print(ans + 2)
