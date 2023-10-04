t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    xors = sorted(v ^ i for i, v in enumerate(a, start=1))
    pairs = count = 0
    for i in range(1, n):
        if xors[i] == xors[i - 1]:
            count += 1
            pairs += count
        else:
            count = 0
    print(pairs)
