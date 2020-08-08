"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    a, b, k1, k2, m = map(int, input().split())
    low = 0
    high = 100000
    if a * high ** k1 + b * high ** k2 <= m:
        print('Love is immortal')
    else:
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if a * mid ** k1 + b * mid ** k2 <= m:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)
