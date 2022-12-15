from sys import stdin


def sieve_eratosthenes(x):
    size = x + 1
    sieve = bytearray(b'\x01' * size)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, size, i):
                sieve[j] = 0
    return sieve


n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))
primes = sieve_eratosthenes(max(a))
mod = 1000000007
min_prime = mod
max_prime = 2
for i in a:
    if primes[i]:
        min_prime = min(min_prime, i)
        max_prime = max(max_prime, i)
print(max_prime - min_prime if min_prime != mod else -1)
