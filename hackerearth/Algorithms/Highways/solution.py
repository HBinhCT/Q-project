"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, k = map(int, input().strip().split())
cities = []
for _ in range(k):
    cities.append(tuple(map(int, input().strip().split())))
cities.sort()
min_y_from_begin = [n + 1]
max_y_from_begin = [-1]
min_y_from_end = [n + 1]
max_y_from_end = [-1]
for _, y in cities:
    min_y_from_begin.append(min(min_y_from_begin[-1], y))
    max_y_from_begin.append(max(max_y_from_begin[-1], y))
for _, y in reversed(cities):
    max_y_from_end.append(max(max_y_from_end[-1], y))
    min_y_from_end.append(min(min_y_from_end[-1], y))
min_y_from_end.reverse()
max_y_from_end.reverse()


def check(x, size, city_list, min_starts, max_start, min_ends, max_ends):
    left = 0
    for right in range(size):
        while city_list[left][0] + x < city_list[right][0] - x:
            left += 1
        if min(min_starts[left], min_ends[right + 1]) + x >= max(max_start[left], max_ends[right + 1]) - x:
            return True
    return False


low = 0
high = n
while low < high:
    mid = (low + high) // 2
    if check(mid, k, cities, min_y_from_begin, max_y_from_begin, min_y_from_end, max_y_from_end):
        high = mid
    else:
        low = mid + 1
print(low)
