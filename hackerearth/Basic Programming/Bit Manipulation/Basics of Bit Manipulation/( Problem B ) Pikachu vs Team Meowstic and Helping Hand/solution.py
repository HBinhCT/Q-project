def helping_hand(arr):
    ln = len(arr)
    res = [arr[0]] * ln
    for x in range(1, ln):
        res[x] = arr[x - 1] | arr[x]
    return res


n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
for i in range(k):
    b = helping_hand(a)
    if b != a:
        a = b
    else:
        break
print(*a)
