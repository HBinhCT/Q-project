"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import accumulate

n, k = map(int, input().strip().split())
a = []
while len(a) < n:
    a += list(map(int, input().strip().split()))
size = max(a) + 1
primes = [False] * 2 + [True] * (size - 2)
i = 2
while i * i < size:
    if primes[i]:
        for j in range(i * i, size, i):
            primes[j] = False
    i += 1
counts = list(accumulate([0] + [int(primes[i]) for i in a]))
ans = 0
for i in range(1, n + 1):
    left = 0
    right = x = i - 1
    while left <= right:
        mid = (left + right) // 2
        if counts[i] - counts[mid] <= k:
            x = mid
            right = mid - 1
        else:
            left = mid + 1
    ans += i - x
print(ans)
