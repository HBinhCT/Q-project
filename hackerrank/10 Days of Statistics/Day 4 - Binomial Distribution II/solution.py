def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


if __name__ == '__main__':
    defective, size = map(int, input().strip().split())
    print(f'{sum(binomial(size, i, defective / 100) for i in range(3)):.3f}')
    print(f'{sum(binomial(size, i, defective / 100) for i in range(2, size + 1)):.3f}')
