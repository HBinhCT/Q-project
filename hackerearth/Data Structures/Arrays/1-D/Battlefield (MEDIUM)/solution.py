t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    total_knights = s.count('K')
    group = s[:total_knights].count('K')
    mx = group
    for i in range(1, n):
        if s[i - 1] == 'K':
            group -= 1
        if s[(i + total_knights - 1) % n] == 'K':
            group += 1
        mx = max(mx, group)
    print(total_knights - mx)
