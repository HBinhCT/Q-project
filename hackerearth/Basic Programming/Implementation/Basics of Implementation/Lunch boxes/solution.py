t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = sorted(map(int, input().strip().split()))
    count = total = 0
    for i in a:
        total += i
        if total > n:
            break
        count += 1
    print(count)
