"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    s = input().strip()
    a_cost = int(input())
    b_cost = int(input())
    cost = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1] and s[i] != '/' and s[-i - 1] != '/':
            cost = -1
            break
        elif s[i] == '/' and s[-i - 1] == '/':
            cost += 2 * min(a_cost, b_cost)
        elif s[i] == '/' and s[-i - 1] != '/':
            cost += a_cost if s[-i - 1] == 'a' else b_cost
        elif s[i] != '/' and s[-i - 1] == '/':
            cost += a_cost if s[i] == 'a' else b_cost
    print(cost)
