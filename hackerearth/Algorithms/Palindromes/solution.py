"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input().strip()
temp = s
if len(set(s)) > 1:
    while s == temp[::-1]:
        temp = temp[:-1]
    print(len(temp))
else:
    print(0)
