from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    s = int(input())
    for i in range(n):
        for c in combinations(a, i + 1):
            if s == sum(c):
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")
