"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
res = []
for i in range(64):
    low = 0
    high = n
    while low < high:
        mid = (low + high + 1) // 2
        x = mid * 2 + 1
        if x * (x - 1) // 2 + x * (2 ** i - 1) > n:
            high = mid - 1
        else:
            low = mid
    x = low * 2 + 1
    if x * (x - 1) // 2 + x * (2 ** i - 1) == n:
        res.append(x * 2 ** i)
    if x * (x - 1) // 2 + x * (2 ** (i + 1) - 1) == n:
        res.append(x * 2 ** (i + 1))
if res:
    ans = 0
    for j in set(res):
        ans ^= j
    print(ans)
else:
    print(-1)
