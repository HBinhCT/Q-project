import math

maximum = float(input())
n = int(input())
mean = float(input()) * n
std = float(input()) * n ** .5
cdf = lambda x: .5 * (1 + math.erf((x - mean) / (std * (2 ** .5))))
print(f'{cdf(maximum):.4f}')
