"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
workers = list(zip(*(iter(a),) * 2))
print(sum(i[0] for i in workers))
