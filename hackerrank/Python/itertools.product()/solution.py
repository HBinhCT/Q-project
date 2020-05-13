from itertools import product

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(*product(a, b))
