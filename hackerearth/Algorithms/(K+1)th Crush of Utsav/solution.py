"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from sys import stdin


def check(x, arr):
    ln = len(arr)
    pos = 2 ** ln
    even = 0
    odd = 0
    for i in range(1, pos):
        dv = 1
        bt = 0
        for j in range(ln):
            if i & (2 ** j) != 0:
                dv *= a[j]
                bt += 1
        if bt % 2 == 0:
            even += x // dv
        else:
            odd += x // dv
    return odd - even


t = int(stdin.readline())
for _ in range(t):

    n, k = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().strip().split()))
    low = 0
    high = 10 ** 18
    while low < high - 1:
        mid = (low + high) // 2
        if check(mid, a) >= k:
            high = mid
        else:
            low = mid + 1
    if check(low, a) == k:
        print(low)
    else:
        print(high)
