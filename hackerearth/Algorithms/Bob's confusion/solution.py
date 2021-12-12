"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    c = [list(map(int, input().strip().split())) for _ in range(3)]
    ans = 'YES'
    for i in range(1, 3):
        diff = c[i][0] - c[0][0]
        for j in range(1, 3):
            sub = c[i][j] - c[0][j]
            if sub != diff:
                ans = 'NO'
                break
        else:
            continue
        break
    print(ans)
