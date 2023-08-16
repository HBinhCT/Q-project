t = int(input())
for _ in range(t):
    m = int(input())
    total = 0
    for _ in range(m):
        length, d = map(int, input().strip().split())
        total += length * d
    if not total:
        print(0)
    else:
        total %= 9
        print(total if total else 9)
