"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
t = int(input())


def find_min_cost(the_cost):
    ln = len(the_cost)
    if not ln:
        return 0
    for i in range(1, ln):
        the_cost[i][0] += min(the_cost[i - 1][1], the_cost[i - 1][2])
        the_cost[i][1] += min(the_cost[i - 1][0], the_cost[i - 1][2])
        the_cost[i][2] += min(the_cost[i - 1][0], the_cost[i - 1][1])
    return min(the_cost[-1])


for _ in range(t):
    n = int(input())
    costs = [list(map(int, input().strip().split())) for _ in range(n)]
    print(find_min_cost(costs))
