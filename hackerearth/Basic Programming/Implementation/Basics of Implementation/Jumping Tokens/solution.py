t = int(input())
for _ in range(t):
    s = input().strip()
    if s in ('BRRRB', 'RBBBR'):
        print(3)
        continue
    count_r = count_b = 0
    adjacent_r = adjacent_b = False
    n = len(s)
    for i in range(len(s)):
        if 'R' == s[i]:
            count_r += 1
            if i and 'R' == s[i - 1]:
                adjacent_r = True
        elif 'B' == s[i]:
            count_b += 1
            if i and 'B' == s[i - 1]:
                adjacent_b = True
    if not count_r or not count_b or (not adjacent_r and not adjacent_b):
        print(n)
        continue
    if 1 == count_r:
        i = s.index('R')
        print(3 if i % 3 == (n - 1 - i) % 3 else 2)
        continue
    if 1 == count_b:
        i = s.index('B')
        print(3 if i % 3 == (n - 1 - i) % 3 else 2)
        continue
    print(2)
