"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def check_code(num1, num2):
    val = 0
    num = num1
    while num:
        num, val = num // 10, val + num % 10
    return num1 - val >= num2


for _ in range(t):
    n, m = map(int, input().strip().split())
    if m >= n:
        print('0')
    elif not check_code(n, m):
        print('0')
    else:
        low = m
        high = n
        while low <= high:
            mid = (low + high) // 2
            if check_code(mid, m):
                high = mid - 1
            else:
                low = mid + 1
        print(n - high)
