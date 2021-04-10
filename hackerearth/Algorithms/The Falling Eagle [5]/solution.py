"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    drunk_quotient_vals = list(map(int, input().strip().split()))
    cost = 0
    for i in range(n - 1):
        cost += max(drunk_quotient_vals[i], drunk_quotient_vals[i + 1])
    print(cost)
