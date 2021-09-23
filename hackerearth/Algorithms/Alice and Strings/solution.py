"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
a = input().strip()
b = input().strip()
lna = len(a)
lnb = len(b)
if lna == lnb:
    for i in range(lna):
        if a[i] > b[i]:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')
