def Max(N, K, arr):
    # Write your code here
    odd = even = 0
    separation = []
    for i in range(N - 1):
        if arr[i] % 2:
            odd += 1
        else:
            even += 1
        if odd == even:
            separation.append(abs(arr[i] - arr[i + 1]))
    separation.sort()
    total = i = 0
    length = min(K, len(separation))
    while i < length:
        if total + separation[i] <= K:
            total += separation[i]
            i += 1
        else:
            break
    return i


N = int(input())
K = int(input())
arr = list(map(int, input().split()))

out_ = Max(N, K, arr)
print(out_)
