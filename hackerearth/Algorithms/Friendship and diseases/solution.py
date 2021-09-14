"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
k, n, m = map(int, input().strip().split())
f = list(map(int, input().strip().split()))
d = list(map(int, input().strip().split()))
tables = [['#'] * (m + 2)]
for _ in range(n):
    tables.append(list('#' + input().strip() + '#'))
tables.append(['#'] * (m + 2))
naive = sorted((f[i], i) for i in range(k))
places = []
indices = []
while naive:
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if tables[row][col] == '.':
                _, i = naive.pop()
                places.append((row, col))
                indices.append(i)
                tables[row][col] = '*'
                if tables[row - 1][col] == '*' and tables[row][col - 1] == '*':
                    tables[row - 1][col - 1] = '#'
                if tables[row - 1][col] == '*' and tables[row][col + 1] == '*':
                    tables[row - 1][col + 1] = '#'
                if tables[row + 1][col] == '*' and tables[row][col - 1] == '*':
                    tables[row + 1][col - 1] = '#'
                if tables[row + 1][col] == '*' and tables[row][col + 1] == '*':
                    tables[row + 1][col + 1] = '#'
                break
        else:
            continue
        break
    else:
        break
ans = [(0, 0) for _ in range(k)]
order = 0
for p in places:
    idx = indices.pop(order)
    ans[idx] = p
    order = -1 if not order else 0
for a in ans:
    print(*a)
