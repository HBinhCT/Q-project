from math import log

c = int(input())
a = int(log(c, 2))
a = int(pow(2, a)) - 1
b = a ^ c
print(a * b)
