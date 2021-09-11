#!/bin/python3


#
# Complete the whatsNext function below.
#
def whatsNext(arr):
    #
    # Write your code here.
    #
    # set bits are at each even index
    ln = len(arr) - 1
    # case: l == 0
    if not ln:
        if arr[0] == 1:
            print(2)
            print(*[1, 1])
        else:
            print(3)
            print(*[1, 1, arr[0] - 1])
        return
    # find index for least significant set bit
    i = ln - 1 if ln & 1 else ln
    # case: l == 1
    if ln == 1:
        c = [1, arr[1] + 1, arr[0] - 1]
    # case: last bit group is off
    elif ln != i:
        c = arr[:i - 1] + [arr[i - 1] - 1, 1, arr[-1] + 1, arr[i] - 1]
    # case: last bit group is set
    else:
        c = arr[:i - 1] + [arr[i - 1] - 1, 1, 1, arr[i] - 1]
    # handle zeros
    if not c[-1]:
        c.pop(-1)
    if c.count(0):
        indexes = []
        for i, v in enumerate(c):
            if not v:
                #  combine bits around zero
                c[i - 1] += c[i + 1]
                indexes.append(i)
        # remove zero and extra bits
        for i in indexes[-1:-1 - len(indexes):-1]:
            c.pop(i + 1)
            c.pop(i)
    print(len(c))
    print(*c)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        whatsNext(arr)
