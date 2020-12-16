"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
velocity = list(map(int, input().strip().split()))
pos = list(map(int, input().strip().split()))


def merge(arr, temp, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for x in range(left, right + 1):
        arr[x] = temp[x]
    return count


def _merge_sort(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count = _merge_sort(arr, temp, left, mid)
        count += _merge_sort(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid, right)
    return count


def merge_sort(arr, ln):
    temp = [0] * ln
    return _merge_sort(arr, temp, 0, ln - 1)


res = [0] * n
for ind, val in enumerate(pos):
    res[val - 1] = velocity[ind]
print(merge_sort(res, n))
