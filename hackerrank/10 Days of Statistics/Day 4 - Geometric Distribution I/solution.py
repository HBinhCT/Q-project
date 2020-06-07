def geometric_distribution(n, p):
    return ((1 - p) ** (n - 1)) * p


if __name__ == "__main__":
    num, din = map(int, input().strip().split())
    x = int(input())
    result = geometric_distribution(x, num / din)
    print(f'{result:.3f}')
