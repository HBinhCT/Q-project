n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
pre = [0]
for i in a:
    if i & i << 1:
        pre.append(pre[-1] + 1)
    else:
        pre.append(pre[-1])
for _ in range(q):
    l, r = map(int, input().strip().split())
    print(pre[r] - pre[l - 1])
