t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    t = input().strip()
    for c in set(s).difference({'?'}):
        if c not in t:
            print('No')
            break
        if s.count(c) > t.count(c):
            print('No')
            break
    else:
        print('Yes')
