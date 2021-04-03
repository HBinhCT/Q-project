"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = map(int, input().split())
num = 1
for i in a:
    num = num * ((pow(i + 1, 2) + 1) // 2) % 1000000007
print(num)
