def swap(arr, ln):
    def merge_sort(left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += merge_sort(left, mid)
            count += merge_sort(mid + 1, right)
            count += merge(left, mid, right)
        return count

    def merge(left, mid, right):
        x = z = left
        y = mid + 1
        count = 0
        while x <= mid and y <= right:
            if arr[x] <= arr[y]:
                temp[z] = arr[x]
                z += 1
                x += 1
            else:
                temp[z] = arr[y]
                count += mid - x + 1
                z += 1
                y += 1
        while x <= mid:
            temp[z] = arr[x]
            z += 1
            x += 1
        while y <= right:
            temp[z] = arr[y]
            z += 1
            y += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return count

    temp = [0] * ln
    return merge_sort(0, ln - 1)


n = int(input())
p = [0] + list(map(int, input().strip().split()))
minimum = float('inf')
maximum = float('-inf')
j = k = 0
for i in range(1, n + 1):
    if p[i] - i < minimum:
        minimum = p[i] - i
        j = i
    if p[i] - i > maximum:
        maximum = p[i] - i
        k = i
p[j], p[k] = p[k], p[j]
print(swap(p[1:], n))
