from heapq import heappush, heapify, heappop


def solve(Q, k, s, n):
    # Write your code here
    heap = []
    heapify(heap)
    heappush(heap, (-n, 1))
    choice = {}
    for i in range(k):
        end, start = heappop(heap)
        mid = -end // 2 + start
        if not end % 2 and s[i] == 'L':
            mid -= 1
        choice[mid] = i + 1
        left = mid - start
        if left:
            heappush(heap, (-left, start))
        right = -end - left - 1
        if right:
            heappush(heap, (-right, mid + 1))
    for pos in Q:
        yield choice[pos] if pos in choice else -1


n, k = map(int, input().strip().split())
s = input().strip()
q = int(input())
Q = []
for _ in range(q):
    Q.append(int(input()))

out_ = solve(Q, k, s, n)
print('\n'.join(map(str, out_)))
