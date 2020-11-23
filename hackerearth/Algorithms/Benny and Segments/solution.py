"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, l = map(int, input().strip().split())
    a = []
    for _ in range(n):
        xl, xr = map(int, input().strip().split())
        if xr - xl <= l:  # 1 ≤ Xl ≤ Xr ≤ 10^6
            a.append((xl, xr))
    a.sort()
    ln = len(a)
    for i in range(ln - 1):
        max_right = a[i][0] + l
        curr_right = a[i][1]
        if curr_right == max_right:
            print('Yes')
            break
        elif curr_right > max_right:
            continue
        else:
            for j in range(i + 1, ln):
                if a[j][0] <= curr_right and a[j][1] <= max_right:
                    curr_right = max(curr_right, a[j][1])
            if curr_right == max_right:
                print('Yes')
                break
    else:
        print('No')
