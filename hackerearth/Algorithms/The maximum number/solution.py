"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from math import gcd

t = int(input())
for _ in range(t):
    n, l = map(int, input().strip().split())
    a = map(int, input().strip().split())
    vls = [0] * 30  # l ≤ 30
    for i in a:
        bi = bin(i)[2:][::-1]
        for j in range(len(bi)):
            vls[j] += (bi[j] == '1')
    ans = []
    for i, vl in enumerate(vls):
        if vl:
            ans.append(2 ** i * vl)
    ans.sort(reverse=True)
    if len(ans) < l:
        print(-1)
    else:
        c = ans[l - 1]
        mm = ans.count(c)
        ind = ans.index(c)
        rem = l - ind
        p = 1
        k = 1
        rem = min(rem, mm - rem)
        while rem:
            p *= mm
            k *= rem
            m = gcd(p, k)
            p //= m
            k //= m
            mm -= 1
            rem -= 1
        print(p)
