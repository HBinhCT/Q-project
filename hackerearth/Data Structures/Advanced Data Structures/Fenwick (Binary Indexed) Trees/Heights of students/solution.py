from bisect import bisect


def func1(Height):
    # Write your code here
    def update(array, length, index, value):
        while index <= length:
            array[index] += value
            index += index & -index

    def convert(array):
        temp = sorted(array)
        length = len(array)
        for x in range(length):
            y = bisect(temp, array[x])
            while y > 0 and temp[y - 1] == array[x]:
                y -= 1
            array[x] = min(y + 1, length)

    def get_total(array, index):
        res = 0
        while index > 0:
            res += array[index]
            index -= index & -index
        return res

    def get_totals(elements):
        arr = elements.copy()
        length = len(arr)
        convert(arr)
        tree = [0] * (length + 1)
        totals = [0] * length
        for x in range(length - 1, -1, -1):
            totals[x] = get_total(tree, arr[x] - 1)
            update(tree, length, arr[x], 1)
        return totals

    n = len(Height)
    dp = get_totals(Height)
    total = sum(dp)
    arranged = sorted(Height)
    ans = float('inf')
    for i in range(n):
        happiness = total - dp[i]
        j = bisect(arranged, Height[i])
        happiness += n - j
        ans = min(ans, happiness)
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    Height = list(map(int, input().strip().split()))

    out_ = func1(Height)
    print(out_)
