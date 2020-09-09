def solve(arr):
    from collections import Counter

    def smallest_set(start, end, counter):
        d = {start - 1: []}
        for i in range(start, end + 1):
            d[i] = []
            prev_len = len(d[i - 1])
            new_lists = counter[i] - prev_len
            if new_lists > 0:
                d[i] = [1] * new_lists
            if prev_len > 0:
                num_appends = min(prev_len, new_lists + prev_len)
                d[i - 1].sort()
                d[i] += [j + 1 for j in d[i - 1][:num_appends]]
                d[i - 1] = d[i - 1][num_appends:]
        ans = d[end][0]
        for i in range(start, end + 1):
            if len(d[i]) > 0:
                ans = min(ans, min(d[i]))
                if ans == 1:
                    return 1
        return ans

    def find_lowest_range(a, start):
        counter = Counter(a)
        i = 0
        res = start
        while i < len(a):
            end = i
            while end < start and (a[i] == a[end] or (a[end] - a[end - 1]) <= 1):
                end += 1
            end -= 1
            if end == i:
                return 1
            res = min(res, smallest_set(a[i], a[end], counter))
            if res == 1:
                return 1
            i = end + 1
        return res

    if arr[0] == 0:  # For some weird reason 0 is a value
        return 0
    first = arr[0]
    new_arr = sorted(arr[1:])
    return find_lowest_range(new_arr, first)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = list(map(int, input().split()))
        print(solve(x))
