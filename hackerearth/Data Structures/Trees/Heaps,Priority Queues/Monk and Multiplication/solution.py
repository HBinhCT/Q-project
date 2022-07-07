from heapq import heappush, heappop

n = int(input())
a = list(map(int, input().strip().split()))
heap = []
product = 1
for i in range(n):
    if i < 2:
        print(-1)
        heappush(heap, a[i])
        product *= a[i]
    else:
        if i == 2:
            product *= a[i]
            heappush(heap, a[i])
        elif a[i] > heap[0]:
            val = heappop(heap)
            product //= val
            product *= a[i]
            heappush(heap, a[i])
        print(product)
