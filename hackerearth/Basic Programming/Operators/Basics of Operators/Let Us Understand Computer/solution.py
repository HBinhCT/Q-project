t = int(input())
for _ in range(t):
    x = int(input())
    i = 1
    while i <= int(x**0.5):
        i *= 2
    if x // i >= i // 2:
        print(x - x // i)
    else:
        print(x - i // 2 + 1)
