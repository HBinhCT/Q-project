"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
t = input()
len_s = len(s)
i = 0
for c in t:
    if c == s[i]:
        i += 1
        if i == len_s:
            break
print(i)
