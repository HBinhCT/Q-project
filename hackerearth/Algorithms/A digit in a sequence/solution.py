"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    a, b, k = map(int, input().strip().split())
    pc = 0
    i = 1
    while True:
        c = (pow(10, i) - 1 - a) // b + 1
        if c > 0:
            if i * (c - pc) < k:
                k -= i * (c - pc)
                pc = c
            else:
                c = pc + (k // i)
                k -= i * (c - pc)
                if k == 0:
                    c -= 1
                break
        i += 1
    print(str(a + b * c)[k - 1])
