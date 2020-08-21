"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())


def cube(x):
    return round(abs(x) ** (1 / 3))


limit = cube(n)
shieves = [True] * (limit + 1)
num = 2
while num * num <= limit:
    if shieves[num]:
        for i in range(num * num, limit + 1, num):
            shieves[i] = False
    num += 1
n -= 9
i = 2
while i * i * i <= n:
    if shieves[i]:
        core_i3 = i * i * i
        temp = cube(n - core_i3)
        if temp * temp * temp + core_i3 == n and shieves[temp]:
            print(1, 2, min(temp, i), max(temp, i))  # a = 1, b = 2
            break
    i += 1
else:
    print(-1)
