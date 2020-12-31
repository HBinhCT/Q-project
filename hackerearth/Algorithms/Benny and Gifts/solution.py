"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
points = [(0, 0)]
x = y = 0
for move in s:
    if move == 'L':
        y -= 1
    elif move == 'R':
        y += 1
    elif move == 'U':
        x -= 1
    else:
        x += 1
    points.append((x, y))
print(len(points) - len(set(points)))
