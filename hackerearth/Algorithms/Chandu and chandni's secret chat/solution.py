"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s, k = input().strip().split()
    k = int(k)
    idxes = list(range(len(s)))
    idxes.sort(key=lambda i: s[i], reverse=True)
    idx = idxes[k - 1]
    word = ''
    for _ in range(len(s)):
        word += s[idx]
        idx = idxes[idx]
    word = word[-1] + word[:-1]
    print(word)
