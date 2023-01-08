t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    big_lefts = [0] * n
    big_lefts[0] = heights[0]
    big_rights = [0] * n
    big_rights[n - 1] = heights[n - 1]
    for i in range(1, n):
        big_lefts[i] = max(big_lefts[i - 1], heights[i])
        j = n - 1 - i
        big_rights[j] = max(big_rights[j + 1], heights[j])
    ans = 0
    for i in range(n):
        ans = (ans + (min(big_lefts[i], big_rights[i]) - heights[i])) % 1000000007
    print(ans)
