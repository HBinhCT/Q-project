"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    x, y = map(int, input().strip().split())
    if x == y:
        print(1)
    elif y < x:
        print(2)
    else:
        i = 1
        while i <= x and i < 64:
            if x >= pow(y, 1 / i) * i:
                break
            i += 1
        print(-1 if i > x else i)
