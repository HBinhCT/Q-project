"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input()
    k = int(input())
    diff = []
    ln = len(s)
    if (ln % 2 == 0 and k % 2 == 1) or (ln % 2 == 1 and k % 2 == 0):
        print('-1')
    else:
        for i in range(ln // 2):
            diff.append(abs(ord(s[i]) - ord(s[ln - 1 - i])))
        diff.sort()
        if diff.count(0) >= k // 2:
            k -= (k % 2 == 1)
            c = diff.count(0) * 2 - k
            c //= 2
            print(c)
        else:
            print(sum(diff[:k // 2]))
