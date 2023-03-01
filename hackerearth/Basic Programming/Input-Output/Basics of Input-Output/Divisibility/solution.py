"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

N = int(input())
data = [int(x) for x in input().split()]

# Write your code here
# ans = 
ans = 'No' if data[-1] % 10 else 'Yes'
print(ans)
