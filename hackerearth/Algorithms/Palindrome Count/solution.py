"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
n = len(s)
count = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        count += s[i:j] == s[i:j][::-1]
print(count)
