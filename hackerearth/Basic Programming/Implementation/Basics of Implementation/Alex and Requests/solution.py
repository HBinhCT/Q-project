n = int(input())
q = int(input())
requests = [0] * (n + 1)
for _ in range(q):
    x = int(input())
    for i in range(min(x, n), 0, -1):
        if requests[i] < x:
            requests[i] = x
            print('YES')
            break
    else:
        print('NO')
