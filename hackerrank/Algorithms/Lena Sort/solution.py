#!/bin/python3

mns = [0, 0]
for i in range(2, 100001):
    mns.append(i - 1 + mns[i // 2] + mns[(i - 1) // 2])


def lena(length, comparisons):
    def mxs(x):
        return x * (x - 1) // 2

    if not mns[length] <= comparisons <= mxs(length):
        return -1
    result = [-1] * length
    stk = [(length, comparisons, 0, 1)]
    while stk:
        length, comparisons, ofs, ofs2 = stk.pop()
        while length:
            comparisons -= length - 1
            for i in range(length):
                if mns[i] + mns[length - 1 - i] <= comparisons <= mxs(i) + mxs(length - 1 - i):
                    c1 = min(max(comparisons, max(mns[i], comparisons - mxs(length - 1 - i))),
                             min(mxs(i), comparisons - mns[length - 1 - i]))
                    result[ofs] = i + ofs2
                    if i:
                        stk.append((i, c1, ofs + 1, ofs2))
                    length, comparisons, ofs, ofs2 = length - i - 1, comparisons - c1, ofs + i + 1, ofs2 + i + 1
                    break
    return result


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        lc = input().split()

        l = int(lc[0])

        c = int(lc[1])

        # Write Your Code Here
        res = lena(l, c)
        print(' '.join(map(str, res)) if res != -1 else -1)
