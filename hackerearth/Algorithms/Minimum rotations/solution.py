"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, f, k, c = input().strip().split()
    n = int(n)
    f = int(f)
    k = int(k)
    s = input()
    temp = s
    count = 0
    flag = False
    while temp[:k].count(c) < f:
        if flag and temp == s:
            count = -1
            break
        temp = temp[-1] + temp[:-1]
        flag = True
        count += 1
    print(count)
