"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, l, r = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
mod = 1000000007  # 10 ** 9 + 7
temp = [0] * n
for i in range(n - 1, -1, -1):
    total = 0
    for j in range(i, n):
        total += a[j]
        if total > r:
            break
        if total >= l:
            if j == n - 1:
                temp[i] = (temp[i] + 1) % mod
            else:
                temp[i] = (temp[i] + temp[j + 1]) % mod
print(temp[0])
