t = int(input())
vowels = ('a', 'e', 'i', 'o', 'u')
for _ in range(t):
    n = int(input())
    s = input().strip()
    compressed = s[0].upper()
    cnt = 0
    for i in range(1, n):
        c = s[i]
        if c in vowels:
            if cnt != 0:
                compressed += str(cnt)
                cnt = 0
            if compressed[-1] != c:
                compressed += c
        else:
            cnt += 1
    if cnt != 0:
        compressed += str(cnt)
    print(compressed)
