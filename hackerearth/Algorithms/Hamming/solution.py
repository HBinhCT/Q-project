"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
strings = []
for i in range(n):
    s = input().strip()
    strings.append(s)
ans = []
for i in range(m):
    counter = [0] * 26
    for j in range(n):
        counter[ord(strings[j][i]) - 97] += 1
    most = max(counter)
    for j in range(26):
        if counter[j] == most:
            ans.append(chr(97 + j))
            break
print(''.join(ans))
