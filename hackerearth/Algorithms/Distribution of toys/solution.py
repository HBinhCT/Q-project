"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    total = (n - 1) * (n - 2) // 2
    check = (n - 1) % 2
    for i in range(n - 1 - check, check, -2):
        haft = i // 2
        if haft > n - i:
            total -= 3
        elif haft == n - i:
            total -= 1
    print(total)
