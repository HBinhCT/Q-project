from functools import reduce

t = int(input())
for _ in range(t):
    s = input().strip()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print(reduce(lambda x, y: x * (ord(y) - 96), s, 1))
