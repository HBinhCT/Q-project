"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
mx = 10000
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    dp = 1
    for i in a:
        dp |= dp << i
    for i in a:
        possible = False
        for j in range(2, 100):
            if i ** j > mx:
                break
            possible |= dp >> i ** j & 1
        print(1 if possible else 0, end=' ')
    print()
