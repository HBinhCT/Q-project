def inversion(arr):
    ln = len(arr)
    if ln == 1:
        return 0
    mid = ln // 2
    remain = ln - mid
    left_part = arr[:mid]
    right_part = arr[mid:]
    count = inversion(left_part) + inversion(right_part)
    j = k = 0
    for i in range(ln):
        if j < mid and (k >= remain or left_part[j] <= right_part[k]):
            arr[i] = left_part[j]
            count += k
            j += 1
        elif k < remain:
            arr[i] = right_part[k]
            k += 1
    return count


def inversions(arr):
    nums = tuple(arr)
    ln = len(nums)
    count = inversion(arr)
    idxes = {arr[i]: i for i in range(len(arr))}
    counts = [count]
    for i in range(len(arr)):
        val = (counts[i] - idxes[nums[i]]) + (ln - 1 - idxes[nums[i]])
        counts.append(val)
    return counts[1:]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(' '.join(map(str, inversions(a))))
