"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for i in range(t):
    s = input()
    ln = len(s)
    if ln == 1:
        print(s)
    else:
        print(s[ln - 2::-2] + s[1 - ln % 2::2])
