"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_left

n, k, s, t = map(int, input().strip().split())
if s > t:
    print(-1)
else:
    def is_possible(ranges, num_fuel, distance, max_time):
        v = num_fuel
        u = num_fuel + 1
        time = distance
        fuel = ranges[-1] * 2
        while time <= max_time:
            fuel -= (ranges[u] - ranges[v])
            time += (ranges[u] - ranges[v]) * (num_fuel - v)
            u -= 1
            v -= 1
            if v == -1:
                break
        if time > max_time:
            if v < num_fuel:
                v += 1
                u += 1
            fuel += (ranges[u] - ranges[v])
        return fuel


    vehicles = []
    for i in range(n):
        cost, capacity = map(int, input().strip().split())
        vehicles.append((capacity, cost))
    vehicles.sort()
    pos = [0] + sorted(list(map(int, input().strip().split())))
    if pos[-1] != s:
        pos.append(s)
    distances = [0]
    for i in range(1, k + 2):
        distances.append(pos[i] - pos[i - 1])
    distances.sort()
    if t >= 2 * s:
        capacity = max(distances)
    else:
        capacity = is_possible(distances, k, s, t)
    index = bisect_left(vehicles, (capacity, 0))
    if index == n:
        print(-1)
    else:
        cost = vehicles[index][1]
        for i in range(index + 1, n):
            cost = min(cost, vehicles[i][1])
        print(cost)
