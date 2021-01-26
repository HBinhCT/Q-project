"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
ln = len(s)
word = list(s)
if word[0] == '?':
    word[0] = 'b' if ln > 1 and word[1] == 'a' else 'a'
for i in range(1, ln - 1):
    if word[i] == '?':
        word[i] = 'b' if word[i + 1] == 'a' or word[i - 1] == 'a' else 'a'
if word[-1] == '?':
    word[-1] = 'b' if ln > 1 and word[-2] == 'a' else 'a'
print(*word, sep='')
