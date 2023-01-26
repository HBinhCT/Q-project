def solve(N, A):
    # Write your code here
    A.sort()
    start = A[0]
    max_len = cnt = j = 1
    for i in range(1, N):
        diff = A[i] - start
        if diff <= 10:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            start = A[j]
            j += 1
    max_len = max(max_len, cnt)
    return max_len


N = int(input())
A = list(map(int, input().split()))

out_ = solve(N, A)
print(out_)
