"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    for i in range(n):
        pos = i
        for j in range(i + 1, n):
            if j - i > k:
                break
            if a[j] < a[pos]:
                pos = j
        for j in range(pos, i, -1):
            a[j], a[j - 1] = a[j - 1], a[j]
        k -= pos - i
    print(*a)
