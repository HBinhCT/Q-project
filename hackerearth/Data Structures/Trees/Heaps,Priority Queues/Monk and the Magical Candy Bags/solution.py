from heapq import heappop, heapify, heappush
from math import floor

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    candies = [-int(i) for i in input().strip().split()]
    heapify(candies)
    max_candies = 0
    for _ in range(k):
        candy = -heappop(candies)
        max_candies += candy
        heappush(candies, -floor(candy / 2))
    print(max_candies)
