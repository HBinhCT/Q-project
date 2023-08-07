t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    count = 0
    for i in range(n):
        if 'B' == s[i]:
            for j in (i - 2, i - 1, i + 1, i + 2):
                if 0 <= j < n and 'W' == s[j]:
                    s[j] = '_'
                    count += 1
    print(count)
