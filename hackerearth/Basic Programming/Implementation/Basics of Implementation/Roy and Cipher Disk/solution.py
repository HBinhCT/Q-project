t = int(input())
for _ in range(t):
    text = "a" + input().strip()
    for i in range(len(text) - 1):
        x = ord(text[i + 1]) - ord(text[i])
        if x > 13:
            x -= 26
        elif x < -12:
            x += 26
        print(x, end=" ")
    print()
