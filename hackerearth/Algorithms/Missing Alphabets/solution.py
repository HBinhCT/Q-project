"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    e = input().strip()
    m = int(input())
    d = {v: i for i, v in enumerate(e)}
    s = []
    for _ in range(m):
        s.append(input().strip())
    s.sort(key=lambda x: [d[i] for i in x])
    print(*s, sep='\n')
