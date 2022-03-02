"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import random


def check_prime(num):
    if num in (2, 3, 5, 7):
        return True
    else:
        a = num - 1
        while not a & 1:
            a >>= 1
        b = random.randint(2, num - 2)
        c = pow(b, a, num)
        if c == 1 or c == num - 1:
            return True
        while a < num - 1:
            c = ((c * c) % num)
            a *= 2
            if c == 1:
                return False
            if c == num - 1:
                return True


t = int(input())
for _ in range(t):
    x = input()
    n = len(x)
    dp = [[True] * (n + 1) for _ in range(n)]
    for i in range(2, n + 1):
        j = 0
        k = i
        while k <= n:
            if (not check_prime(int(x[j:k]))) and dp[j][k - 1] and dp[j + 1][k]:
                dp[j][k] = False
            j += 1
            k += 1
    if dp[0][n]:
        print('Alice')
    else:
        print('Bob')
