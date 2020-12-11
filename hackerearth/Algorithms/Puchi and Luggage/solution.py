"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
M_SIZE = 1000001


def update(frequency, idx, val=1):
    while idx < M_SIZE:
        frequency[idx] += val
        idx += (idx & -idx)


def query(frequency, idx):
    res = 0
    while idx > 0:
        res += frequency[idx]
        idx -= (idx & -idx)
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    weights = []
    for _ in range(n):
        weights.append(int(input()))
    fre = [0] * M_SIZE
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[i] = query(fre, weights[i])
        update(fre, weights[i])
    print(*ans)
