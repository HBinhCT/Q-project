"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input().strip()
    a = b = c = 0
    ln = len(s)
    ans = (ln * (ln + 1)) // 2
    for i in range(ln):
        if s[i] == 'a':
            a = i + 1
            ans -= min(b, c)
        elif s[i] == 'b':
            b = i + 1
            ans -= min(a, c)
        elif s[i] == 'c':
            c = i + 1
            ans -= min(a, b)
    print(ans)
