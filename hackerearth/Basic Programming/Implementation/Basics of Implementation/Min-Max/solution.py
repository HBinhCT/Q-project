n = int(input())
arr = list(map(int, input().strip().split()))
nums = set(arr)
for i in range(min(nums), max(nums) + 1):
    if i not in nums:
        print('NO')
        break
else:
    print('YES')
