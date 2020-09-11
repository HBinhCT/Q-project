"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import math

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().strip().split())
    if a < b:
        a, b = b, a
    if a % b == 0:
        print(n * b)
    else:
        lcm = a * b // math.gcd(a, b)
        no_terms_lcm = lcm // a + lcm // b - 1
        ratio = a / b
        q, r = divmod(n, no_terms_lcm)
        num_1 = r // (ratio + 1)
        num_2 = (r + 1) // (ratio + 1)
        if num_2 > num_1:
            print(int(lcm * q + a * num_2))
        else:
            print(int(lcm * q + b * (r - num_2)))
