t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    t = input().strip()
    diffs = []
    cnt = 0
    for i in range(n):
        if s[i] != t[i]:
            cnt += 1
            if cnt > 3:
                print('NO')
                break
            diffs.append(i)
    else:
        if cnt <= 1:
            print('YES')
        elif 2 == cnt:
            uniq_chars = {s[diffs[0]], t[diffs[0]], s[diffs[1]], t[diffs[1]]}
            print('YES' if len(uniq_chars) in (2, 3) else 'NO')
        elif 3 == cnt:
            chars = [s[diffs[0]], t[diffs[0]], s[diffs[1]], t[diffs[1]], s[diffs[2]], t[diffs[2]]]
            uniq_chars = set(chars)
            m = len(uniq_chars)
            if m in (2, 4):
                print('YES')
            elif 3 == m:
                print('YES' if any(3 == chars.count(c) for c in uniq_chars) else 'NO')
            else:
                print('NO')
