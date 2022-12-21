from math import ceil


def sieve(size):
    is_primes = [False, False] + [True] * (size - 2)
    for i in range(2, int(size ** 0.5) + 1):
        if is_primes[i]:
            for j in range(i * i, size, i):
                is_primes[j] = False
    return is_primes


def prepare(size):
    is_primes = sieve(size)
    counter = [0] * size
    primes = []
    for i in range(1, size):
        counter[i] = counter[i - 1]
        if is_primes[i]:
            counter[i] = counter[i - 1] + 1
            primes.append(i)
        else:
            counter[i] = counter[i - 1]
    return primes, counter


def calc(x, size, primes, counter):
    i = 0
    count = 0
    while primes[i] < ceil(x ** 0.5):
        y = x // primes[i]
        count += counter[min(y, size - 1)] - counter[primes[i]]
        i += 1
    return count


t = int(input())
n = 1000001
ps, counts = prepare(1000001)
for _ in range(t):
    l, r = map(int, input().strip().split())
    print(calc(r, n, ps, counts) - calc(l - 1, n, ps, counts))
