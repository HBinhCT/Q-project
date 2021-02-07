"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
a = sorted(map(int, input().strip().split()))
samosas = 0
for i in range(n):
    samosas += a[i]
    if samosas > k:
        print(i)
        break
else:
    print(n)
