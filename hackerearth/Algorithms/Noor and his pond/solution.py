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
    sizes = []
    factors = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        sizes.append(s)
        factors.append(e)
    sizes.sort()
    factors.sort()
    count = n
    j = 0
    for i in range(n):
        if factors[i] >= sizes[j]:
            count -= 1
            j += 1
    print(count)
