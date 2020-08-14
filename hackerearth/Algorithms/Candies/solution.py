"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

s = input()
t = int(input())
size = len(s)


def check(x, n):
    hashing = defaultdict(lambda: 0)
    count = 0
    for i in range(size):
        c = s[i]
        hashing[c] += 1
        if hashing[c] % 2 == 0:
            count += 1
        if i >= x:
            c = s[i - x]
            hashing[c] -= 1
            if hashing[c] % 2 != 0:
                count -= 1
        if count >= n // 2:
            return True
    return False


for _ in range(t):
    k = int(input())
    low = k
    high = size
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if check(mid, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
