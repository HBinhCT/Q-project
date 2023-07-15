n, l = map(int, input().strip().split())
ans = 0
for _ in range(n):
    s = input().strip()
    m = len(s) + 1
    for i in range(m):
        for j in range(i + 1, m):
            s1 = s[:i]
            s2 = s[i:j]
            s3 = s[j:]
            s4 = s1[::-1]
            s5 = s2[::-1]
            s6 = s3[::-1]
            if any(st == st[::-1] for st in (
                    s1 + s2 + s3,
                    s1 + s2 + s6,
                    s1 + s5 + s3,
                    s1 + s5 + s6,
                    s4 + s2 + s3,
                    s4 + s2 + s6,
                    s4 + s5 + s3,
            )):
                ans += 1
                break
        else:
            continue
        break
print(ans)
