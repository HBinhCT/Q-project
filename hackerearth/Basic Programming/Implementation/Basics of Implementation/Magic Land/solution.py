def get_max(arr, size):
    res = 1
    for x in arr:
        temp = [1] * size
        for y in range(1, len(x)):
            if x[y] == x[y - 1]:
                temp[y] = temp[y - 1] + 1
        res = max(max(temp), res)
    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().strip().split())))
    max_row = get_max(a, m)
    max_col = get_max(list(zip(*a)), n)
    print(max_row * max_col)
