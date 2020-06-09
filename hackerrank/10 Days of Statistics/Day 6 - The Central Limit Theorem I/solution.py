import math

weight = float(input())
amount = int(input())
mean = float(input()) * amount
std = float(input()) * amount ** .5
cdf = lambda x: .5 * (1 + math.erf((x - mean) / (std * (2 ** .5))))
print(f'{cdf(weight):.4f}')
