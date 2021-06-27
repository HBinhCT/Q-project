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
    a = map(int, input().strip().split())
    choose = set()
    s = []
    for i, v in enumerate(a, 1):
        if v not in choose:
            choose.add(v)
            s.append(i)
    print(len(s))
    print(*s)
