s = input().strip()
x = y = 0
for c in s:
    if 'L' == c:
        x -= 1
    elif 'R' == c:
        x += 1
    elif 'U' == c:
        y += 1
    elif 'D' == c:
        y -= 1
print(x, y)
