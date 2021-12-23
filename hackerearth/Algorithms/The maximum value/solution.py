"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate

t = int(input())
arr = []
for _ in range(t):
    n = int(input())
    arr.append(n)
size = max(arr) + 1
primes = [0] * 2 + [1] * (size - 2)
i = 2
while i * i < size:
    if primes[i]:
        for j in range(i * i, size, i):
            primes[j] = 0
    i += 1
counts = list(accumulate(primes))
for n in arr:
    print(counts[n])
