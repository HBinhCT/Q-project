t = int(input())
for _ in range(t):
    text = input().strip()
    pattern = input().strip()
    print('YES' if set(text).intersection(set(pattern)) else 'NO')
