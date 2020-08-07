"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    a, b, c, d, k = map(int, input().strip().split())
    low = 0
    high = 1000000  # 10^4
    while low < high:
        x = low + (high - low + 1) // 2
        fx = a * x * x * x + b * x * x + c * x + d  # ax^3 + bx^2 + cx + d
        if fx == k:
            print(k)
            break
        elif fx < k:
            low = x
        else:
            high = x - 1
    else:
        print(low)
