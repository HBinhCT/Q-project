"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
N, K = map(int, input().strip().split())
raju = list(map(int, input().strip().split()))
angles = set()
for i in raju:
    j = 1
    existed = set()
    while True:
        x = i * j % 360
        if x in existed:
            break
        angles.add(x)
        existed.add(x)
        j += 1
rani = list(map(int, input().strip().split()))
for i in rani:
    print('YES' if i in angles else 'NO')
