"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input()
    l_count = s.count('L')
    r_count = s.count('R')
    u_count = s.count('U')
    d_count = s.count('D')
    print(sum(divmod(abs(l_count - r_count), 2)) + sum(divmod(abs(u_count - d_count), 2)))
