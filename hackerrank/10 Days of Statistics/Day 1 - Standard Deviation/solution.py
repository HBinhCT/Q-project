n = int(input().strip())
X = list(map(int, input().strip().split()))
mean = sum(X) / n
variance = sum(((x - mean) ** 2) for x in X) / n
stddev = variance ** 0.5
print(f'{stddev:0.1f}')
