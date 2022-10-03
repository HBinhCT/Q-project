from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = input().strip()
    next_look = deque([i for i, v in enumerate(a) if v == '1'])
    pattern_len = 0
    while len(next_look) > 1 and pattern_len * len(next_look) < n:
        cur_look = next_look
        next_look = deque()
        is_found = False
        pattern_len += 1
        last = cur_look[-1] - n
        while cur_look:
            pos = cur_look.popleft()
            if pos - last < pattern_len:
                last = pos
                continue
            last = pos
            if a[(pos + pattern_len) % n] == '1':
                if not is_found:
                    is_found = True
                    next_look = deque()
                next_look.append(pos)
            elif not is_found:
                next_look.append(pos)
    if len(next_look) == 0:
        print(k - 1)
        continue
    if len(next_look) == 1:
        pattern_len = n
    print(min(next_look) + (k - 1) * pattern_len)
