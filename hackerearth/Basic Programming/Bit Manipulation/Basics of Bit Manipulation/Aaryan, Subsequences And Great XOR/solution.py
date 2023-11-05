from functools import reduce
from operator import ior

n = int(input())
a = map(int, input().strip().split())
print(reduce(ior, a))
