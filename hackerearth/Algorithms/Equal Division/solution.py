"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
teams = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    teams.append((a, b))
teams.reverse()
ans = 0
total = 0
for a, b in teams:
    a += total
    if a % b:
        total += b - a % b
print(total)
