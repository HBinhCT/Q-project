"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
a = input().strip()
b = input().strip()
count = 0
if a.count('0') == b.count('0'):
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    else:
        print(count // 2)
else:
    print('-1')
