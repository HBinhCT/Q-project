"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    pos = s.find('3')
    pre = s[:pos]
    suf = s[pos:]
    pre += ''.join(c for c in suf if c == '2')
    suf = ''.join(c for c in suf if c != '2')
    print(''.join(sorted(pre)) + suf)
