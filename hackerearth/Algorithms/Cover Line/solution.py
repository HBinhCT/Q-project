from heapq import heapify, heappop, heappush

n = int(input())
m = int(input())
line_segments = []
for _ in range(m):
    line_segments.append(tuple(map(int, input().strip().split())))
line_segments.sort()
heap = [(0, 0)]
heapify(heap)
for left, right, weight in line_segments:
    max_weight, line_num = heappop(heap)
    while heap and line_num < left - 1:
        max_weight, line_num = heappop(heap)
    if line_num >= left - 1:
        heappush(heap, (max_weight, line_num))
        if right > line_num:
            heappush(heap, (max(max_weight, weight), right))
    else:
        print(-1)
        break
else:
    max_weight, line_num = heappop(heap)
    while heap and line_num != n:
        max_weight, line_num = heappop(heap)
    print(max_weight if line_num == n else -1)
