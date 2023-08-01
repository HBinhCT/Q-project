from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    pieces = []
    counter = deque([])
    for _ in range(n):
        bar = input().strip()
        pieces.append(bar)
        cnt = bar.count('#')
        counter.append(cnt)
        total += cnt
    if total % 2:
        print('NO')
    else:
        half = total // 2
        cnt = 0
        for i in range(n):
            cnt += counter.popleft()
            if cnt == half:
                print('YES')
                break
        else:
            tran_pieces = tuple(zip(*pieces))
            cnt = 0
            for i in range(n):
                cnt += tran_pieces[i].count('#')
                if cnt == half:
                    print('YES')
                    break
            else:
                print('NO')
