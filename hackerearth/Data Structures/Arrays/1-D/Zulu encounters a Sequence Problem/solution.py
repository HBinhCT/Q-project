test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int, input().strip().split()))
    max_point = i = 0
    while i < n - 1:
        cur = a[i]
        while i < n - 1 and a[i] <= a[i + 1]:
            i += 1
        max_point = max(max_point, abs(cur - a[i]))
        cur = a[i]
        while i < n - 1 and a[i] >= a[i + 1]:
            i += 1
        max_point = max(max_point, abs(cur - a[i]))
    print(max_point)
