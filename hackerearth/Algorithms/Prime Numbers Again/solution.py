"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from functools import lru_cache
from math import sqrt


@lru_cache(maxsize=None)
def is_prime(x, power=False):
    for i in range(2, int(sqrt(x)) + 1):
        if not x % i:
            return x == i ** i if power else False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2 or n == 4 or is_prime(n) or is_prime(n, True):
        print(1)
    elif not n % 2 or is_prime(n - 2, True) or is_prime(n - 4, True) or is_prime(n - 2) or is_prime(n - 4):
        print(2)
    else:
        print(3)
