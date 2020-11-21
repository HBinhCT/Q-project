"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
# _ = input()
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))
elements = []
for row in range(n):
    for col in range(n):
        elements.append(matrix[row][col])
elements.sort()
left = top = 0
right = bottom = n - 1
i = j = 0
while left <= right and top <= bottom:
    for col in range(left, right + 1):
        matrix[top][col] = elements[j]
        j += 1
    top += 1
    for row in range(top, bottom + 1):
        matrix[row][right] = elements[j]
        j += 1
    right -= 1
    for col in range(right, left - 1, -1):
        matrix[bottom][col] = elements[j]
        j += 1
    bottom -= 1
    for row in range(bottom, top - 1, -1):
        matrix[row][left] = elements[j]
        j += 1
    left += 1
for row in range(n):
    print(*matrix[row])
