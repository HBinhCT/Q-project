"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
b = 1
mid = n // 2
while b <= mid:
    x = 2 * n - b * (b + 1)  # Y = b*(b+1)/2
    if x < 0:
        print('NO')
        break
    a = (-1 + (1 + 4 * x) ** .5) / 2
    if int(a) == a:
        print('YES')
        break
    b += 1
