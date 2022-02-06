"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input().strip()
count_a = 0
count_b = 0
count_c = 0
mod = 1000000007
for c in s:
    if c == 'a':
        count_a = (1 + 2 * count_a) % mod
    elif c == 'b':
        count_b = (count_a + 2 * count_b) % mod
    elif c == 'c':
        count_c = (count_b + 2 * count_c) % mod
print(count_c)
