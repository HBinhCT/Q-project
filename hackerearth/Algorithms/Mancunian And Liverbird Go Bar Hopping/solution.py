"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
directions = list(map(int, input().strip().split()))
to_right_forward = [0] * n
to_right_opposite = [0] * n
to_left_forward = [0] * n
to_left_opposite = [0] * n
for i in range(n - 1):
    if not directions[i]:
        to_right_opposite[i + 1] = to_right_opposite[i] + 1
    else:
        to_right_forward[i + 1] = to_right_forward[i] + 1
    if not directions[n - 2 - i]:
        to_left_forward[n - 2 - i] = to_left_forward[n - 1 - i] + 1
    else:
        to_left_opposite[n - 2 - i] = to_left_opposite[n - 1 - i] + 1
for i in range(n):
    to_right_forward[i] += to_left_forward[i] + 1
    to_right_opposite[i] += to_left_opposite[i] + 1
val = 0
q = int(input())
for _ in range(q):
    q_line = input().strip().split()
    if q_line[0] == 'U':
        val = 1 - val
    else:
        if val % 2:
            print(to_right_forward[int(q_line[-1]) - 1])
        else:
            print(to_right_opposite[int(q_line[-1]) - 1])
