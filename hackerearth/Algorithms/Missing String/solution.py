"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from itertools import product
from string import ascii_lowercase

s = input().strip()
x = 1
while True:
    for p in product(ascii_lowercase, repeat=x):
        res = ''.join(p)
        if res not in s:
            print(res)
            break
    else:
        x += 1
        continue
    break
