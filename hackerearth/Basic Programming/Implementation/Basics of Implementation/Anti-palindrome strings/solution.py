t = int(input())
for _ in range(t):
    s = input().strip()
    if s[::-1] == s:
        print(-1)
    else:
        print(''.join(sorted(s)))
