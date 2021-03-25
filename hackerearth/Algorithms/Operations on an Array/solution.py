"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = int(input())
a = sorted(map(int, input().strip().split()))
left = 0
right = sum(a)
j = 0
temp = 0
ans = right
for i, element in enumerate(a):
    while a[j] < abs(element - a[j]):
        temp += a[j]
        j += 1
    count = temp
    count += (i - j) * element - left + temp
    count += right - (n - i) * element
    ans = min(ans, count)
    left += element
    right -= element
print(ans)
