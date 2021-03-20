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
    s = input().strip()
    ac = s.count('A')
    ans = ac
    for c in s:
        if c == 'A':
            ac -= 1
            if ans > ac:
                ans = ac
        else:
            ac += 1
    print(ans)
