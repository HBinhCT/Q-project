p = input().strip()
min_steps = len(p) // 2
left = 0
right = min_steps
while right > 0:
    count = 0
    for i, j in zip(p[:len(p) // 2], p[:(len(p) - 1) // 2:-1]):
        count += (i != j)
    min_steps = min(min_steps, count + left)
    p = p[1:]
    right -= 1
    left += 1
print(min_steps)
