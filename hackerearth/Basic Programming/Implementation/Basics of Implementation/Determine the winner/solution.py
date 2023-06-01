t = int(input())
for _ in range(t):
    s = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    f = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    f_score = c_score = 0
    for i in range(4):
        f_score += max(s[i] // 2, s[i] - f[i] * d[i])
        c_score += max(s[i] // 2, s[i] - c[i] * d[i])
    if f_score != c_score:
        print('Flash' if f_score > c_score else 'Cisco')
    else:
        f_max = max(f)
        c_max = max(c)
        if f_max != c_max:
            print('Flash' if f_max < c_max else 'Cisco')
        else:
            print('Tie')
