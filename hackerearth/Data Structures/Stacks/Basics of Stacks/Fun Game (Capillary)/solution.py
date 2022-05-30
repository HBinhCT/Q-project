def funGame(arr):
    # Write your code here
    ln = len(arr)
    i = 0
    j = ln - 1
    res = ''
    while i != ln and j != -1:
        if arr[i] > arr[j]:
            res += '1'
            j -= 1
        elif arr[i] < arr[j]:
            res += '2'
            i += 1
        else:
            res += '0'
            j -= 1
            i += 1
    return res


n = int(input())
arr = list(map(int, input().strip().split()))

out_ = funGame(arr)
print(' '.join(out_))
