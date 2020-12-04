"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, s = map(int, input().strip().split())
    height = list(map(int, input().strip().split()))
    lower = greater = equal = 0
    for i in height:
        if i > s:
            greater += 1
        elif i < s:
            lower += 1
        else:
            equal += 1
    print(abs(lower - greater) + (equal % 2 and equal > 0))
