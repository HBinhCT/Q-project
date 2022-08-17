t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    q = int(input())
    for _ in range(q):
        p, *query = list(map(int, input().strip().split()))
        if p == 1:
            i, val = query
            i -= 1
            a[i] = val
        else:
            l, r = [i - 1 for i in query]
            value = 0
            start = l
            end = r
            length = r - l + 1
            x = length
            j = length - 2
            for i in range(length // 2):
                value += a[start] * x + a[end] * x
                start += 1
                end -= 1
                x += j
                j -= 2
            if length % 2:
                value += a[start] * x
            print(value)
