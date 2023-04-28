n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
mid = ((n - k + 1) // 2) - 1
print(max(a[mid:mid + k + 1]))
