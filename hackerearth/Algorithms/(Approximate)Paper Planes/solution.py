"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
bx, by, bz = map(int, input().strip().split())
bvx, bvy, bvz = map(int, input().strip().split())
mx, my, mz = map(int, input().strip().split())
mvx, mvy, mvz = map(int, input().strip().split())


def f(a, b, c, x):
    return a * x * x + b * x + c


a = (mvx - bvx) ** 2 + (mvy - bvy) ** 2 + (mvz - bvz) ** 2
b = 2 * ((bx - mx) * (bvx - mvx) + (by - my) * (bvy - mvy) + (bz - mz) * (bvz - mvz))
c = (bx - mx) ** 2 + (my - by) ** 2 + (mz - bz) ** 2
if b <= 0:
    if a == 0:
        x = -c / b
        if x < t:
            ans = min(f(a, b, c, x), f(a, b, c, t))
        else:
            ans = f(a, b, c, t)
    elif b == 0:
        ans = c
    else:
        x = -b / (2 * a)
        if x < t:
            ans = min(f(a, b, c, x), f(a, b, c, t))
        else:
            ans = f(a, b, c, t)
else:
    ans = c
ans = ans ** .5
print(f'{ans:0.6f}')
