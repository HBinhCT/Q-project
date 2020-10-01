"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
s = input()
q = input()
numbers = map(int, input().strip().split())
n = len(s)
counter = [0]
for i in range(n):
    counter.append(counter[i] + n - i)
for i in numbers:
    if i > n * (n + 1) // 2:
        print(-1)
    else:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            if counter[mid] >= i:
                high = mid - 1
            else:
                low = mid + 1
        print(s[high:high + i - counter[high]])
