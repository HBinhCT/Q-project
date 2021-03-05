"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = list(map(int, input().strip().split()))
exist = False
for i in range(n - 1, 0, -1):
    j = 0
    while not exist and j < n - i:
        if a[j] == a[j + i]:
            print(i + 1)
            exist = True
        else:
            j += 1
    if exist:
        break
else:
    print(0)
