"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
rooms = []
for _ in range(n):
    rooms.append(list(map(int, input().strip().split())))
for i in reversed(range(n - 1)):
    for j in range(n):
        if j == 0:
            rooms[i][j] += max(rooms[i + 1][j], rooms[i + 1][j + 1])
        elif j == n - 1:
            rooms[i][j] += max(rooms[i + 1][j], rooms[i + 1][j - 1])
        else:
            rooms[i][j] += max(rooms[i + 1][j], rooms[i + 1][j + 1], rooms[i + 1][j - 1])
print(max(rooms[0]))
