def get_total(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


def update(array, length, index, value):
    while index <= length:
        array[index] += value
        index += index & -index


n = int(input())
elements = set()
searches = set()
operations = []
for _ in range(n):
    operation = list(map(int, input().strip().split()))
    if operation[0] == 1:
        elements.add(operation[1])
    elif operation[0] == 2:
        elements.add(operation[2])
        operation[1] -= 1
        searches.add((operation[1], operation[2]))
    operations.append(operation)
elements = sorted(elements)
searches = sorted(searches)
indexes = {v: k for k, v in enumerate(elements, start=1)}
stack = [0] * n
len_stack = 0
len_tree = 1 << (len(indexes).bit_length())
tree = [0] * (len_tree + 1)
len_searches = len(searches)
search_idx = 0
cur_k, cur_x = searches[search_idx]
res = dict()
for i in range(n):
    o, *query = operations[i]
    if o == 0:
        len_stack -= 1
        val = stack[len_stack]
        update(tree, len_tree, val, -1)
    elif o == 1:
        a = query[0]
        val = indexes[a]
        update(tree, len_tree, val, 1)
        stack[len_stack] = val
        len_stack += 1
    elif o == 2:
        k, x = query
        print(res[k, x])
    while i == cur_k:
        val = indexes[cur_x]
        res[i, cur_x] = get_total(tree, min(val - 1, len_tree))
        search_idx += 1
        cur_k, cur_x = searches[search_idx] if search_idx < len_searches else (-1, -1)
