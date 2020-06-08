from math import factorial, exp

mean = float(input())
k = int(input())
poisson_prob = ((mean ** k) * exp(-mean)) / factorial(k)
print(f'{poisson_prob:.3f}')
