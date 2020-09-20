"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from functools import reduce
from itertools import combinations
from operator import mul


def count(arr, x):
    res = 0
    for num, sign in arr:
        if num > x:
            return res
        res += sign * (x // num)
    return res


t = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
divisor_list = []
n = len(primes)
for i in range(1, n + 1):
    for comb in combinations(primes, i):
        div = reduce(mul, comb, 1)
        if len(comb) % 2:
            divisor_list.append((div, 1))
        else:
            divisor_list.append((div, -1))
divisor_list.sort()
for _ in range(t):
    k = int(input())
    low = 2  # 2 = primes[0]
    high = 2 * k
    ans = low
    while low <= high:
        mid = (low + high) // 2
        c = count(divisor_list, mid)
        if c < k:
            low = mid + 1
        elif c > k:
            high = mid - 1
        else:
            high = mid - 1
            ans = mid
    print(ans)
