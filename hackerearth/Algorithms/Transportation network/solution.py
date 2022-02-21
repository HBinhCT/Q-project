"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, q = map(int, input().strip().split())
railway = 0
road = 0
for _ in range(q):
    b, u, v = map(int, input().strip().split())
    if b == 1:
        railway += 1
    else:
        road += 1
    print('YES' if railway == road else 'NO')
