from heapq import heappush, heappop

heap = []
item_lookup = set()


def add(v):
    heappush(heap, v)
    item_lookup.add(v)


def delete(v):
    item_lookup.discard(v)


def print_smallest():
    while heap[0] not in item_lookup:
        heappop(heap)
    print(heap[0])


queries = {
    1: add,
    2: delete,
    3: print_smallest
}

q = int(input())
for _ in range(q):
    query = list(map(int, input().strip().split()))
    queries[query[0]](*query[1:])
