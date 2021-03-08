"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = sorted(map(int, input().strip().split()))
j = len(a) - 1
i = 0
ans = 0
to_right = True
while i < j:
    ans += a[j] - a[i]
    if to_right:
        i += 1
    else:
        j -= 1
    to_right = not to_right
ans += a[j] - a[0]
print(ans)
