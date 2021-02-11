"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s, k = input().strip().split()
    ln = len(s)
    n = int(s, 2)
    k = 2 ** int(k) - 1
    time = 0
    for _ in range(ln):
        if not n & 1:
            n ^= k
            time += 1
        n >>= 1
    print(-1 if n else time)
