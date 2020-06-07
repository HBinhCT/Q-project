def geometric_distribution(n, p):
    return ((1 - p) ** (n - 1)) * p


if __name__ == "__main__":
    num, din = map(int, input().strip().split())
    x = int(input())
    result = sum(geometric_distribution(i, num / din) for i in range(1, x + 1))
    print(f'{result:.3f}')
