t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    count = max_len = 0
    for i in a:
        if i % 2:
            count = 0
        else:
            count += 1
            max_len = max(max_len, count)
    print(max_len if max_len else -1)
