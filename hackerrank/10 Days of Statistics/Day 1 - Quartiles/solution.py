from statistics import median

n = int(input())
x = sorted(map(int, input().strip().split()))
print(int(median(x[:n // 2])))
print(int(median(x)))
print(int(median(x[(n + 1) // 2:])))
