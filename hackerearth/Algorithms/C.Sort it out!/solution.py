"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
m = int(input())
a = list(map(int, input().strip().split()))
sorted_a = sorted(a)
if sorted_a == a:
    ans = [i for i in range(m)]
else:
    ans = []
    for i in range(m):
        t = a.index(sorted_a[i])
        ans.append(a.index(sorted_a[i]))
        a[t] = -1
print(' '.join(map(str, ans)))
