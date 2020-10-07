"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def num_glowing(n, primes):
    if len(primes) == 0:
        return 0
    p = primes[0]
    m = n // p
    ps = primes[1:]
    return m + num_glowing(n, ps) - num_glowing(m, ps)


for _ in range(t):
    s = input()
    k = int(input())
    switches = []
    for i in range(len(s)):
        if s[i] == '1':
            switches.append(i + 1)
    left = 1
    right = 40 * k
    u = 0
    v = num_glowing(right, switches)
    while left + 1 < right:
        mid = (left * (v - k) + right * (k - u)) // (v - u)
        if mid <= left:
            mid += 1
        if mid >= right:
            mid -= 1
        x = num_glowing(mid, switches)
        if x >= k:
            right = mid
            v = x
        else:
            left = mid
            u = x
    print(right)
