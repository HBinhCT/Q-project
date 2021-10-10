"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(input().strip())
    print('No' if len(set(matrix)) < n else 'Yes')
