import math

mean, std = map(float, input().strip().split())
higher_grade = int(input())
pass_grade = int(input())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
print(f'{(1 - cdf(higher_grade)) * 100:.2f}')
print(f'{(1 - cdf(pass_grade)) * 100:.2f}')
print(f'{cdf(pass_grade) * 100:.2f}')
