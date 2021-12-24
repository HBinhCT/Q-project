"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, x = map(int, input().strip().split())
    cards = list(map(int, input().strip().split()))
    total = abs(sum(cards))
    print(total // x + (total % x > 0))
