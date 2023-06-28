n = int(input())
i, j, p = map(int, input().strip().split())
for x in range(n):
    row = ''
    for y in range(n):
        impact = max(abs(j - y), abs(i - x))
        if p - impact <= 0:
            row += '0 '
        else:
            row += (str(p - impact) + ' ')
    print(row[:-1])
