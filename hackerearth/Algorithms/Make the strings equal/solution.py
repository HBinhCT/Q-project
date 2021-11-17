"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import Counter


def check(string1, string2):
    if Counter(string1) != Counter(string2):
        return False
    if any(v > 1 for v in Counter(string1).values()):
        return True
    count = 0
    while len(string1) > 2:
        pos = string2.index(string1[0])
        count += pos
        string1 = string1[1:]
        string2 = string2[:pos] + string2[pos + 1:]
    return (count % 2 == 1) != (string1 == string2)


q = int(input())
for _ in range(q):
    n = int(input())
    s = input().strip()
    t = input().strip()
    if check(s, t):
        print('YES')
    else:
        print('NO')
