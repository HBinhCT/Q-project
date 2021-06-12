"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    prerequisites = {}
    for _ in range(m):
        u, v = map(int, input().strip().split())
        prerequisites[u] = v
    for course in prerequisites:
        if prerequisites[course] in prerequisites and prerequisites[prerequisites[course]] == course:
            print(0)
            break
    else:
        print(1)
