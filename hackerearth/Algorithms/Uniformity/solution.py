"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
s = input()
mx = 0
ans = 0
count = {i: 0 for i in 'abc'}
for i in range(len(s)):
    count[s[i]] += 1
    mx = max(mx, count[s[i]])
    if ans - mx < k:
        ans += 1
    else:
        count[s[i - ans]] -= 1
print(ans)
