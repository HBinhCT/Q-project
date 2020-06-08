import math

mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
# Less than 19.5
print(f'{cdf(19.5):.3f}')
# Between 20 and 22
print(f'{cdf(22) - cdf(20):.3f}')
