"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
q = int(input())
s = input().strip()
vector = [0] * (len(s) + 1)
for i, c in enumerate(s, 1):
    vector[i] = vector[i - 1] ^ 1 << (ord(c) - 97)  # ord('a') = 97
for _ in range(q):
    l, r = map(int, input().split())
    val = vector[r] ^ vector[l - 1]
    if val & (val - 1):
        print('Impossible')
    else:
        print('Possible')
