import statistics

n = int(input())
x = tuple(map(float, input().split()))
y = tuple(map(float, input().split()))
rho = sum(a * b for a, b in zip([i - statistics.mean(x) for i in x], [i - statistics.mean(y) for i in y])) / (
            n * statistics.pstdev(x) * statistics.pstdev(y))
print(f'{rho:.3f}')
