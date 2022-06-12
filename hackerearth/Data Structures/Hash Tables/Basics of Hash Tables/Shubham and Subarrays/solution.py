n = int(input())
arr = list(map(int, input().strip().split()))
subarrays = set()
for i in range(n):
    visited = set()
    li = 0
    ri = 1
    for j in range(i, n):
        if arr[j] not in visited:
            visited.add(arr[j])
            li += arr[j]
            ri *= arr[j]
            ri %= 1000000007
            subarrays.add((li, ri))
print(len(subarrays))
