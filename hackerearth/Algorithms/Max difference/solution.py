t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    if n <= 1:
        print(0)
        continue
    if n == 2:
        print(abs(a[0] - a[1]))
        continue
    maximum = max(a)
    minimum = min(a)
    diff = maximum - minimum
    a.remove(maximum)
    a.remove(minimum)
    diff += max(a) - min(a)
    print(diff)
