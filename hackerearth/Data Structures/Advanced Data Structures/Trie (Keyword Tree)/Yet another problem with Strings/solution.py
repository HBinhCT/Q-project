from sys import stdin


def get_deciphered(string, last_yes_decipher):
    res = ''
    for c in string:
        res += chr((ord(c) - 97 + last_yes_decipher) % 26 + 97)  # 97 = ord('a')
    return res


n, q = map(int, stdin.readline().strip().split())
strings = []
for _ in range(n):
    s = stdin.readline().strip()
    strings.append(s)
last_yes = 0
for idx in range(q):
    p, *query = stdin.readline().strip().split()
    if p == '1':
        t = query[0]
        if last_yes:
            t = get_deciphered(t, last_yes)
        for s in strings:
            if s in t:
                last_yes = idx
                print('YES')
                break
        else:
            print('NO')
    else:
        i, alpha = map(int, query)
        alpha = (alpha + last_yes) % 26
        strings[(i + last_yes) % n] += chr(alpha + 97)  # 97 = ord('a')
