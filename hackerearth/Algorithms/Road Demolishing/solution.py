"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, q = map(int, input().strip().split())
    q -= 1
    ans = n * n - (n % q) * ((n + q - 1) // q) ** 2 - (q - n % q) * (n // q) ** 2
    ans //= 2
    ans = n * (n - 1) // 2 - ans
    print(abs(ans))
