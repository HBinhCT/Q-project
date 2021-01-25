"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
s = input()
t = input()
days = 0
for i, j in zip(s, t):
    ord_i = ord(i)
    ord_j = ord(j)
    k = (ord_j - ord_i) % 26
    days += k // 13
    days += k % 13
print(days)
