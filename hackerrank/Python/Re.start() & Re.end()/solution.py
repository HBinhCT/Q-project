import re

S = input().strip()
k = input().strip()
assert 0 < len(S) < 100
assert 0 < len(k) < len(S)
pattern = re.compile(k)
r = pattern.search(S)
if not r:
    print('(-1, -1)')
while r:
    print(f'({r.start()}, {r.end() - 1})')
    r = pattern.search(S, r.start() + 1)
