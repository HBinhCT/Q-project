"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
mod = 1000000007
fact = [1]
for i in range(1, 1001):
    fact.append((fact[-1] * i) % mod)
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    even = odd = 0
    for i in a:
        if i % 2:
            odd += 1
        else:
            even += 1
    ans = 0
    for i in range(odd + 1):
        if i % 2:
            j = k - i
            if 0 <= j <= even:
                ans += fact[odd] * pow(fact[i] * fact[odd - i] % mod, mod - 2, mod) * fact[even] * pow(
                    fact[j] * fact[even - j] % mod, mod - 2, mod)
                ans %= mod
    print(ans)
