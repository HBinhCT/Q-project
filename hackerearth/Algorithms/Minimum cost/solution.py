"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import heapq


def calc(free_positions, num):
    visited = [False] * (num + 1)
    travel = [(0, 1)]
    heapq.heapify(travel)
    while travel:
        cost, index = heapq.heappop(travel)
        if index == num:
            return cost
        if not visited[index]:
            visited[index] = True
            if index - 1 >= 1 and not visited[index - 1]:
                heapq.heappush(travel, (cost + 1, index - 1))
            if index + 1 <= num and not visited[index + 1]:
                heapq.heappush(travel, (cost + 1, index + 1))
            if not visited[free_positions[index - 1]]:
                heapq.heappush(travel, (cost, free_positions[index - 1]))


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().strip().split()))
    print(calc(p, n))
