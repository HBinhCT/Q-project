n, m = map(int, input().strip().split())
prices = [int(input()) for _ in range(n)]
print(sum(prices[:m]) + min(prices[m:]) - 1)
