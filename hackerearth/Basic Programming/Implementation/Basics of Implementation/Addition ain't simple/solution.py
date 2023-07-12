from string import ascii_lowercase

n = int(input())
for _ in range(n):
    s = input().strip()
    ln = len(s)
    pos = {c: i for i, c in enumerate(ascii_lowercase, start=1)}
    print(''.join(ascii_lowercase[(pos[s[i]] + pos[s[ln - 1 - i]] - 1) % 26] for i in range(ln)))
