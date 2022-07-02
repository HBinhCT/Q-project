def find_id(idx=0, col=0):
    global c, s, ids
    if col == c:
        ids += s[idx]
    if s[idx + 2] != '.':
        find_id(idx + 2, col - 1)
    if s[idx + 3] != '.':
        find_id(idx + 3, col + 1)
    s = s[:idx + 1] + s[idx + 5:]


t = int(input())
for _ in range(t):
    c, s = input().strip().split()
    c = int(c)
    ids = ''
    find_id()
    print(''.join(sorted(ids)) if ids else 'Common Gandhijee!')
