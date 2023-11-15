size = 100001
is_primes = [False, False] + [True] * (size - 2)
for i in range(2, int(size**0.5) + 1):
    if is_primes[i]:
        for j in range(i * i, size, i):
            is_primes[j] = False
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    x = a.count(1)
    y = sum(1 for i in a if is_primes[i])
    print(x * (x - 1) // 2 * y)
