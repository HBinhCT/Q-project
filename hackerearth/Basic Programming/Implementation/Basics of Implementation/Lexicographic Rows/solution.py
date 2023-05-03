def is_interesting(arr):
    for x in range(1, len(arr)):
        if ''.join(arr[x - 1]) > ''.join(arr[x]):
            return False
    return True


n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    matrix.append(input().strip())
count = 0
temp = [[] for _ in range(n)]
for j in range(m):
    for i in range(n):
        temp[i].append(matrix[i][j])
    if not is_interesting(temp):
        for k in temp:
            k.pop()
print(m - len(temp[0]))
