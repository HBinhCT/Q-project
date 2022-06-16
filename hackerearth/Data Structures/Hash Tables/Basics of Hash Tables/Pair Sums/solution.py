n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
term = set()
for i in a:
    if i not in term:
        term.add(k - i)
    else:
        print('YES')
        break
else:
    print('NO')
