"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
for word in words:
    if word[::-1] in words:
        ln = len(word)
        print(ln, word[ln // 2])
        break
