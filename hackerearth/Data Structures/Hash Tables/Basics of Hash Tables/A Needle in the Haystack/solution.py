t = int(input())
for _ in range(t):
    pattern = input().strip()
    text = input().strip()
    if pattern in text or pattern[::-1] in text:
        print('YES')
    else:
        print('NO')
