from functools import reduce
from operator import mul
from math import gcd

n = int(input())
a = list(map(int, input().strip().split()))
gx = reduce(gcd, a)
fx = reduce(mul, a)
print(fx ** gx % 1000000007)
