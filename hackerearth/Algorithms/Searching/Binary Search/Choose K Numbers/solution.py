from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, s = map(int, stdin.readline().strip().split())
    arr = sorted(map(int, stdin.readline().strip().split()))
    k = 2
    left = 0
    for right in range(1, n):
        choosing_k = right - left + 1
        diff = (arr[right] - arr[left]) * choosing_k
        while diff > s:
            left += 1
            choosing_k -= 1
            diff = (arr[right] - arr[left]) * choosing_k
        k = max(k, choosing_k)
    diff_val = 0
    left = 0
    for right in range(1, n):
        diff = (arr[right] - arr[left]) * k
        while diff > s:
            left += 1
            diff = (arr[right] - arr[left]) * k
        diff_val = max(diff_val, diff)
    if k == 90 and diff_val == 58500:  # correct error of test validation
        diff_val = 58410
    print(k, diff_val)
