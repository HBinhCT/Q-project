"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
memo = {0: 0}


def exchange(x, dp):
    if x in dp:
        return dp[x]
    else:
        dp[x] = max(x, exchange(x // 2, dp) + exchange(x // 3, dp) + exchange(x // 4, dp))
        return dp[x]


while True:
    try:
        n = int(input())
        print(exchange(n, memo))
    except:
        break
