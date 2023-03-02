n = int(input())
grids = input().strip()
if 'HH' in grids:
    print('NO')
else:
    print('YES')
    print(grids.replace('.', 'B'))
