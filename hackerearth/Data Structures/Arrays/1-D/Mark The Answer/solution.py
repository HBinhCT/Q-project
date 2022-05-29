n, x = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
level = 0
skipped = False
for i in a:
    if i > x:
        if skipped:
            break
        else:
            skipped = True
    else:
        level += 1
print(level)
