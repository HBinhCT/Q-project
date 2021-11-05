"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n = input()
ln = len(n)
a = [0] * ln
left = right = 0
for i in range(1, ln):
    if i > right:
        left = right = i
        while right < ln and n[right - left] == n[right]:
            right += 1
        a[i] = right - left
        right -= 1
    else:
        if a[i - left] < right - i + 1:
            a[i] = a[i - left]
        else:
            left = i
            while right < ln and n[right - left] == n[right]:
                right += 1
            a[i] = right - left
            right -= 1
ways = 0
for i in range(1, len(a)):
    ways += (a[i] >= i)
print(ways)
