def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


if __name__ == '__main__':
    boys, girls = map(float, input().strip().split())
    odds = boys / girls
    result = sum(binomial(6, i, odds / (1 + odds)) for i in range(3, 7))
    print(f'{result:.3f}')
