from collections import deque

n = int(input())
sequences = []
for _ in range(n):
    sequences.append(deque([int(i) - 1 for i in input().strip().split()]))
count = 0
while any(map(len, sequences)):
    available_guests = [True] * n
    is_consistent = False
    for i in range(n):
        if not available_guests[i]:
            continue
        if sequences[i]:
            j = sequences[i][0]
            if not available_guests[j] or i != sequences[j][0]:
                continue
            available_guests[i] = available_guests[j] = False
            sequences[i].popleft()
            sequences[j].popleft()
            is_consistent = True
    if not is_consistent:
        print(-1)
        break
    count += 1
else:
    print(count * 3)
