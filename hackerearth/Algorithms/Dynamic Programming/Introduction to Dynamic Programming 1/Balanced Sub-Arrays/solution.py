t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().strip().split()))
    for i in range(n):
        a[i + 1] = a[i + 1] & 0x01 ^ a[i]
    counter = [0, 0]
    count = 0
    for i in range(n + 1):
        count += counter[a[i]]
        counter[a[i]] += 1
    tmp = 0
    for i in range(1, n + 1):
        x = a[i] - a[i - 1]
        if x:
            tmp += 1
        else:
            tmp = 0
        count += (tmp + 1) // 2 - tmp // 2
    print(count)
