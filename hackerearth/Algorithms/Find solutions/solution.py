"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict

n = int(input())
a = []
for _ in range(n):
    line = input()
    try:
        a.append(int(line))
    except:
        a = list(map(int, line.strip().split()))
        break
counting = defaultdict(int)
for i in range(n):
    if a[i]:
        for j in range(n):
            for k in range(n):
                val = a[i] * (a[j] + a[k])  # RHS(s(t+u))
                counting[val] += 1
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            val = a[i] * a[j] + a[k]  # LHS(p*q+r)
            if val in counting:  # p*q+r=s(t+u)
                ans += counting[val]
print(ans)
