t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    s = []
    for _ in range(n):
        s.append(list(map(int, input().strip().split())))
    u = min(map(min, s))
    v = max(map(max, s))
    unsafe_row = [False] * n
    unsafe_col = [False] * m
    for x, row in enumerate(s):
        for y, element in enumerate(row):
            if element == u or element == v:
                unsafe_row[x] = True
                unsafe_col[y] = True
    print((n - sum(unsafe_row)) * (m - sum(unsafe_col)))
