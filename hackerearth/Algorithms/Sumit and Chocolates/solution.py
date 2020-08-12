"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = map(int, input().strip().split())
q = int(input())
counter = {}
count = 1
box = 1
for i in a:
    for j in range(i):
        counter[count] = box
        count += 1
    box += 1
for _ in range(q):
    i = int(input())
    print(counter[i])
