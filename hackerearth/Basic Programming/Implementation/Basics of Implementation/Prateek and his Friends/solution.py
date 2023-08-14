t = int(input())
for _ in range(t):
    n, x = map(int, input().strip().split())
    costs = [int(input()) for _ in range(n)]
    j = 0
    total = costs[0]
    for i in range(1, n):
        while total > x:
            total -= costs[j]
            j += 1
        if total == x:
            print("YES")
            break
        total += costs[i]
    else:
        while total > x:
            total -= costs[j]
            j += 1
        print("YES" if total == x else "NO")
