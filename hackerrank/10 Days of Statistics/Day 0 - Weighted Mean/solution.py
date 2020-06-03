N = int(input().strip())
X = list(map(int, input().strip().split()))
W = list(map(int, input().strip().split()))
print(f'{sum([a * b for a, b in zip(X, W)]) / sum(W):.1f}')
