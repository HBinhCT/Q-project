n = int(input())
arr = list(map(int, input().strip().split()))
m = max(arr)
seen = [False] * (m + 2)
mex_values = []
mex = 0
for i in arr:
    seen[i] = True
    while seen[mex]:
        mex += 1
    mex_values.append(mex)
print(" ".join(map(str, mex_values)))
