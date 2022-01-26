"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    for i in range(n + 1):
        a = k - m * (n - i)
        b = 2 * i - n
        if b != 0 and a % b == 0 and 0 <= a / b <= m:
            print('Yes')
            break
    else:
        print('No')
