from sys import stdin
from bisect import bisect

cases = [1]
digits = 2
total = 2
while total < 1000000000000000:
    tmp = total + 2 * digits
    cases.append(tmp - 2)
    cases.append(tmp - 1)
    total += 2 ** digits * digits
    digits += 1
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(bisect(cases, n))
