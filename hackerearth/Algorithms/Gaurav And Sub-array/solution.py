"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = [None] * n
for i in range(n):
    count = 0
    num = a[i]
    while num:
        num = num & (num - 1)  # It's figuring out if n is either 0 or an exact power of two.
        count += 1
    b[i] = count
for _ in range(q):
    k = int(input())
    if k == 0:
        print(1)
        continue
    val = start = end = 0
    res = n + 1
    while end < n:
        while val < k and end < n:
            val += b[end]
            end += 1
        while val >= k and start < n:
            res = min(res, end - start)
            val -= b[start]
            start += 1
    print(res if res <= n else -1)
