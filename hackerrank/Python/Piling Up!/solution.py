from collections import deque

for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().rstrip().split()))
    for j in range(len(queue) - 1):
        if queue[0] >= queue[1]:
            queue.popleft()
        elif queue[-1] >= queue[-2]:
            queue.pop()
        else:
            print('No')
            break
    else:
        print('Yes')
