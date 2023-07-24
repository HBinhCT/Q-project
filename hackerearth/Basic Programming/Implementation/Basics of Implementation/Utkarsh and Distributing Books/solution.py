t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().strip().split()))
    print(min(b) - 1, sum(b) - n)
