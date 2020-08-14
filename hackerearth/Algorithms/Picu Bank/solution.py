"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    d, a, m, b, x = map(int, input().strip().split())
    x -= d
    one_round = a * m + b
    total = x // one_round * (m + 1)
    ctr = x % one_round
    total += ctr // a + (ctr % a != 0)
    print(total)
