from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    choose = sorted((i * v for i, v in Counter(a).items() if i > 0), reverse=True)
    print(sum(choose[:k]))
