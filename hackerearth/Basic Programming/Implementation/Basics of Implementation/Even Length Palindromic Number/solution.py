from string import digits

t = int(input())
for _ in range(t):
    n = input().strip()
    digit = '0'
    count = -1
    for d in digits:
        c = n.count(d)
        if c > count:
            digit, count = d, c
    print(digit)
