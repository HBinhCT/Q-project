T = int(input())
for _ in range(T):
    n, is_prime = int(input()), True
    if n <= 1 or (n > 3 and (n % 2 == 0 or n % 3 == 0)):
        is_prime = False
    else:
        # All primes greater than 3 are of the form 6k ± 1 (k is integer)
        for x in range(5, int(n ** .5) + 1, 6):
            if n % x == 0 or n % (x + 2) == 0:
                is_prime = False
                break
    print('Prime' if is_prime else 'Not prime')
