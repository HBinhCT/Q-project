"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = map(int, input().strip().split())
a = sorted(a)
x = a[0]
pre = [x]
for i in range(1, len(a)):
    if a[i] != x:
        x = a[i]
        pre.append(x)
    else:
        pre[-1] += x
found = False
left = 0
right = sum(pre[1:])
if left != right:
    for i in range(1, len(pre)):
        left += pre[i - 1]
        right -= pre[i]
        if left == right:
            found = True
            break
    else:
        left = 0
        right = sum(pre)
        suf = sorted(set(a))
        for i in range(len(pre)):
            left += pre[i]
            right -= pre[i]
            if left == right and suf[i + 1] - suf[i] > 1:
                # choose any number that is not in the list
                found = True
                break
            if left > right:
                break
print('YES' if found else 'NO')
