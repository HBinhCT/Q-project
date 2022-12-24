def least_prime_factors(m):
    f = [0] * m
    f[1] = 1
    for i in range(2, m):
        if f[i] == 0:
            f[i] = i
            for j in range(i * i, m, i):
                if f[j] == 0:
                    f[j] = i
    return f


t = int(input())
nums = []
size = 0
for _ in range(t):
    n = int(input())
    nums.append(n)
    size = max(size, n)
least_primes = least_prime_factors(size + 1)
for n in nums:
    factors = []
    x = n
    while x != 1:
        factor = least_primes[x]
        factors.append(factor)
        x //= factor
    divisors = {1}
    for i in factors:
        divisors |= set(j * i for j in divisors)
    total = temp = 0
    for i in divisors:
        total += i * temp
        temp += i
    print(total)
