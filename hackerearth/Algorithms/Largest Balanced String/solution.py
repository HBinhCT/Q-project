"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
opens = ('(', '{', '[')
closes = (')', '}', ']')
for _ in range(t):
    a = input().strip()
    ln = 0
    for i in range(3):
        c1 = a.count(opens[i])
        c2 = a.count(closes[i])
        ln += 2 * min(c1, c2)
    print(ln)
