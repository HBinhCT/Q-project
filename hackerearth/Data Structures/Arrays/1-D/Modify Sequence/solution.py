n = input()
a = list(map(int, input().strip().split()))
diff = 0
for i in a:
    if i - diff < 0:
        print('NO')
        break
    else:
        diff = i - diff
else:
    print('NO' if diff else 'YES')
