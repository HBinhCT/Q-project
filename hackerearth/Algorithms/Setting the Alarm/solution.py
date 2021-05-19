"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def calc(x):
    x //= 60
    if 6 < x < 18:
        return 1 + abs(12 - x)
    return min(x, 24 - x)


for _ in range(t):
    a = input()
    b = input()
    h1, m1 = int(a[0:2]), int(a[3:5])
    h2, m2 = int(b[0:2]), int(b[3:5])
    h1 %= 12
    h2 %= 12
    h1 += (a[-2:] == 'pm') * 12
    h2 += (b[-2:] == 'pm') * 12
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    p = abs(t2 - t1)
    ans = 0
    if p % 60 >= 30:
        ans += 60 - p % 60
        if p % 60 > 30:
            p += 60 - p % 60
        else:
            ans = 30
            if calc(p + 30) > calc(p - 30):
                p -= 30
            else:
                p += 30
    else:
        ans += p % 60
        p -= p % 60
    p //= 60
    if 6 < p < 18:
        ans += 1
        p = abs(12 - p)
    else:
        p = min(p, 24 - p)
    ans += p
    print(ans)
