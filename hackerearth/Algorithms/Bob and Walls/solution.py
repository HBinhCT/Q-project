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
    a = map(int, input().strip().split())
    count = 0
    max_height = -1
    for i in a:
        if i > max_height:
            count += 1
            max_height = i
    print(count)
