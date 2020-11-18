"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
vaccines = list(map(int, input().strip().split()))
midichlorians = list(map(int, input().strip().split()))
count = 0
ln = len(vaccines)
for i in range(ln):
    count += (vaccines[i] > midichlorians[i])
print('Yes' if count == ln else 'No')
