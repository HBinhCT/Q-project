"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for case in range(t):
    n = int(input())
    x = list(map(int, input().strip().split()))
    mx = 0
    points = x[0]
    for i in x[1:]:
        temp = max(mx, points)
        points = i + mx
        mx = temp
    print(f'Case {case + 1}: {str(max(points, mx))}')
