from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    chocolates = list(map(int, input().strip().split()))
    k = int(input())
    counter = defaultdict(int)
    ways = 0
    for i in range(n):
        ways += counter[k - chocolates[i]]
        counter[chocolates[i]] += 1
    print(ways)
