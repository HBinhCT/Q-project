"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def magic_sum(x, size, adjacency, res):
    val1 = adjacency[x]
    val2 = val3 = 0
    if 2 * x <= size:
        val2 = magic_sum(2 * x, size, adjacency, res)
    if 2 * x + 1 <= size:
        val3 = magic_sum(2 * x + 1, size, adjacency, res)
    res.append(val1 + val2 + val3)
    return val1 + max(val2, val3)


for _ in range(t):
    n = int(input())
    v = [0] + list(map(int, input().strip().split()))
    ans = []
    magic_sum(1, n, v, ans)
    print(max(ans))
