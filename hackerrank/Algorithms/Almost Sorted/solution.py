#!/bin/python3


# Complete the almostSorted function below.
def almostSorted(arr):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("yes")
        return

    index = []
    for i in range(0, len(arr)):
        if sorted_arr[i] != arr[i]:
            index.append(i)

    if len(index) == 2:
        arr[index[0]], arr[index[1]] = arr[index[1]], arr[index[0]]
        if arr == sorted_arr:
            print("yes\nswap", index[0] + 1, index[1] + 1)
            return

    left = index[0]
    right = index[-1]
    arr[left:right + 1] = arr[right:left - 1:-1]
    if arr == sorted_arr:
        print("yes\nreverse", left + 1, right + 1)
        return

    print("no")
    return


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
