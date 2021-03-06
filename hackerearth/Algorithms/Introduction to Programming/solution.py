"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
string, k = input().strip().split()
ls = list(string + ' ')[::-1]
k = int(k)
a = ['0']
for _ in range(k):
    while a[-1] <= ls[-1]:
        a += ls.pop(),
    a.pop()
print(int(''.join(a) + ''.join(ls[1:][::-1])))
