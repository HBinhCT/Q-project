"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = input()
    if '21' in n or int(n) % 21 == 0:
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')
