from sys import stdin

n, q = map(int, stdin.readline().strip().split())
arr = list(map(int, stdin.readline().strip().split()))
lefts = {}
rights = {}
left = right = -1
for i in range(n):
    lefts[i] = left
    if arr[i] == 1:
        left = i
    j = n - 1 - i
    rights[j] = right
    if arr[j] == 1:
        right = j
for _ in range(q):
    p, index = map(int, stdin.readline().strip().split())
    if p == 0:
        print(lefts[index], rights[index])
    else:
        if arr[index] == 0:
            arr[index] = 1
            for i in range(index - 1, -1, -1):
                rights[i] = index
                if arr[i] == 1:
                    break
            for i in range(index + 1, n, 1):
                lefts[i] = index
                if arr[i] == 1:
                    break
