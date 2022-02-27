"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
gird = [input().strip() for _ in range(n)]
if gird[0][0] == '1':
    print(0)
else:
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        if gird[i][0] == '0':
            result[i][0] = 1
    for i in range(m):
        if gird[0][i] == '0':
            result[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            if gird[i][j] == '0':
                x = i
                y = j
                while x > 0 and result[x - 1][j] == 0:
                    x -= 1
                while y > 0 and result[i][y - 1] == 0:
                    y -= 1
                result[i][j] = result[x - 1][j] + result[i][y - 1]
    print(result[-1][-1] % 1000000007)
