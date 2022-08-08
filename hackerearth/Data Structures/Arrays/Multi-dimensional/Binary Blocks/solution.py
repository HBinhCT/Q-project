def count_toggled_pixels(grid, width, height, divisor):
    remainder = height % divisor
    if remainder:
        for _ in range(divisor - remainder):
            grid.append('0' * width)
        height = height + divisor - remainder
    remainder = width % divisor
    if remainder:
        for x in range(height):
            grid[x] += '0' * (divisor - remainder)
        width = width + divisor - remainder
    res = x = 0
    while x < height:
        y = 0
        while y < width:
            toggled = ''
            for z in range(divisor):
                temp = grid[x + z]
                toggled += temp[y:y + divisor]
            cnt_1 = toggled.count('1')
            cnt_0 = len(toggled) - cnt_1
            res += min(cnt_1, cnt_0)
            y += divisor
        x += divisor
    return res


n, m = map(int, input().strip().split())
pixels = []
for _ in range(n):
    pixels.append(input().strip())
k = 7
ans = n * m
for i in range(k, 1, -1):
    cnt = count_toggled_pixels(pixels, m, n, i)
    ans = min(ans, cnt)
print(ans)
